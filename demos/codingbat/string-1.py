# left2
def left2(str):
  first2 = str[:2] # grabs the first two characters
  secondHalf = str[2:] # grabs everything starting at index 2
  return secondHalf + first2 

#non_start
def non_start(a, b):
  return a[1:] + b[1:]

#combo_string
def combo_string(a, b):
  shortest = a if(len(a) < len(b)) else b
  longest = a if(len(a) > len(b)) else b
  return shortest + longest + shortest
  
