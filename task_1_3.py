# 3. Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной
# строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

n = 1
while n < 21:
    if n == 1:
        n = str(n)
        print(n + ' процент')
    elif n < 5:
        n = str(n)
        print(n + ' процента')
    else:
        n = str(n)
        print(n + ' процентов')
    n = int(n)
    n = n + 1
while n <= 100:
    excess = n % 10
    if excess == 1:
        n = str(n)
        print(n + ' процент')
    elif excess < 5 and excess != 0:
        n = str(n)
        print(n + ' процента')
    else:
        n = str(n)
        print(n + ' процентов')
    n = int(n)
    n = n + 1
