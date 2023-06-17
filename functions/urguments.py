# A function named concatenate_args that takes any number of string arguments
# in positional arguments format and concatenates them into a single string

def concatenate_args(*myarry):
    empty_string=(" ")
    for names in myarry:
        empty_string += names
    return empty_string          


# A function named concatenate_kwargs that takes any number of string arguments 
# in keyword arguments  format and concatenates them into a single string

def concatenate_kwargs(**arry):
    str=""
    for key,value in arry.items():
        str +=(f"{key},{value}, ")
    return str