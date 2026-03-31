import csv

from matplotlib import pyplot as plt
from datetime import datetime 

filename = 'Weather/data/death_valley_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
        
    dates, highs, lows = [], [], []
    for row in reader:
        current_data = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_data}')
        else:
            dates.append(current_data)
            highs.append(high)
            lows.append(low)
            
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    
    title = 'Daily high and low temperatures - 2021\nDeath Valley, CA'
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()