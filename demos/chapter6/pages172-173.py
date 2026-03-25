def add_one(num: int) -> int:
    return num + 1
# int objects are immutable, meaning the original variable will not be changed
# if the variable is passed to a function. Other immutable types are str, float, bool
x = 0 
print(add_one(x)) # 1
print(x) # 0


def add_one_to_list(nums: list) -> list:
    nums.append(1)
    return nums
# list objects are mutable, meaning the original value will be changed
# if the variable is passed to a function
y = []
print(add_one_to_list(y)) # [1]
print(y) # [1]