from itertools import count


def greater_num(num_1, num_2):
    if num_1>num_2:
        print(num_1)
    elif num_2>num_1:
        print(num_2)
greater_num(13,42)


def num_differ(a, b):
    if a>b==135 or b>a==135:
        print('yes')
    else:
        print('no')
num_differ(270,135)


def seasons_year (month):
    if month ==1 or month==2 or month== 12:
        print('зима')
    elif month in range(3,6):
        print('весна')
    elif month in range(6,9):
        print('лето')
    elif month in range(9,12):
        print('осень')
    else:
        print('введите числа от 1 до 12')
seasons_year(9)


def arbitrary_num (a,b,c):
    if a>10 and b>10 and c>10:
        print('yes')
    else:
        print('no')
arbitrary_num(111,222,222)


def list_numbers (my_list:list)->int:
    result=0
    for elem in my_list:
        result=result+elem
    return result
print(list_numbers([1,2,3,-4,5]))


def day_in_month (year:int, month:int):
    print(month*29 + year*12*29)
day_in_month(1,1)
