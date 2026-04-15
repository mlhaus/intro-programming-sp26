from text_input import getCurrentDirectory

# Calling "w" will create a brand new file each time.
# WARNING: If the file already exists, all previous data will be lost
with open(getCurrentDirectory() + "/haiku.txt", "w") as file:
    file.write("Pressure builds and grows!") # 5 syllables
    file.write("\nStudy sessions, late nights spent!") # 7 syllables
    file.write("\nHope for passing grades!") # 5 syllables
    file.write("\n\n")

# Calling "a" will append content to the end of the file
# This will not delete previous data
# Both "w" and "a" will create a file if it doesn't exist.
with open(getCurrentDirectory() + "/haiku2.txt", "a") as file:
    file.write("Steadfast through the storm,")
    file.write("\nUnwavering, spirit strong,")
    file.write("\nSuccess blooms at last.")
    file.write("\n\n")