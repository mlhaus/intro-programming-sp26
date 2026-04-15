# no_teen_sum
def fix_teen(n):
  if(13 <= n < 15 or 16 < n <= 19):
    return 0
  return n
  
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

#lone_sum
def lone_sum(a, b, c):
  if(a == b and b == c):
    return 0
  if(a == b):
    a, b = 0, 0
  if(a == c):
    a, c = 0, 0
  if(b == c):
    b, c = 0, 0
  return a + b + c
  
def lone_sum(a, b, c):
  sum = 0
  if(a != b and a != c):
    sum += a
  if(b != a and b != c):
    sum += b
  if(c != a and c != b):
    sum += c
  return sum
