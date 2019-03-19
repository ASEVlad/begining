from fractions import Fraction
import copy
def OutputAnswer(mas,i):
    for n in range(i):
        row = ""
        for k in range(i):
            row += ''.join(str(mas[n][k]).ljust(10))
        print(row)

def CreateInverseMatrixGause(mas, i):
    def Determinant(mas, i):
        deter = 1
        for n in range(i):
            deter *= mas[n][n]
        return deter != 0

    def CreateUnitMatrix(mas, i):
        for n in range(i):
            if mas[n][n] != 1:
                coef = mas[n][n]
                # change each element in row
                for k in range(n, i * 2):
                    mas[n][k] /= coef
        for n in range(i):
            mas[n] = mas[n][i:i*2]
        return mas

    # add row for inverse matrix
    for n in range(i):
        for k in range(i):
            mas[n].append(int(n == k))
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
            # if element on diagonal still 0, go through each colomn and check element in this row on 0
            if mas[n][n] == 0:
                # go through each other colomn
                for l in range(n + 1, i):
                    # if element not 0, we swap colomn
                    if mas[n][l] != 0:
                        # swap colomn
                        for t in range(i):
                            mas[t][n], mas[t][l] = mas[t][l], mas[t][n]
                            mas[t][i + n], mas[t][i + l] = mas[t][i + l], mas[t][i + n]
                        break
        # go throgh each colomn
        for m in range(i):
            # change all rows except n row
            if (m != n) and (mas[n][n] != 0):
                # coefficient for each row
                coef = mas[m][n] / mas[n][n]
                # change each element in row
                for k in range(n, i * 2):
                    mas[m][k] -= coef * mas[n][k]
    if Determinant(mas, i):
        return CreateUnitMatrix(mas, i)
    else:
        return None

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
    return mas, i

def NormaMatrix(mas, i):
    maxx = []
    sum = 0
    for n in range(i):
        for i in mas[n]:
            sum += i
        maxx.append(sum)
        sum = 0
    return max(maxx)



answer = True
mas, i = InputMatrix()
inversemas = []
mascopy = copy.deepcopy(mas)

try:
    inversemas = CreateInverseMatrixGause(mas, i)
    OutputAnswer(inversemas, i)
    print(NormaMatrix(inversemas, i) * NormaMatrix(mascopy, i))
except:
    print('inverse matrix does not exist, because determinant is 0')

'''2 0 3 1
-4 3 -4 -2
4 7 9 1
5 7 0 8'''

'''
-7 -6 -6 6 144
7 6 8 -13 -170
4 17 -16 10 21
-5 18 19 0 -445'''
'''
-2 4 7 42
-7 -6 -6 7
11 -2 -8 -91'''
