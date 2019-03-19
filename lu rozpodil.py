import numpy as np
import scipy.linalg as la
from fractions import Fraction

def nothing():
    global i, mas, answer
    # go in each row
    for n in range(i):
        # if element on diagonal = 0, we change find another row or colomn in matrix and swap them
        if mas[n][n] == 0:
            # check element in other rows шn this colomn on 0
            # go through each other row
            for l in range(n + 1, i):
                # if element not 0, we swap rows
                if mas[l][n] != 0:
                    mas[n], mas[l] = mas[l], mas[n]
                    break
            # if element on diagonal still 0, go throgh colomn and check element in this row on 0
            if mas[n][n] == 0:
                # go through each other colomn
                for l in range(n + 1, i):
                    # if element not 0, we swap colomn
                    if mas[n][l] != 0:
                        # swap colomn
                        for t in range(i):
                            mas[t][n], mas[t][l] = mas[t][l], mas[t][n]
                        break
        # if element on diagonal = 0 and the last number in this row is not 0, the decision is False.
        if (mas[n][n] == 0) and (mas[n][i] != 0):
            answer = False
            break
        # go throgh each colomn
        for m in range(i):
            # change all rows except n row
            if (m != n) and (mas[n][n] != 0):
                # coefficient for each row
                coef = mas[m][n] / mas[n][n]
                # change each element in row
                for k in range(n, i + 1):
                    mas[m][k] -= coef * mas[n][k]

def InputMatrix():
    i = int(input('enter \'i\''))
    #enter all row
    mas = [input('enter row') for n in range(i)]
    #split them on col
    for n in range(i):
        mas[n] = mas[n].split(' ')
    #change their type on integer
    for n in range(i):
        #go through row
        for m in range(i):
            #change each element in row
            mas[n][m] = Fraction(mas[n][m])
    return mas

def OutputAnswer(mas):
    for n in range(len(mas)):
        row = ""
        for k in range(len(mas[n])):
            row += ''.join(str(mas[n][k]).ljust(10))
        print(row)
#a = InputMatrix()#надо перевести в нп.еррей
a = np.array(InputMatrix())
(P, L, U) = la.lu(a)

print(P)
print(L)
print(U)

D = np.diag(np.diag(U)) # D is just the diagonal of U
U /= np.diag(U)[:, None] # Normalize rows of U
print(P.dot(L.dot(D.dot(U)))) # Check