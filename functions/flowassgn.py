# 1. Write a function that uses while, if and continue statements to 
#print all the even numbers between 0 and 50. 

def print_even():
    nums = 0
    while nums <= 50:
        if nums % 2 != 0:
            nums += 1
            continue
        print(nums)
        nums += 2


# 2. Write a function that takes an integer argument and prints "Prime" 
#if the number is prime, and "Not prime" if the number is not prime.

def check_prime():
    x = range(50)
    for i in x:
        if i <= 1:
            print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")


# 3. Write a function that takes a list of integers as input and prints
#the sum of all the even numbers in the list.

def sum_even_numbers():
    x = range(100)
    sums = 0
    for num in x:
        if num % 2 == 0:
            sums += num
    print(sums)


# 4. Write a function that takes any two integers as input, and prints the sum of
#all the numbers between the two integers (inclusive) that are divisible by 3.

def divisible_three(start, end):
    
    total = 0
    for num in range(30, 100+1):
        if num % 3 == 0:
            total += num
    print( start, end, total)