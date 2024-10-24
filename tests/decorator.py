# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def say_hello():
#     print("Hello!")

# say_hello()

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase

#     return wrapper

# def say_hi():
#     return 'hello there'

# decorate = uppercase_decorator(say_hi)
# decorate()

def maximumCount(nums):
    negative = sum([1 if el < 0 else 0 for el in nums])
    positive = sum([1 if el > 0 else 0 for el in nums])
    print(f"There are {positive} positive integers and {negative} negative integers. The maximum count among them is {max(positive, negative)}.")

# maximumCount([-3,-2,-1,0,0,1,2])

table = {}
for num in tuple([1,2,1,3,2,5]):
    table[num] = table[num] + 1 if num in table else 1

print([el for el in table if table[el] == 1 ])
# print(result)