from input import input
from test import test_input
import numpy as np

print('Initiate Day 9 script')
#TODO: Solve
operations = input.split('\n')
test_operations = test_input.split('\n')

def move_head(letter):
    if(letter == 'U'):
        return ["y", 1]
    elif(letter == 'D'):
        return ["y", -1]
    elif(letter == 'L'):
        return ["x", -1]
    elif(letter == 'R'):
        return ["x", 1]


def main():
    hx = 0
    hy = 0
    tx = 0
    ty = 0

    xy = ["0-0"]
    for operation in test_operations:
        operation = operation.split()
        for i in range(int(operation[1])):
            move = move_head(operation[0])
            if(move[0] == "x"):
                hx += move[1]
            else:
                hy += move[1]
            try:
                tx += int((hx - tx) / abs(hx - tx)) or 0
            except:
                tx += 0
            try:
                ty += int((hy - ty) / abs(hy - ty)) or 0
            except:
                ty += 0
            if(str(tx) + '-' + str(ty) not in xy):
                print(tx, ty)
                xy.append(str(tx) + '-' + str(ty))

    print(xy)
    print(len(xy))
main()
