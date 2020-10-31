import time
import ui.main as ui
import csv
from os import path
import re

def call_add_movie():
    ui.clear()
    print('Add Movie')
    print()
    movie_title = input("Movie Title: ")
    movie_release_date = input("Movie Release Date: ")
    rating = input("Rating: ")
    try:
        number_of_units = int( input ("How many do you have in stock?: "))
    except:
        print(ui.choice_invalid_messaging)
        time.sleep(ui.invalid_timer)

    fields = ['movie_title', 'movie_release_date', 'rating', 'number_of_units']
    rows = [[movie_title, movie_release_date, rating, number_of_units]]
    
    if path.isfile('data/movie.csv'):
        with open('data/movie.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if movie_title == row[0]:
                        print("Duplicate Movie Error")
                        time.sleep(ui.invalid_timer)
                        return
                    line_count += 1            

    with open("data/movie.csv", 'a') as csvfile:
       # creating a csv writer object  
       csvwriter = csv.writer(csvfile) 

       if csvfile.tell() == 0:
           # writing the fields  
           csvwriter.writerow(fields)

       # writing the data rows  
       csvwriter.writerows(rows)
    
    ui.clear()
    print("New movie added")
    time.sleep(ui.invalid_timer)
    

def call_edit_movie():
    ui.clear()
    print('Edit Movie')
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
        menu_selection = int(input('Select movie to edit: '))
    except:
        print(ui.choice_invalid_messaging)
        time.sleep(ui.invalid_timer)
        return

    movie_title = input("Movie Title: ")
    movie_release_date = input("Movie Release Date: ")
    rating = input("Rating: ")
    try:
        number_of_units = int( input ("How many do you have in stock?: "))
    except:
        print(ui.choice_invalid_messaging)
        time.sleep(ui.invalid_timer)

    fields = ['movie_title', 'movie_release_date', 'rating', 'number_of_units']
    movies[menu_selection -1] = [movie_title, movie_release_date, rating, number_of_units]
    
    with open("data/movie.csv", 'w+') as csvfile:
       # creating a csv writer object  
       csvwriter = csv.writer(csvfile) 

       if csvfile.tell() == 0:
           # writing the fields  
           csvwriter.writerow(fields)

       # writing the data rows  
       csvwriter.writerows(movies)

    ui.clear()
    print('Movie updated')
    time.sleep(ui.invalid_timer)

def call_find_movie():
    ui.clear()
    print('Find Movie')
    print()

    movie_title = input('Movie Title: ')

    if path.isfile('data/movie.csv'):
        with open('data/movie.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            found = False
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if row[0] == movie_title:
                        print()
                        print(line_count, end = '')
                        print(' ' + row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3])
                        print()
                        found = True
                        _ = input('Press enter to continue')
                    line_count += 1
    
    if found == False:
        print('Movie not found')
        time.sleep(ui.invalid_timer)

def call_find_movies():
    ui.clear()
    print('Find Movies')
    print()

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
                    line_count += 1
            print()
            _ = input('Press enter to continue')

def call_delete_movie():
    ui.clear()
    print('Delete Movie')
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
        menu_selection = int(input('Select movie to delete: '))
    except:
        print(ui.choice_invalid_messaging)
        time.sleep(ui.invalid_timer)
        return

    fields = ['movie_title', 'movie_release_date', 'rating', 'number_of_units']
    movies.pop(menu_selection - 1)

    with open("data/movie.csv", 'w+') as csvfile:
       # creating a csv writer object  
       csvwriter = csv.writer(csvfile) 

       if csvfile.tell() == 0:
           # writing the fields  
           csvwriter.writerow(fields)

       # writing the data rows  
       csvwriter.writerows(movies)

    ui.clear()
    print('Movie deleted')
    time.sleep(ui.invalid_timer)