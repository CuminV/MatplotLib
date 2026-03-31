import sys

from tkinter import Tk, filedialog 
from weather import Weather

def main():
    root = Tk()

    root.withdraw()

    def choose_file():
        filename = filedialog.askopenfilename(
            title="Choose CSV file",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        
        if not filename:
            sys.exit()
        
        return filename

    def open_file():
        filename = choose_file()
        weather = Weather(filename)
        return weather


    weather = open_file()
    
    while True:
        print('Enter "q" if you want to exit\n'
            'Please choose the type:\n'
            'Temperature = 1\nPrecipitation = 2\nAnother file = 3')
        question = input('')
        if question == '1':
            dates, highs, lows, year = weather.get_temperature_data()
            weather.plot_temperature(dates, year, highs, lows)
        elif question == '2':
            dates, precipitations, year = weather.get_precipitation_data()
            weather.plot_precipitation(dates, year, precipitations)
        elif question == '3':
            weather = open_file()
        elif question == 'q':
            break
        else:
            print('Unknown command. Enter 1, 2, 3 or q.')
            continue
    

        
if __name__ == '__main__':
    main()