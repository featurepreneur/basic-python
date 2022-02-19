import json
from pprint import pprint

#Create
FILEPATH = 'city.json'

def get_json_data():

    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    return data

def store_json_data(data):

    with open(FILEPATH, 'w') as outfile:
        json.dump(data, outfile)

# CRUD: CREATE
def add_city(city, state):

    current_data = {
        "name"  : city,
        "state" : state 
    }

    data = get_json_data() 
        
    # print(data)

    data[city] = current_data
    store_json_data(data)

#Read all cities
def get_all_city():
    data = get_json_data()
    
    return data

#Read single cities
def get_single_city(city):

    data = get_json_data()

    if (city in data):
        return data[city]


def startpy():
    city="chennai"
    state = "Tamil nadu"
    add_city(city, state) 
    print("creating json")

    #CRUD READ 
    cities = get_all_city()
    pprint(cities)

    # CRUD: READ single
    city_name = 'Waterloo'
    single_city = get_single_city(city_name)
    print(single_city)
    
    

if __name__ == "__main__":
    startpy()