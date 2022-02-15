import json

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

def startpy():
    city="hyderabad"
    state = "telengana"
    add_city(city, state) 
    print("creating json")

if __name__ == "__main__":
    startpy()