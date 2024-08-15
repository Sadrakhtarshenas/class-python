import math

print('Welcome To This Program:)')
print('1 BMI')
print('2 Calculator')


opreator = input('what i can do for you? ')

if (opreator == '1') or (opreator == 'BIM') or (opreator == 'bmi'):
    weight = float(input('enter your weight (KG): '))
    height = float(input('enter your height (CM): '))
    centimetre = height * height
    answer = weight / centimetre
    print(answer)

elif (opreator == '2') or (opreator == 'Calculator'):
    print('1 +')
    print('2 -')
    print('3 /')
    print('4 *')

opreator = input('enter the operation you want to perform:')
    
if (opreator == '1') or (opreator == '+'):
    num1 = float(input('please enter your first number: '))
    num2 = float(input('please enter your second: '))
    answer = num1 + num2
    print(answer)

if (opreator == '2') or (opreator == '-'):
    num1 = float(input('please enter your first number: '))
    num2 = float(input('please enter your second number: '))
    answer = num1 - num2
    print(answer)

if (opreator == '3') or (opreator == '/'):
    num1 = float(input('please enter your fisrt number: '))
    num2 = float(input('please neter your second number: '))
    answer = num1 / num2 
    print(answer)

if (opreator == '4') or (opreator == '*'):
    num1 = float(input('please enter your first number: '))
    num2 = float(input('please enter your second number: '))
    answer = num1 * num2
    print(answer)