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
        
    prcp_index = header_row.index('PRCP')
    name_index = header_row.index('NAME')
    date_index = header_row.index('DATE')
    
    dates, precipitations = [], []
    for row in reader:
        current_data = datetime.strptime(row[date_index], "%Y-%m-%d")
        year = current_data.year
        try:
            precipitation = float(row[prcp_index])
        except ValueError:
            print(f'Missing data for {current_data}')
        else:
            dates.append(current_data)
            precipitations.append(precipitation)

            
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(dates, precipitations, c='blue')
    title = f'Annual precipitations - {year}\n{name_index}'
    
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Precipitations', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()