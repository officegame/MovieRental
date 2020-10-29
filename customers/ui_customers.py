from os import system
import time
import ui.main as ui
import csv
from os import path
import re

def call_add_customer():
    ui.clear()
    print('Add Customer')
    print()
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    email = input("Email: ")

    if not check_email(email):
        print('Invalid email')
        time.sleep(ui.invalid_timer)
        return

    fields = ['first_name', 'last_name', 'address', 'email']
    rows = [[first_name, last_name, address, email]]
    
    if path.isfile('data/customers.csv'):
        with open('data/customers.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if email == row[3]:
                        print("Duplicate Customer Error")
                        time.sleep(ui.invalid_timer)
                        return
                    line_count += 1

    with open("data/customers.csv", 'a') as csvfile:
       # creating a csv writer object  
       csvwriter = csv.writer(csvfile) 

       if csvfile.tell() == 0:
           # writing the fields  
           csvwriter.writerow(fields)

       # writing the data rows  
       csvwriter.writerows(rows)

    ui.clear()
    print("New customer added")
    time.sleep(ui.invalid_timer)


def call_edit_customer():
    pass

def call_find_customer():
    ui.clear()
    print('Find Customer')
    print()

    customer_email = input('Email: ')

    if path.isfile('data/customers.csv'):
        with open('data/customers.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            found = False
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if row[3] == customer_email:
                        print()
                        print(line_count, end = '')
                        print(' ' + row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3])
                        print()
                        found = True
                        _ = input('Press enter to continue')
                    line_count += 1
    
    if found == False:
        print('Customer not found')
        time.sleep(ui.invalid_timer)

def call_delete_customer():
    pass

def check_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        return True  
    else:  
        return False