# Task_1
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:

# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

duration = float(input('Введите продолчительность периода в секундах: '))
res = ' '
if duration >= 86400:
    days = duration // 86400
    days = str(days)
    res = days + ' дней '
    duration = duration % 86400
if duration >= 3600:
    hours = duration // 3600
    hours = str(hours)
    res = res + hours + ' часов '
    duration = duration % 3600
if duration >= 60:
    minuts = duration // 60
    minuts = str(minuts)
    res = res + minuts + 'минут'
    duration = duration % 60
if:
    duration = str(duration)
    res = res + duration + 'секунд'
print(res)

