import requests
from operator import itemgetter
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

#Create a list of the IDs for the top 30 stories.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=lambda x: x['comments'], 
                          reverse=True)

news_links, comments, labels = [], [], []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    hn_link = submission_dict['hn_link']
    news_links.append(f"<a href='{hn_link}'>{title}</a>")
    comments.append(submission_dict['comments'])
    labels.append(f"Comments: {submission_dict['comments']}")


data = {
    'type': 'bar',
    'x': news_links,
    'y': comments,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}

my_layout = {
    'title': 'Most-Commented Stories on Hacker News',
    'xaxis': {'title': 'Stories'},
    'yaxis': {'title': 'Comments'},
}

fig = {'data': [data], 'layout': my_layout}
offline.plot(fig, filename='API_Requests/Comments.html')

