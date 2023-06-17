def hello(name):
    print(f"Hello{name}")


    #Write a Python program to count the number of items 
#in a dictionary that have a value greater than a certain number.
#9:29
#That's the python question

# def count_items(c: dict, value: int) -> int:
#     check = 0
#     for key in c:
#         if c[key] > value:
#             check += 1
#     return check

my_dict = {"apple": 5, "banana": 8, "orange": 3, "kiwi": 9, "grape": 2}
value = 4
count = len([x for x in my_dict.values() if x<value])
print(value)
# print(f"Number of items in the dictionary with a value greater than {value}: {count}")