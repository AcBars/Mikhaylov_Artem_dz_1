# 2. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = str(input('Введите число n: '))
nn = n + n
nnn = nn + n
n = int(n)
nn = int(nn)
nnn = int(nnn)
print(n + nn + nnn)