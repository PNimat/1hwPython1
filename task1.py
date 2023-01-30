"""
Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

# Первый вариант решения
import copy

n = int(input('Введите трехзначное число '))
while n < 100 or n > 999:
    n = int(input('Введите трехзначное число '))

n_copy = copy.copy(n)
count = 0

while n_copy > 0:  # Считаю скольео цифр в числе
    n_copy = n_copy // 10
    count += 1

sum_of = 0
for _ in range(count):
    result = n % 10
    n = n // 10
    sum_of += result
print(f'Сумма чисел в числе = {sum_of}')

# Второй вариант решения

n = input('Введите трехзначное число ')
sum_of = 0

for i in n:
    sum_of += int(i)
print(f'Сумма чисел в числе = {sum_of}')




