'''
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''
num = input('Введите число: ')
sum = 0
j = 0
newlist = []
for i in num:
       newlist.append(i)
while j < len(newlist):
    sum = sum + int(newlist[j])
    j = j + 1
print(f"Сумма цифр {num} равна {sum}")