import functions

print("Hello World")

first = 5 #int(input("Введите первое целое число: "))
second = 10 #int(input("Введите второе целое число: "))
opr = "div" #input("Введите операцию: ")

rez, firstFromFunc, secondFromFunc = functions.operation(first, second, opr)
print("Ответ: ", rez, ".С числами ", firstFromFunc, " и ", secondFromFunc)

spis = [0,3,5,6,8,9,0,2]#input().split()
newSpis = []
rezult = functions.evenNumbers(spis, newSpis)
print("Список четных чисел: ", rezult)