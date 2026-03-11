# front3
def front3(str):
  front = str[:3]
  return front * 3

# front_back
def front_back(str):
  # return the unmodified string if it has 0 or 1 characters
  if(len(str) <= 1):
    return str
  first_char = str[0] # the first character is at index 0
  middle = str[1:-1] # All characters between index 1 and the last character
  last_char = str[-1] # the last character is at index -1 (or len(str)-1)
  return last_char + middle + first_char


# missing_char
def missing_char(str, n):
  first_part = str[:n] # Give me the first n characters
  second_part = str[n + 1:] # Give me all remaining characters after n
  return first_part + second_part

# not_string
def not_string(str):
  if(str[:3] == "not"):
    return str
  return "not " + str
