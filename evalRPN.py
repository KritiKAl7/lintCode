
from collections import deque

def evalRPN(tokens):
    oprands = ("+","-","*","/")
    numStack = deque()
    for i in tokens:
        print numStack
        if i in oprands:
            right = numStack.pop()
            left = numStack.pop()
            if i == "+":
                res = left + right
                print str(left) + i + str(right)
            elif i == "-":
                res = left - right
                print str(left) + i + str(right)
            elif i == "*":
                res = left * right
                print str(left) + i + str(right)
            elif i == "/":
                res = int(float(left) / right)
                print str(left) + i + str(right)
            numStack.append(res)
        else:
            numStack.append(int(i))
    return numStack[0]

print evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])