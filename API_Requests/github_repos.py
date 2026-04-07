import requests
from plotly import offline

while True:
    print("Enter 'q' to quit.")
    answer = input("Enter a programming language: ")
    answer = answer.lower().strip()

    if answer == 'q':
        break

    url = f'https://api.github.com/search/repositories?q=language:{answer}&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        response_dict = r.json()
    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")
        continue

    print(f"Status code: {r.status_code}")
    repo_dicts = response_dict.get('items', [])

    if not repo_dicts:
        print("No repositories found for this language.")
        continue

    repo_links, stars, labels = [], [], []

    for repo_dict in repo_dicts:
        repo_name = repo_dict.get('name', 'No name')
        repo_url = repo_dict.get('html_url', '')
        repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")
        stars.append(repo_dict.get('stargazers_count', 0))

        owner = repo_dict.get('owner', {}).get('login', 'Unknown')
        description = repo_dict.get('description') or 'No description provided.'
        label = f"{owner}<br />{description}"
        labels.append(label)

    data = {
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
        },
        'opacity': 0.6,
    }

    my_layout = {
        'title': f'Most-Starred {answer.title()} Projects on GitHub',
        'xaxis': {'title': 'Repository'},
        'yaxis': {'title': 'Stars'},
    }

    fig = {'data': [data], 'layout': my_layout}
    offline.plot(fig, filename='API_Requests/Stars.html')
    break

