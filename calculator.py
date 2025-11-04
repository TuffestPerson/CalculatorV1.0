import math

def pluseke(x, y):
    return x + y

def minuseke(x, y):
    return x - y

def ymnojenie(x, y):
    return x * y

def delenie(x, y):
    if y == 0:
        return "net"
    return x / y

def stepen(x, y):
    return x ** y

def sqrtt(x):
    if x < 0:
        return "НЕТ"
    return math.sqrt(x)

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Выход")

    choice = input("Введите номер операции: ")

    if choice in ('1', '2', '3', '4', '5'): 
        try:                                
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Пожалуйста, введите ЧИСЛА.") 
            continue
        if  choice == '1':
            print(num1, "+", num2, "=", pluseke(num1, num2)) 
        elif choice == "2":
            print(num1, "-", num2, "=", minuseke(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", ymnojenie(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", delenie(num1, num2))
        elif choice == '5':
            print(num1, "^", num2, "=", stepen(num1, num2))

    elif choice == '6':
        try:
            num = float(input("Введите число: "))
        except ValueError:
            print("chislo nado")
            continue
        print("Квадратный корень из", num, "=", sqrtt(num))

    elif choice == '7':
        break
    else:
        print("НеT")
