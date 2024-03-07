#Задача 6. 
#N = int(input("Введите число N: "))
#i = 0

#while i < N:
    #print(i)
    #i += 1

#Задача 7.
a = float(input("Введите вещественное число a: "))
n = 1
s = 0

while s <= a:
    s += 1 / n
    n += 1
    print(n)
    
#Задание 8.
n = int(input("Введите число n: "))
i = 1

while i * i <= n:
    i += 1

print(i)