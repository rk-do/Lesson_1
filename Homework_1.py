print("Задание 1".upper())
a = 5
b = 10
print (a + b)
user = int(input("Введите первое число: "))
user_1 = int(input("Введите второе число: "))
print(int(user + user_1))

print("Задание 2".upper())
time = int(input("Введите время в секундах: "))
hour = int(time/3600)
min = int(time/60%60)
sec = int(time/1%60)
print("{}:{}:{}".format(hour, min, sec))

print("Задание 3".upper())
name = int(input("Введите число: "))
num_1 = str(name)
num_2 = num_1 + num_1
num_3 = num_1 + num_1 + num_1
comp = name + int(num_2) + int(num_3)
print("Результат равен: ", comp)

print("Задание 4".upper())
user_2 = int(input("Введите целое число: "))
r = -1
while user_2 > 0:
    d = user_2 % 10
    if d > r:
       r = d
    user_2 = user_2//10
print(r)

print("Задание 5".upper())
val = int(input("Каково значение выручки фирмы: "))
cos = int(input("Каково значение издержек фирмы: "))
if val > cos:
    print("Фирма работает с прибылью")
else:
    print("Фирма работает с убытком")
rent = val/cos
print("Рентабельность составляет: ", rent)
number_of_people = int(input("Введите количество работников фирмы: "))
cost_of_people = rent/number_of_people
print("Прибыль фирмы в рассчете на одного работника составляет: ", cost_of_people)

print("Задание 6".upper())
x = int(input("Пробежал в первый день: "))
y = int(input("Пробежал в завершающий день: "))
day = 0
while y - x > 0:
    x = x + (x * 0.1)
    day += 1
print(day)

