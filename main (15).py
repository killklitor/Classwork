#coding uft-8
#Задание 7. 
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if a < b:
    print("Меньшее число:", a)
elif b < a:
    print("Меньшее число:", b)
else:
    print("Числа равны")

#Задание 8. 
km = float(input("Введите расстояние в километрах: "))
ft = float(input("Введите расстояние в футах: "))
m = ft * 0.45
if km > m:
    print("Большее расстояние в километрах:", km)
elif m > km:
    print("Большее расстояние в метрах:", m)
else:
    print("Расстояния равны")

#Задание 10.
a = float(input("введите 1 число:"))
b = float(input("введите 2 число:"))
c = a / b 
print (c)

#Задача 11
def compare_speed():
    a = float(input("Введите скорость в км/ч: "))    
    b = float(input("Введите скорость в м/сек: "))
    kmh_to_ms = a / 3.6
    if kmh_to_ms > b:
        print(f"Скорость в км/ч ({a}) больше скорости в м/сек ({b})")    
    elif kmh_to_ms < b:
        print(f"Скорость в м/сек ({b}) больше скорости в км/ч ({a})")
    else:
        print("Скорости равны")
compare_speed()
#Задача 12
radius = float(input("Введите радиус круга: "))
side = float(input("Введите сторону квадрата: "))
circle_area = 3.14159 * radius**2square_area = side**2
if circle_area > square_area:
    print("Площадь круга больше площади квадрата.")
elif circle_area < square_area:
    print("Площадь квадрата больше площади круга.")
else:
    print("Площади круга и квадрата равны.")