def adding(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def division(x,y):
    return x / y

def multiplication(x,y):
    return x * y


print('1. adding')
print('2. subtraction')
print('3. division')
print('4. multiplication')
choose = int(input('choose operation (1/2/3/4): '))

num1 = float(input('enter the first number: '))
num2 = float(input('enter the second number: '))

if choose == 1:
    print('Selected adding')
    print(num1, '+', num2, '=', adding(num1, num2))
elif choose == 2:
    print('Selected subtraction')
    print(num1, '-', num2, '=', subtraction(num1, num2))
elif choose == 3:
    print('Selected division')
    print(num1, '/', num2, '=', division(num1, num2))
elif choose == 4:
    print('Selected multiplication')
    print(num1, '*', num2, '=', multiplication(num1, num2))
else:
    print('Incorrect choice')
