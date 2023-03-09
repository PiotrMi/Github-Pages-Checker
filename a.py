import requests

# Replace 'username' with your GitHub username
username = 'piotrmi'

# Fetch all repositories owned by the user
url = f'https://api.github.com/users/{username}/repos'
response = requests.get(url)
repos = response.json()

print(response.text)

if isinstance(repos, dict) and repos.get('message') == 'Not Found':
    print(f'Error: {repos["message"]}')
    exit()

# Filter repositories that have GitHub Pages enabled
pages_repos = []
for repo in repos:
    url = f'https://api.github.com/repos/{username}/{repo["name"]}/pages'
    response = requests.get(url)
    pages = response.json()
    if pages.get('message') == 'Not Found':
        continue
    pages_repos.append(repo['name'])

# Print the list of repositories with GitHub Pages enabled
print(f'Repositories with GitHub Pages enabled: {", ".join(pages_repos)}')
