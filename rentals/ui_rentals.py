import time
import ui.main as ui
import csv
from os import path
import re

def call_rent_movie():
    ui.clear()
    print('Which Movie would you like to see')
    print()

    rentals = []
    if path.isfile('data/movie.csv'):
        with open('data/movie.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    print(line_count, end = '')
                    print(' ' + row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3])
                    rentals.append(row)
                    line_count += 1

    print()
    try:
        menu_selection = int(input('Select the movie you would like to rent: '))
    except:
        print(ui.choice_invalid_messaging)
        time.sleep(ui.invalid_timer)
        return

def call_return_movie():
    pass