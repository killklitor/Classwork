#coding: utf-8
#задание 1 
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
if a > b:
    maximus = a
    minimus = b
else:
    maximus = b
    minimus = a
print("Максимум", maximus)
print("Минимум", minimus)      
#Задание 2
a = int(input("Введите сторону квадрата"))
b = int(input("Введите радиус круга"))
if 2*b <= a:
    print("Круг впишется в квадрат")
else:
    print("Круг не впишется в квадрат")
#Задание 3
a = int(input("Введите число"))
if a > 0:
    b = 1/a*a 
else:
    b = a*a 
print (b)
#Задание 4
a = int(input("Введите сторону квадрата"))
b = int(input("Введите радиус круга"))
if b * 2 => a:
    print('квадрат впишется в круг')
else:
     print('квадрат не впишется в круг')
#задача 5
a = int(input("Введите первое вещественное число"))
a = int(input("Введите второе вещественное число"))
if a > b:
    print("первое вещественное число больше второго")
else:
     print("второе вещественное число больше второго")