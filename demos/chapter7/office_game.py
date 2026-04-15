import os, csv, random
from text_input import getCurrentDirectory

INPUT_FILENAME = getCurrentDirectory() + "/The Office cast.csv"
OUTPUT_FILENAME = getCurrentDirectory() + "/highest_score.txt"

def process_csv_dict_reader(path, fields):
    delim = get_delimiter(path)
    data = []
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=delim)
        for row in reader:
            record = []
            for field in fields:
                record.append(row[field])
            data.append(record)
    return data

def get_delimiter(path):
    file_extension = path[path.rfind('.')+1:]
    if(file_extension == 'tsv'):
        delim = "\t"
    else:
        delim = ","
    return delim

def get_game_data():
    needed_fields = ['Name', 'Description']
    data = process_csv_dict_reader(INPUT_FILENAME, needed_fields)
    return data

def ask_question(character):
    prompt = f"What character id {character[0]} play? "
    user_guess = input(prompt).strip()
    correct_answer = character[1]
    if(user_guess.lower() == correct_answer.lower()):
        print("That's correct")
        return 1
    else:
        print(f"Incorrect. It was {correct_answer}.")
        return 0
    
def update_high_score(score):
    with open(OUTPUT_FILENAME, 'w') as file:
        file.write(str(score))
    print("Congratuations, you beat the highest score!")
    
def check_highest_score(score):
    with open(OUTPUT_FILENAME, 'r') as file:
        highest_score = int(file.read())
        if(score > highest_score):
            update_high_score(score)

def play_game():
    data = get_game_data()
    score = 0
    count = 0
    while(len(data) > 0):
        rand_char = random.randint(0, len(data) - 1)
        character = data.pop(rand_char)
        score += ask_question(character)
        count += 1
    print(f"Game over. Your final score was {score} out of {count}.")
    check_highest_score(score)

play_game()