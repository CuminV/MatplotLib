import csv
import sys

from matplotlib import pyplot as plt
from datetime import datetime 
from tkinter import Tk, filedialog


root = Tk()
root.withdraw()

def choose_file():
    filename = filedialog.askopenfilename(
        title="Choise CSV file",
    initialdir="Weather/data",
    filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    
    if not filename:
        return None
    
    return filename


filename = choose_file()

if filename is None:
    print("File not selected")
    sys.exit()
    
    
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    tmax_index = header_row.index('TMAX')
    tmin_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')
    date_index = header_row.index('DATE')
    
        
    dates, highs, lows = [], [], []
    for row in reader:
        current_data = datetime.strptime(row[date_index], "%Y-%m-%d")
        year = current_data.year
        try:
            high = int(row[tmax_index])
            low = int(row[tmin_index])
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
    
    title = f'Annual high and low temperatures - {year}\n{row[name_index]}'
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()