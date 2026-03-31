import csv

from matplotlib import pyplot as plt
from datetime import datetime 

filename = 'Weather/data/death_valley_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
        
    dates, precipitations = [], []
    for row in reader:
        current_data = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            precipitation = float(row[5])
        except ValueError:
            print(f'Missing data for {current_data}')
        else:
            dates.append(current_data)
            precipitations.append(precipitation)

            
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(dates, precipitations, c='blue')
    title = 'Daily precipitations - 2021\nDeath Valley, CA'
    
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Precipitations', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()