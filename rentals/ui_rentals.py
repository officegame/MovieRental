import time
import ui.main as ui
import csv
from os import path
import re
from datetime import datetime

def call_rent_movie():
    ui.clear()
    print('Movies To Rent')
    print()

    movies = []
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
                    movies.append(row)
                    line_count += 1
    
    print()
    try:
        movie_selection = int(input('Select movie to rent: '))
    except:
        print(ui.choice_invalid_messaging)
        time.sleep(ui.invalid_timer)
        return
    
    ui.clear()
    print('Who is renting this movie?')
    print()
    
    customers = []
    if path.isfile('data/customers.csv'):
        with open('data/customers.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    print(line_count, end = '')
                    print(' ' + row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3])
                    customers.append(row)
                    line_count += 1
    
    print()
    try:
        customer_selection = int(input('Select customer to rent to: '))
    except:
        print(ui.choice_invalid_messaging)
        time.sleep(ui.invalid_timer)
        return
    
    fields = ['movie_rented', 'customer_email', 'rented_on', 'returned_on']
    rows = [[movies[movie_selection - 1] [0], customers[customer_selection - 1] [3], datetime.now().strftime("%d/%m/%Y %H:%M:%S")]]

    if path.isfile('data/rentals.csv'):
        with open('data/rentals.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            rented = False
            
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if row[0] == movies[movie_selection -1][0] and row[1] == customers[customer_selection - 1][3] and len(row) > 2:
                        print('You already have this movie')
                        time.sleep(ui.invalid_timer)
                        return
                    line_count += 1
                
    if int(movies[movie_selection - 1][3]) < 1:
        print('We dont have that movie in stock')
        time.sleep(ui.invalid_timer)
        return
    else:
        movies[movie_selection -1][3] = str(int(movies[movie_selection -1][3]) - 1)
        
        fields = ['movie_title', 'movie_release_date', 'rating', 'number_of_units']
        
        with open("data/movie.csv", 'w+') as csvfile:
            # creating a csv writer object  
            csvwriter = csv.writer(csvfile) 

            if csvfile.tell() == 0:
                # writing the fields  
                csvwriter.writerow(fields)
                # writing the data rows  
                csvwriter.writerows(movies)

    with open("data/rentals.csv", 'a') as csvfile:
       # creating a csv writer object  
       csvwriter = csv.writer(csvfile) 

       if csvfile.tell() == 0:
           # writing the fields  
           csvwriter.writerow(fields)

       # writing the data rows  
       csvwriter.writerows(rows)

    ui.clear()
    print("Movie Rented")
    time.sleep(ui.invalid_timer)

    

def call_return_movie():
    pass

def call_list_rentals():
    ui.clear()
    print('All Rented Movies')
    print()

    if path.isfile('data/rentals.csv'):
        with open('data/rentals.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    print(line_count, end = '')
                    print(' ' + row[0])
                    line_count += 1
            print()
            _ = input('Press enter to continue')