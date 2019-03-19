import time
from math import log,exp,sqrt

def generator(n, minim=0, maxim=1):
    '''генрирует n чисел от minim(минимум) до maxim(максимум)'''
    global seed
    #параметры Парка-Миллера
    a = 65539
    m = 2 ** 31
    result_mas = []
    #генерация псевдослучайных величин
    for i in range(n):
        next = a * seed % m
        result_mas.append(((next / m) * (maxim - minim) + minim))
        seed = next
    if n == 1:#если число одно, выводим число а не массив
        return result_mas[0]
    else:
        return result_mas

def normal(n,mu,sigma):
    '''генерация случайных чисел с нормальным распредилением
    n - количество чисел'''
    result=[]
    while len(result)<n:
        u = generator(1)
        x = generator(1, mu - 6 * sigma, mu + 6 * sigma)
        if u < exp((-(x - mu) ** 2) / (2 * (sigma ** 2))):
            result.append(x//1)
    return result

def eksp(mas, n, lambd):
    #квантильное преобразование в експонинциальное расапредиление
    result = []
    for i in range(n):
        result.append((log(mas[i]/lambd) * -1)//0.2)
    return result

class Bandit:
    def __init__(self, raspred):
        '''n - количество чисел в массиве
        money - кол денег на каждом бандите
        mu - мат ожидание
        sigma - разброс
        labmd - ламбда для експонинциального рапредиления
        values - числа в массиве'''
        self.n = 500
        self.money = 1000
        self.mu = generator(1,0,10)//1
        self.sigma = generator(1,0,2)//0.1*10
        self.lambd = generator(1,0.1)//0.1
        if raspred == 1:
            self.values = eksp(generator(self.n,0,self.mu),self.n,self.lambd)
        else:
            self.values = normal(self.n,self.mu,self.sigma)

    def roll_bandit(self, i):
        '''крутим бандита
        выбираем 2 числа из массива(numbers_of_bandit) и сравниваем их,
        если 2 числа одинаковые - умножаем число на 10(это и будет наше вознаграждение)'''
        numbers_of_bandit = []
        for k in range(2):
            numbers_of_bandit.append(self.values[i * 2 + k])
        if (numbers_of_bandit[0] == numbers_of_bandit[1]):
            reward = int(numbers_of_bandit[0]) * 20
        else:
            reward = 0
        return reward

def metod1(bandit1,bandit2,bandit3):
    '''крутим 100 раз каждый из бандитов, и по количество заработаных денег выбираем лучшего'''
    for i in range(100):
        bandit1.money += bandit1.roll_bandit(i) - 3
        bandit2.money += bandit2.roll_bandit(i) - 3
        bandit3.money += bandit3.roll_bandit(i) - 3
    print(bandit1.money,bandit2.money,bandit3.money)
    if (bandit1.money > bandit2.money) and (bandit1.money > bandit3.money):
        print('bandit1 is the best')
    elif bandit2.money > bandit3.money:
        print('bandit2 is the best')
    else:
        print('bandit3 is the best')

def metod2(bandit1,bandit2,bandit3):
    '''Прошу прощения за этот ужасный код,
    result1,result2,result3 - награды каждого бандита при каждом прокруте
    umbers_of_roll - количество прокрутов каждого бандита
    probability - верхняя граница каждого бандита'''
    def srednee(mas):
        '''средний выигрышь какого нибудь бандита'''
        sum = 0
        for i in mas:
            sum += i
        return sum / len(mas)
    '''крутим по одному разу каждого бандита, и меняем все переменные'''
    result1 = [bandit1.roll_bandit(0)]
    result2 = [bandit2.roll_bandit(0)]
    result3 = [bandit3.roll_bandit(0)]
    number_of_roll1 = 1
    number_of_roll2 = 1
    number_of_roll3 = 1
    probability1 = result1[0] + sqrt(2 * log(3))
    probability2 = result2[0] + sqrt(2 * log(3))
    probability3 = result2[0] + sqrt(2 * log(3))
    '''крутим еще 245  меняем переменные
    тут можно было проверять просто на больше меньше, но мне показалось, 
    что в каких то случаях эта стратегия может потребовать больше проверок'''
    for i in range(2,248):
        if (probability1 == probability2) and (probability2 == probability3):
            result1.append(bandit1.roll_bandit(number_of_roll1))
            number_of_roll1 += 1
            probability1 = srednee(result1) + sqrt(2 * log(i+3) / number_of_roll1)
            bandit1.money += bandit1.roll_bandit(number_of_roll1) - 3

            result2.append(bandit2.roll_bandit(number_of_roll1))
            number_of_roll2 += 1
            probability2 = srednee(result2) + sqrt(2 * log(i+3) / number_of_roll2)
            bandit2.money += bandit2.roll_bandit(number_of_roll1) - 3

            result3.append(bandit3.roll_bandit(number_of_roll1))
            number_of_roll3 += 1
            probability3 = srednee(result3) + sqrt(2 * log(i+3) / number_of_roll3)
            bandit3.money += bandit3.roll_bandit(number_of_roll1) - 3
        elif (probability1 == probability2) and (probability1 > probability3):
            result1.append(bandit1.roll_bandit(number_of_roll1))
            number_of_roll1 += 1
            probability1 = srednee(result1) + sqrt(2 * log(i+2) / number_of_roll1)
            bandit1.money += bandit1.roll_bandit(number_of_roll1) - 3

            result2.append(bandit2.roll_bandit(number_of_roll1))
            number_of_roll2 += 1
            probability2 = srednee(result2) + sqrt(2 * log(+3) / number_of_roll2)
            bandit2.money += bandit2.roll_bandit(number_of_roll1) - 3
        elif (probability1 == probability3) and (probability1 > probability2):
            result1.append(bandit1.roll_bandit(number_of_roll1))
            number_of_roll1 += 1
            probability1 = srednee(result1) + sqrt(2 * log(i+2) / number_of_roll1)
            bandit1.money += bandit1.roll_bandit(number_of_roll1) - 3

            result3.append(bandit3.roll_bandit(number_of_roll1))
            number_of_roll3 += 1
            probability3 = srednee(result3) + sqrt(2 * log(+2) / number_of_roll3)
            bandit3.money += bandit3.roll_bandit(number_of_roll1) - 3
        elif (probability2 == probability3) and (probability2 > probability1):
            result2.append(bandit2.roll_bandit(number_of_roll1))
            number_of_roll2 += 1
            probability2 = srednee(result2) + sqrt(2 * log(i+2) / number_of_roll2)
            bandit2.money += bandit2.roll_bandit(number_of_roll1) - 3

            result3.append(bandit3.roll_bandit(number_of_roll1))
            number_of_roll3 += 1
            probability3 = srednee(result3) + sqrt(2 * log(i+2) / number_of_roll3)
            bandit3.money += bandit3.roll_bandit(number_of_roll1) - 3
        elif (probability1 > probability2) and (probability1 > probability3):
            result1.append(bandit1.roll_bandit(number_of_roll1))
            number_of_roll1 += 1
            probability1 = srednee(result1) + sqrt(2 * log(i+1) / number_of_roll1)
            bandit1.money += bandit1.roll_bandit(number_of_roll1) - 3
        elif (probability2 > probability3) and (probability2 > probability1):
            result2.append(bandit2.roll_bandit(number_of_roll1))
            number_of_roll2 += 1
            probability2 = srednee(result2) + sqrt(2 * log(i+1) / number_of_roll2)
            bandit2.money += bandit2.roll_bandit(number_of_roll1) - 3
        elif (probability3 > probability1) and (probability3 > probability2):
            result3.append(bandit3.roll_bandit(number_of_roll1))
            number_of_roll3 += 1
            probability3 = srednee(result3) + sqrt(2 * log(i+1) / number_of_roll3)
            bandit3.money += bandit3.roll_bandit(number_of_roll1) - 3
    #вывод ответа
    if (number_of_roll1 > number_of_roll2) and (number_of_roll1 > number_of_roll3):
        print('bandit1 is the best')
    elif number_of_roll2 > number_of_roll3:
        print('bandit2 is the best')
    else:
        print('bandit3 is the best')
    print(bandit1.money, bandit2.money, bandit3.money)

def metod3():
    #выбираем случайным образом бандита и говорим что он лучший :)
    x = generator(1,1,4)//1
    # вывод ответа
    if x == 1:
        print('bandit1 is the best')
    elif x == 2:
        print('bandit2 is the best')
    else:
        print('bandit3 is the best')


seed = time.time()%1*100000 #первоначальное значения для псевдогенерации случайнх чисел
bandit1 = Bandit(generator(1,1,4)//1)
bandit2 = Bandit(generator(1,1,4)//1)
bandit3 = Bandit(generator(1,1,4)//1)
metod1(bandit1,bandit2,bandit3)
metod2(bandit1,bandit2,bandit3)
metod3()