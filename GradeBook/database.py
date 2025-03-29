import json


def load_data():
    try:
        with open('students.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    return data


def save_data(data):
    with open('students.json', 'w') as file:
        json.dump(data, file, indent=4)




