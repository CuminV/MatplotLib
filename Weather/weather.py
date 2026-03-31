import csv

from datetime import datetime
from matplotlib import pyplot as plt 

class Weather:
    
    def __init__(self, filename):
        self.filename = filename
        self.read_file()
        
    def read_file(self):
        with open(self.filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header_row = next(reader)
                
            self.prcp_index = header_row.index('PRCP')
            self.name_index = header_row.index('NAME')
            self.date_index = header_row.index('DATE')
            self.tmax_index = header_row.index('TMAX')
            self.tmin_index = header_row.index('TMIN')
            
            self.rows = list(reader)
            if not self.rows:
                raise ValueError('CSV file contains no data rows.')
            self.place_name = self.rows[0][self.name_index]
            
                
    def get_temperature_data(self):
        dates = []
        highs = []
        lows = []
        year = None
        
        for row in self.rows:
            current_date = datetime.strptime(row[self.date_index], "%Y-%m-%d")
            year = current_date.year
            try:
                high = int(row[self.tmax_index])
                low = int(row[self.tmin_index])
            except ValueError:
                print(f'Missing data for {current_date}')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        if not dates:
            raise ValueError('No valid temperature data found.')
        return dates, highs, lows, year

    def get_precipitation_data(self):
        dates = []
        precipitations = []
        year = None
        
        for row in self.rows:
            current_date = datetime.strptime(row[self.date_index], "%Y-%m-%d")
            year = current_date.year
            try:
                precipitation = float(row[self.prcp_index])
            except ValueError:
                print(f'Missing data for {current_date}')
            else:
                dates.append(current_date)
                precipitations.append(precipitation)
        if not dates:
            raise ValueError('No valid precipitation data found.')
        return dates, precipitations, year
        
        
    def plot_temperature(self, dates, year, highs, lows):
        plt.style.use('classic')
        fig, ax = plt.subplots() 
        ax.plot(dates, highs, c='red', alpha=0.5)
        ax.plot(dates, lows, c='blue', alpha=0.5)
        title = f'Annual high and low temperatures - {year}\n{self.place_name}'
        ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
        ax.set_ylabel('Temperature (F)', fontsize=16)
        ax.set_title(title, fontsize=20)
        ax.set_xlabel('', fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)
        fig.autofmt_xdate()
        plt.show()    
            
            
    def plot_precipitation(self, dates, year, precipitations):
        plt.style.use('classic')
        fig, ax = plt.subplots()
        ax.plot(dates, precipitations, c='blue')
        title = f'Annual precipitations - {year}\n{self.place_name}'
        ax.set_ylabel('Precipitations', fontsize=16)
        ax.set_title(title, fontsize=20)
        ax.set_xlabel('', fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)
        fig.autofmt_xdate()
        plt.show()
        
