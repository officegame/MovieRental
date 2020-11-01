from os import system, name
import sys
import time

import customers.ui_customers as ui_customer
import movies.ui_movies as ui_movie
import rentals.ui_rentals as ui_rental

invalid_timer = 3
choice_messaging = "Enter your selection: "
choice_invalid_messaging = "Invalid selection"

def print_main_menu():
    print_header()
    print("1. Customer Management")
    print("2. Movie Management")
    print("3. Rentals")
    print("4. Exit")
    print()

def print_customer_management_menu():
    print_header()
    print("1. Add Customer")
    print("2. Edit Customer")
    print("3. Find Customer")
    print("4. Find Customers")
    print("5. Delete Customer")
    print("6. Back to main menu")
    print()

def print_movie_management_menu():
    print_header()
    print("1. Add Movie")
    print("2. Edit Movie")
    print("3. Find Movie")
    print("4. List All Movies")
    print("5. Delete Movie")
    print("6. Back to main menu")
    print()

def print_rentals_menu():
    print_header()
    print("1. Rent Movie")
    print("2. Return Movie")
    print("3. Back to main menu")
    print()

def print_header():
    clear()
    print("MovieRental")
    print("-----------")
    print()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    else: # posix
        _ = system('clear')

def run():
    while True:
        print_main_menu()
        try:
            main_menu_answer = int(input(choice_messaging))
        except:
            print(choice_invalid_messaging)
            time.sleep(invalid_timer)
            continue

        if main_menu_answer == 4:
            sys.exit()

        if main_menu_answer < 1 or main_menu_answer > 3:
            print(choice_invalid_messaging)
            time.sleep(invalid_timer)
            continue
        
        if main_menu_answer == 1:
            while True:
                print_customer_management_menu()
                try:
                    sub_menu_answer = int(input(choice_messaging))
                except:
                    print(choice_invalid_messaging)
                    time.sleep(invalid_timer)
                    continue

                if sub_menu_answer == 6:
                    break

                if sub_menu_answer < 1 or sub_menu_answer > 5:
                    print(choice_invalid_messaging)
                    time.sleep(invalid_timer)
                    continue

                if sub_menu_answer == 1:
                    ui_customer.call_add_customer()
                elif sub_menu_answer == 2:
                    ui_customer.call_edit_customer()
                elif sub_menu_answer == 3:
                    ui_customer.call_find_customer()
                elif sub_menu_answer == 4:
                    ui_customer.call_find_customers()
                elif sub_menu_answer == 5:
                    ui_customer.call_delete_customer()

        elif main_menu_answer == 2:
            while True:
                print_movie_management_menu()
                try:
                    sub_menu_answer = int(input(choice_messaging))
                except:
                    print(choice_invalid_messaging)
                    time.sleep(invalid_timer)
                    continue

                if sub_menu_answer == 6:
                    break

                if sub_menu_answer < 1 or sub_menu_answer > 5:
                    print(choice_invalid_messaging)
                    time.sleep(invalid_timer)
                    continue

                if sub_menu_answer == 1:
                    ui_movie.call_add_movie()
                elif sub_menu_answer == 2:
                    ui_movie.call_edit_movie()
                elif sub_menu_answer == 3:
                    ui_movie.call_find_movie()
                elif sub_menu_answer == 4:
                    ui_movie.call_find_movies()
                elif sub_menu_answer == 5:
                    ui_movie.call_delete_movie()

        elif main_menu_answer == 3:
            while True:
                print_rentals_menu()
                try:
                    sub_menu_answer = int(input(choice_messaging))
                except:
                    print(choice_invalid_messaging)
                    time.sleep(invalid_timer)
                    continue

                if sub_menu_answer == 3:
                    break

                if sub_menu_answer < 1 or sub_menu_answer > 2:
                    print(choice_invalid_messaging)
                    time.sleep(invalid_timer)
                    continue

                if sub_menu_answer == 1:
                    ui_rental.call_rent_movie()
                elif sub_menu_answer == 2:
                    ui_rental.call_return_movie()