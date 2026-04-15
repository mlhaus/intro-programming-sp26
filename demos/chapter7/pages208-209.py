from text_input import getCurrentDirectory
import re # for regular expressions

# https://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string
def remove_non_alphabetic_chars(str):
    # A regular expression (regex) is a sequence of characters that define a search pattern.
    regex = re.compile('[^\\w-]+') # matches any non-word char except a - (dash/hyphen  )
    return regex.sub('', str) # this code will remove spaces, commas, and other punctuation

# https://stackoverflow.com/questions/20577840/python-dictionary-sorting-in-descending-order-based-on-values
# The book talks about dictionaries in chapter 12
def sort_reverse(dict):
    # The book talks about sorted on page 185
    # This code will display the words shown the most first
    return sorted(wordCount, key=wordCount.get, reverse=True)

# This will constain all of the words in the story
words = []
with open(getCurrentDirectory() + "/green-eggs-and-ham.txt") as file:
    # words = file.readlines() # I don't want \n characters
    # Loop through all lines in the file, stopping at the end
    while(line := file.readline()) != "":
        # First, it removes spaces and \n
        # Second, it splits each line into its own array
        # Use concatenation instead of append
        words += line.strip().split()

# Dictionaries are covered in Chapter 12
wordCount = {} # {"green":15,"eggs":10}
for word in words:
    cleanWord = remove_non_alphabetic_chars(word).lower()
    if(cleanWord not in wordCount):
        wordCount[cleanWord] = 1
    else:
        wordCount[cleanWord] += 1
# print(wordCount) # Shows the unsorted dictionary
print(f"There are {len(wordCount)} unique words in the story 'Green Eggs and Ham'") # Shows how many unique words there are in the story
sorted_wordCountdict = sort_reverse(wordCount)
for key in sorted_wordCountdict:
    print(f"The word '{key}' appears {wordCount[key]} times.")