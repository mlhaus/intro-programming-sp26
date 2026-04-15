import os, csv
from text_input import getCurrentDirectory

def get_delimiter(path):
    file_extension = path[path.rfind('.')+1:]
    if(file_extension == 'tsv'):
        delim = "\t"
    else:
        delim = ","
    return delim

FILENAME = getCurrentDirectory() + "/movies.tsv"

def csv_writer(path, list):
    delim = get_delimiter(path)
    with open(path, 'w', newline="") as file:
        writer = csv.writer(file, delimiter=delim)
        writer.writerows(list)

def csv_dict_writer(path, header, list):
    list_of_dicts = []
    for row in list:
        my_dict = dict(zip(header, row))
        list_of_dicts.append(my_dict)

    delim = get_delimiter(path)
    with open(path, 'w', newline='') as file:
        writer = csv.DictWriter(file, delimiter=delim, fieldnames=header)
        writer.writeheader()
        writer.writerows(list_of_dicts)

header = ['title', 'release_date']
movies = [
    ['Monty Python and the Holy Grail', '1975'],
    ['Cat on a Hot Tin Roof', '1958'],
    ['On the Waterfront', '1954'],
    ['Guardians of the Galaxy, Vol. 2', '2017'],
    ['Planes, Trains, and Automobiles', '1994']
]
# Use this function to generate the file without a header
csv_writer(FILENAME, movies)
# Use this function to generate the file with a header.
# csv_dict_writer(FILENAME, header, movies)