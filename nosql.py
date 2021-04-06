import pymongo
from pymongo import MongoClient
from datetime import date

cluster = MongoClient("mongodb+srv://user1:paulius123@cluster0.lvsgw.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["FirstDB"]

ownership = db["ownership"]

def operation() :
    print("TO ADD NEW CUSTOMER - 1 "
                   "\nTO ADD NEW CAR - 2"
                   "\nTO ADD OWNER FOR CAR - 3"
                   "\nTO EXIT - 4")
    
    choice = input()
    return int(choice)

def add_customer() :
    customer = db["customer"]
    name = input("NAME : ")
    surname = input("SURNAME : ")
    birth = input("DATE OF BIRTH (xxxx-xx-xx) : ")
    sex = input("SEX : ")
    country = input("COUNTRY : ")
    city = input("CITY : ")
    adress = input("ADRESS : ")
    doc = {
        '_id' : name,
        'First Name' : name,
        'Surname' : surname,
        'Date of birth' : birth,
        'Sex' : sex,
        'Location' : {
            'Country': country,
            'City' : city,
            'Adress' : adress,
        }
    }
    customer.insert_one(doc)
    
def add_cars() : 
    cars = db["cars"]
    make = input("MAKE : ")
    model = input("MODEL : ")
    year = input("YEAR (xxxx-xx-xx) : ")
    color = input("COLOR : ")
    engine = input("ENGINE : ")
    FT = input("FUEL TYPE : ")
    GB = input("GEAR BOX : ")
    doc = {
        "Make" : make,
        "Model" : model,
        "Year" : year,
        "Color" : color, 
        "Engine" : engine,
        "Fuel type" : FT,
        "Gear box" : GB,
    }
    car_id = cars._id
    cars.insert_one(doc)

def add_owner() : 
    customer_id = input("WHICH CUSTOMER : ")
    
    car_id = input("WHICH CAR : ")
    doc = {
        "customer_id" : customer_id,
        "car_id" : car_id,
    }
    ownership.insert_one(doc)
    
while True : 
    choice = operation()
    if choice == 1 :
        customer = add_customer()
    if choice == 2 :
        cars = add_cars()
    if choice == 3 : 
        ownership = add_owner()
    if choice == 4 :
        break