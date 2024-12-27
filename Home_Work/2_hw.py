def task_1 (user:str, age:int, weight:float, mylist:list, address:bool) -> int:
    return (type(user), type(age), type(weight), type(mylist), type(address))
print(task_1('darya', 15, 45.5, [1, 2], 10>9))

def task_2 (a:list)->int:
    return (a[0:3])
print(task_2([1,2,3,5,8,13,21]))

def task_3 (x:int)->int:
    return (x*x)
print(task_3(4))