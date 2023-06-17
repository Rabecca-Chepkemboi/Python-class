def odd_numbers():
    x = range(20)
    for i in x:
        if i % 2 != 0:
            print(i)



def divisible_by_five():
    x = range(100)
    for i in x:
        if i % 5 == 0:
            print(f"{i}is divisible by 5")
        else:
            print(f"{i} is not divisible by 5")    



def multiple_comparison():
    x = range(30)
    for i in x:
        if i % 2 == 0:
            print(f"{i} is divisible by 2")
        elif i % 3 == 0:
            print(f"{i} is divisible by 3")    
        elif i % 5 == 0:
            print(f"{i} is divisible by 5")    
        else:
            print(f"{i} is not divisible by 2, 3, or 5")    



def divisible_by_two_and_three():
    x = range(30)
    for i in x:
        if i % 2 == 0 and i % 3 == 0:
            print(f"{i} is divisible by both 2 and 3")
        elif i % 2 == 0 or i % 3 == 0:
            print(f"{i} is divisible by either 2 and 3")
        else:
            print(f"{i} is not divisible by 2 or 3")  



def while_loop():
    x = 1
    while x < 10:
        print("Hello while")              



def break_statement():
    x = 1
    while x < 10:
        print("Hello there")
        x + 1
        if x == 5:
            break



def continue_statement():
    x = 0
    while x < 20:
        x += 1
        if x % 2 == 0:
            continue
        print(x)  