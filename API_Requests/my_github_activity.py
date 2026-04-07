import requests
from collections import Counter
from plotly import offline


url = 'https://api.github.com/users/CuminV/events/public'
headers = {'Accept': 'application/vnd.github+json'}

try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    events = r.json()
except requests.exceptions.RequestException as error:
    print(f"Request error: {error}")
else:
    print(f"Status code: {r.status_code}")

    activity_by_day = Counter()

    for event in events:
        event_date = event['created_at'][:10]
        activity_by_day[event_date] += 1

    dates = sorted(activity_by_day.keys())
    activity_counts = [activity_by_day[date] for date in dates]

    data = [{
        'type': 'bar',
        'x': dates,
        'y': activity_counts,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'My GitHub Activity by Day',
        'xaxis': {'title': 'Date'},
        'yaxis': {'title': 'Number of Events'},
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='API_Requests/My_GitHub_Activity.html')
