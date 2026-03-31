import csv

from datetime import datetime
from matplotlib import pyplot as plt 

class Weather():
    
    def __init__(self, filename):
        self.dates = []
        self.precipitations = []
        self.highs = [] 
        self.lows = []
        self.filename = filename
        self.open_file()
        
    def open_file(self):
        with open(self.filename) as f:
            self.reader = csv.reader(f)
            header_row = next(self.reader)
                
            self.prcp_index = header_row.index('PRCP')
            self.name_index = header_row.index('NAME')
            self.date_index = header_row.index('DATE')
            self.tmax_index = header_row.index('TMAX')
            self.tmin_index = header_row.index('TMIN')
            
            self.rows = list(self.reader)
            
    def high_and_low_temperature(self):
        self.dates = []
        self.highs = []
        self.lows = []
        for self.row in self.rows:
            current_data = datetime.strptime(self.row[self.date_index], "%Y-%m-%d")
            self.year = current_data.year
            try:
                high = int(self.row[self.tmax_index])
                low = int(self.row[self.tmin_index])
            except ValueError:
                print(f'Missing data for {current_data}')
            else:
                self.dates.append(current_data)
                self.highs.append(high)
                self.lows.append(low)
            

    def get_precipitation(self):
        self.dates = []
        self.precipitations = []
        for self.row in self.rows:
            current_data = datetime.strptime(self.row[self.date_index], "%Y-%m-%d")
            self.year = current_data.year
            try:
                precipitation = float(self.row[self.prcp_index])
            except ValueError:
                print(f'Missing data for {current_data}')
            else:
                self.dates.append(current_data)
                self.precipitations.append(precipitation)
        
        
        
    def plot(self, mode):
        
        plt.style.use('classic')
        fig, ax = plt.subplots()
        
        if mode == 'temperature':
            ax.plot(self.dates, self.highs, c='red', alpha=0.5)
            plt.plot(self.dates, self.lows, c='blue', alpha=0.5)
            title = f'Annual high and low temperatures - {self.year}\n{self.row[self.name_index]}'
            plt.fill_between(self.dates, self.highs, self.lows, facecolor='blue', 
                            alpha=0.1)
            plt.ylabel('Temperature (F)', fontsize=16)
            
        elif mode == 'precipitation':
            ax.plot(self.dates, self.precipitations, c='blue')
            title = f'Annual precipitations - {self.year}\n{self.row[self.name_index]}'
            plt.ylabel('Precipitations', fontsize=16)

        plt.title(title, fontsize=20)
        plt.xlabel('', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        fig.autofmt_xdate()
        plt.show()
        
