import datetime

def greeting(name):
    hourOfDay = datetime.datetime.now().hour
    result = "Good "
    if(hourOfDay >= 5 and hourOfDay < 12):
        result += "morning"
    elif(hourOfDay >= 12 and hourOfDay < 17):
        result += "afternoon"
    elif(hourOfDay >= 17 and hourOfDay < 22):
        result += "evening"
    elif(hourOfDay >= 22 and hourOfDay < 24 or hourOfDay >= 0 and hourOfDay < 5):
        result += "night"
    else:
        result += "day"
    print(result + ", " + name + "!")

greeting("Marc")
greeting("Amy")
greeting("John")