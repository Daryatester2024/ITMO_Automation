num=5
if num >= 0:
    print ('число больше либо равно 0')
else:
    print('число отрицательное')

str_1= 'test'
srt_2= 'testing'


def task_yes_no (str_1, str_2):
    if str_2 in str_2:
        print('да')
    else:
        print('нет')
task_yes_no(str_1='test', str_2='testing')


num_float=77
if num_float>0:
    print('положительное число')
elif num_float==0:
    print('ноль')
else:
    print('отрицательное число')


permit_print= True
if num > 0 or permit_print:
    print('num-положительное число')
elif not permit_print:
    print('печать запрещена')


def student_status (num):
    if num==1 or num==2 or num==3 or num==4:
        print('бакалавр')
    elif num in range (5,7):
        print('магистр'),
    elif 7<=num<=9:
        print('аспирант')
    else:
        print('Введите корректный год обучения')
student_status(1)


num -35
if num>100 or num <-100:
    print('-')
else:
    print('+')