from text_input import getCurrentDirectory

with open(getCurrentDirectory() + "/itsy-bitsy-spider.txt", "r") as file:
    print(file.read()) # reads all content
    print()

with open(getCurrentDirectory() + "/itsy-bitsy-spider.txt", "r") as file:
    print(file.readlines()) # reads each line into a list, with \n at the end
    print()

with open(getCurrentDirectory() + "/itsy-bitsy-spider.txt", "r") as file:
    print(file.readline()) # read a single line
    print()
