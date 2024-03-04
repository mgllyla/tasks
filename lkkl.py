numb = int(input())
if numb > 0 and (numb % 2 == 0):
    print("Положительное четное число")
if numb > 0 and numb % 2 != 0:
    print("Полложительное нечетное число")
if numb == 0:
    print("Ноль")
elif (numb < 0) and (numb % 2 <= 0):
    print("Отрицательное четное число")
if numb < 0 and numb % 2 != 0:
    print("Отрицательноe нечетное число")
    
