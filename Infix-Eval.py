from pythonds.basic.stack import Stack

global operandstack
global stackofoperates

operandstack = Stack()
stackofoperates = Stack()


def isnum(n):
    counter = 0
    for i in n:
        if i in '0123456789.':
            counter += 1
    if counter == len(n):
        return True
    else:
        return False


def emptystacks():
    while not operandstack.isEmpty():
        operandstack.pop()
    while not stackofoperates.isEmpty():
        stackofoperates.pop()


def cal(Op):
    num1 = operandstack.pop()
    num2 = operandstack.pop()

    if Op == "+":
        return float(num2) + float(num1)
    elif Op == "-":
        return float(num2) - float(num1)
    elif Op == "*":
        return float(num2) * float(num1)
    elif Op == "/":
        return float(num2) / float(num1)
    else:
        return float(num2) ** float(num1)


def orderinfix():
    print('pls enter your infix operation separated by spaces : ', end='')

    calculation = input().split()

    priority = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    for token in calculation:

        if isnum(token):
            operandstack.push(token)

        elif token == "(":
            stackofoperates.push(token)

        elif token == ")":
            operation = stackofoperates.pop()
            while operation != "(":
                operandstack.push(cal(operation))
                operation = stackofoperates.pop()

        else:
            while (not stackofoperates.isEmpty()) and (priority[stackofoperates.peek()] >= priority[token]):
                operandstack.push(cal(stackofoperates.pop()))

            stackofoperates.push(token)

    while not stackofoperates.isEmpty():
        operandstack.push(cal(stackofoperates.pop()))

    print("Result : ", end='')
    print(operandstack.pop())

try:
    orderinfix()
except ZeroDivisionError:
    print('Divide by Zero is not Accepted .. Try again')
    emptystacks()
    orderinfix()
except:
    print('invalid input pls try again')
    emptystacks()
    orderinfix()


