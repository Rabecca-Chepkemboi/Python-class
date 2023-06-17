def hello(*names):
    for name in names:
        print(f"hello{name}")
   

def sum(*numbers):
    answer = 0
    for number in numbers:
        answer += number
    return answer       

# write a function that accepts any number of integers an multiply all 
# of them and return the answer

def numbers(*numb):
    results = 1
    for nums in numb:
        results *= nums
    return results    


def student_attributes(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


def my_country(country = "burundi"):
    print(f"hello from{country}")