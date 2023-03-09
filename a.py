import requests

# Replace 'username' with your GitHub username
username = 'username'

# Fetch all repositories owned by the user
url = f'https://api.github.com/users/{username}/repos'
response = requests.get(url)
repos = response.json()

# Filter repositories that have GitHub Pages enabled
pages_repos = []
for repo in repos:
    url = f'https://api.github.com/repos/{username}/{repo["name"]}/pages'
    response = requests.get(url)
    pages = response.json()
    if pages['message'] != 'Not Found':
        pages_repos.append(repo['name'])

# Print the list of repositories with GitHub Pages enabled
print(f'Repositories with GitHub Pages enabled: {", ".join(pages_repos)}')
