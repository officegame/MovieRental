from os import system
import time
import ui.main as ui
import csv
from os import path

def call_add_customer():
    ui.clear()
    print('Add Customer')
    print()
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    email = input("Email: ")

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
    pass

def call_delete_customer():
    pass