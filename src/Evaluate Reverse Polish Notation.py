__author__ = 'xuelu520'
#coding=utf-8

#Evaluate the value of an arithmetic expression in Reverse Polish Notation.

#Valid operators are +, -, *, /. Each operand may be an integer or another expression.

#Some examples:
#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

#注释待写。

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        res = 0
        ll = len(tokens)
        if ll == 1:return int(tokens[0])
        l = []
        for i in range(ll):
            x = tokens[i]
            if(x=="+" or x=="-" or x=="*" or x=="/"):
                aa = l[len(l)-1]
                del l[len(l)-1]
                bb = l[len(l)-1]
                del l[len(l)-1]
                res = cc(bb,aa,x)
                l.append(res)
            else:
                l.append(x)
        return res


def cc(x,y,z):
    a=int(x)
    b=int(y)
    c=z
    result = 0
    if c == "+":
        result = a+b
    elif c == "-":
        result = a-b
    elif c == "*":
        result = a*b
    elif c == "/":
        if abs(a) >= abs(b):
            result = ee(a,b)
    return result

def ee(a,b):
    if b == 0:return 0
    if a*b < 0:
        return -(abs(a)//abs(b))
    else:
        return a/b