import copy
from fractions import Fraction
def OutputAnswer(answer,mas,i):
    def MultipleAnswer(n, row, i):
        # create string in which we will write an answer
        str_answer = 'x{}'.format(n + 1)
        # go through each element
        for k in range(n + 1, i):
            # if element is above 0 add him
            if row[k] < 0:
                str_answer += '{}x{}'.format(row[k], k + 1)
            # if element is upper then 0 add him
            elif row[k] > 0:
                str_answer += '+{}x{}'.format(row[k], k + 1)
        # end the creation of an answer
        str_answer += '={}'.format(row[-1])
        return (str_answer)

    # if answer is True, we print the answer
    if answer:
        # go through each element on diagonal
        for n in range(i):
            # check row on multiple answer
            check = 0
            for k in range(i):
                if mas[n][k] != 0: check += 1
            # if answer is not multiple print Xi and its value
            if check == 1:
                print('x{} = {}'.format(n + 1,mas[n][-1] / mas[n][n]))
            # if answer multiple create answer and print it
            elif check > 1:
                print(MultipleAnswer(n, mas[n], i))
            # if row don't have any not 0 element, print, that this variable can be any value in R
            else:
                print('x{} = R'.format(n + 1))
    # if answer is False, print '-1'
    else:
        print('-1')

def OutputAnswerMas(mas,i):
    for n in range(i):
        row = ""
        for k in range(i+1):
            row += ''.join(str(mas[n][k]).ljust(10))
        print(row)
    print()

def CreateDiagonalMatrixGause():
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
        OutputAnswerMas(mas, i)

def InputMatrix():
    i = int(input('enter \'i\''))
    #enter all row
    mas = [input('enter row') for n in range(i)]
    #split them on col
    for n in range(i):
        mas[n] = mas[n].split(' ')
    #change their type on fraction
    for n in range(i):
        #go through row
        for m in range(i + 1):
            #change each element in row
            if m == i:
                mas[n][m] = Fraction(int(mas[n][m])/100*99)
            else:
                mas[n][m] = Fraction(mas[n][m])
    return mas, i

def VectorNev(mas, i):
    if print_result:
        A = mas[:, :-1]
        b = mas[:, -1]
        print(np.dot(A, x) - b)

def CreateMatrix(mas, i):
    for n in range(i):
        if mas[n][n] != 1:
            if mas[n][i] != 0:
                coef = mas[n][i]
            # change each element in row
            for k in range(n, i + 1):
                mas[n][k] /= coef
    return mas

answer = True
mas, i = InputMatrix()
mascopy = copy.deepcopy(mas)
CreateDiagonalMatrixGause()
mas = CreateMatrix(mas, i)
try:
    OutputAnswerMas(mas,i)
except:
    pass
OutputAnswer(answer, mas, i)
'''2 0 3 1 20
-4 3 -4 -2 -34
4 7 9 1 48
5 7 0 8 97'''

'''
-7 -6 -6 6 144
7 6 8 -13 -170
4 17 -16 10 21
-5 18 19 0 -445'''
'''
-2 4 7 42
-7 -6 -6 7
11 -2 -8 -91


2 5 4 1 20
1 3 2 1 11
2 10 9 7 40
3 8 9 2 37
'''
