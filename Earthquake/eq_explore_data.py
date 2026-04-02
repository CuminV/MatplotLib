import json

from plotly.graph_objs import Layout
from plotly import offline  
from pathlib import Path


base_dir = Path(__file__).resolve().parent 
filepath = base_dir / 'data' / 'readable_eq_data.json'
with open(filepath, encoding='utf-8') as f:
    all_eq_data = json.load(f)  

title = all_eq_data['metadata']['title']
all_eq_data = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_data:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])
    
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')