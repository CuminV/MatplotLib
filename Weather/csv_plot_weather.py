import sys

from tkinter import Tk, filedialog 
from weather import Weather


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

weather = Weather(filename)

if filename is None:
    print("File not selected")
    sys.exit()


while True:
    print('Enter "q" if you want to exit\n'
          'Please choise the type:\n'
          'Temperature = 1\nPrecipitation = 2')
    # Add "Another file = 3"
    question = input('')
    if question == '1':
        weather.high_and_low_temperature()
        weather.plot('temperature')
    elif question == '2':
        weather.get_precipitation()
        weather.plot('precipitation')
    elif question == 'q':
        break
    else:
        print('Only numbers!')
        continue


    
    