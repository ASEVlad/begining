#Роботишин mykola robotyshyn
#Квочкин kvochkin vlad
countt = 1
def indexing(f):
    def printing(self):
        global countt
        countt += 1
        print(f'this is {countt-1}')
        return f(self)
    return printing

class Ticket:
    count = 1
    def __init__(self, price):
        self.price = price
        self.id = Ticket.count
        Ticket.count += 1

class Student(Ticket):
    def __init__(self,price):
        self.price = price * 0.5
        self.id = Ticket.count
        Ticket.count += 1

    @indexing
    def prin(self):
        print('Price = {} Id = {}'.format(self.price,self.id))

class Advance(Ticket):

    def __init__(self, price):
        self.price = price  * 0.6
        self.id = Ticket.count
        Ticket.count += 1

    @indexing
    def prin(self):
        print('Price = {} Id = {}'.format(self.price, self.id))

class Late(Ticket):

    def __init__(self, price):
        self.price = price * 0.9
        self.id = Ticket.count
        Ticket.count += 1

    @indexing
    def prin(self):
        print('Price = {} Id = {}'.format(self.price, self.id))

def Generator():
    for i in range(10):
        yield f'event{i}'

event = []
x = Generator()
for i in x:
    event.append(i)
try:
    while True:
        if input('What event?') in event:
            ticket = input('What ticket?')
            if ticket == 'student':
                tickett = Student(100)
                tickett.prin()
            elif ticket == 'advance':
                tickett = Advance(100)
                tickett.prin()
            elif ticket == 'late':
                tickett = Late(100)
                tickett.prin()
            else: print('wrong ticket')
except:
    print('try again')