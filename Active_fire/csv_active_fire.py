import csv

from datetime import datetime
from plotly.graph_objs import Layout
from plotly import offline  
from pathlib import Path


base_dir = Path(__file__).resolve().parent
filepath = base_dir / 'data' / 'MODIS_C6_1_Global_24h.csv'
with open(filepath, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lons_index = header_row.index('longitude')
    lats_index = header_row.index('latitude')
    bright_index = header_row.index('brightness')
    dates_index = header_row.index('acq_date')

    num_rows = 5000
    brightness_values, lons, lats, hover_text = [], [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[dates_index], "%Y-%m-%d")
            lon = float(row[lons_index])
            lat = float(row[lats_index])
            brightness = float(row[bright_index])
            label = f'Brightness: {brightness}, Date: {date.strftime("%Y-%m-%d")}'

        except ValueError:
            print(f'Missing data for row: {row}')
        else:
            lons.append(lon)
            lats.append(lat)
            brightness_values.append(brightness)
            hover_text.append(label)
        if len(lons) >= num_rows:
            break

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [0.05 * brightness for brightness in brightness_values],
        'color': brightness_values,
        'colorscale': 'Reds',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    }
}]
my_layout = Layout(title='Global Active Fires in the Last 24 Hours')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_active_fires.html')
