import csv
import os

def getCurrentDirectory():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    return current_directory

def process_file(path, fields):
    delim = get_delimiter(path)
    data = []
    path = getCurrentDirectory() + "/" + path
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=delim)
        for row in reader:
            record = []
            for field in fields:
                try:
                    record.append(row[field])
                except KeyError:
                    continue
            data.append(record)
    return data

def get_delimiter(path):
    file_extension = path[path.rfind('.') + 1:]
    return "," if file_extension == "csv" else "\t"

def write_file(path, fields, list):
    list_of_dictionaries = []
    for record in list:
        dictionary = dict(zip(fields, record))
        list_of_dictionaries.append(dictionary)
    delim = get_delimiter(path)
    path = getCurrentDirectory() + "/" + path
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, delimiter=delim, fieldnames=fields)
        writer.writeheader()
        writer.writerows(list_of_dictionaries)
        
if __name__ == "__main__":
    write_file("test.csv", ["Field 1", "Field 2"], [["Record 1a", "Record 1b"], ["Record 2a", "Record 2b"]])