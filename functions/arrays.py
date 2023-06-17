             #ARRAYS

#Write a Python program to find the second 
#largest element in an array of integers.
list1 = [10, 22, 14, 45, 50, 99]
 
# new_list is a set of list1
new_list = set(list1)
 
# Removing the largest element from temp list
new_list.remove(max(new_list))
 
# Elements in original list are not changed
# print(list1)
print(max(new_list))


#Write a Python program to reverse an array of integers.
#(using string slicing)
num = 2436458
print(str(num)[::-1])



lst = [10, 31, 22, 53, 14, 5]
lst.reverse()
print(lst)
 
# print("Using reversed() ", list(reversed(lst)))


#Write a Python program to remove duplicates from an array
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("original : "
      + str(test_list))
 
# using list comprehension
# to remove duplicated
# from list
res = []
[res.append(x) for x in test_list if x not in res]
 
# printing list after removal
print ("after removed : "
       + str(res))

# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# [x.append (a) for a in arry if a not in x]
# print(x)


#Write a Python program to find the first missing positive integer in an unsorted array.

def positive(arry):
    arry = list(set(arry))
    arry.sort()
    smallest = 1
    for i in arry:
        if i == smallest:
            smallest += 1
    return smallest
arry = [56, 67, 34, 23, 89, 12, 31]
print(positive(arry))




                #LIST

#Write a Python program to find the sum of all elements in a list.
#(using list comprehension)
list1 = [2, 15, 23, 10]
print(sum(list1))


#Write a Python program to sort a list of integers
#in ascending and descending order.
numbers = [11, 3, 7, 5, 2]

# sorting the list in ascending order
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


#Write a Python program to remove all odd numbers from a list.
# lists = [23, 12, 13, 54, 34, 22, 30]
# lis1 = []
# for x in lists
# if x % 2 == 0
# lists.append (x)
# print(lis1)


# Write a function that takes a list of numbers as input and 
# returns a new list with all duplicate numbers removed.
list1 = [2, 5, 7, 2, 6, 4, 5]    
def removeDups (num):
    return list(set(num))
print(removeDups(list1))