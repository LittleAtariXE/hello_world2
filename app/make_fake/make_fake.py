import os
from random import choice, randint


lib_path = os.path.dirname(os.path.abspath(__file__)) + '/library'

def load_text(file_name):
    output = set()
    with open(f'{lib_path}/{file_name}', 'r') as f:
        for line in f.readlines():
            output.add(line.rstrip('\n'))

    return list(output)

def correct_date(date):
    if int(date) < 10:
        new = f'0{date}'
    else:
        new = str(date)
    return new

def generate_date_birth(birth):
    if birth == '':
        birth = 'xx.xx.xxxx'
    base = birth.split('.')
    day, month, year = base[0], base[1], base[2]
    if day.lower() == 'xx':
        day = randint(1, 30)

    if month.lower() == 'xx':
        month = randint(1, 12)

    if int(day) > 27:
        while int(month) == 2:
            month = randint(1, 12)
    if year.lower() == 'xxxx':
        year = randint(1963, 1999)
    return [correct_date(day), correct_date(month), str(year)]

def generate_pesel(birth, sex):
    first = f'{birth[2][2:4]}{birth[1]}{birth[0]}'

    fate = randint(1, 4)
    if fate == 2:
        x1 = '1'
    else:
        x1 = '0'
    x2 = str(randint(0, 7))
    x3 = str(randint(0, 9))
    x4 = randint(0, 8)

    if sex == 'men' and x4 % 2 == 0:
        x4 += 1
    elif sex != 'men' and x4 % 2 != 0:
        x4 += 1
    x4 = str(x4)
    second = x1 + x2 + x3 + x4

    pesel = list(first + second)
    hash = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    new = []
    for x in range(0, 10):
        rec = hash[x] * int(pesel[x])
        if rec > 9:
            rec = rec % 10
        new.append(rec)

    suma = 0
    for x in new:
        suma += x

    if suma > 9:
        suma = suma % 10
        if suma == 0:
            suma = 0
        else:
            suma = 10 - suma
    pesel = first + second + str(suma)
    return pesel

def generate_email(imie, nazw, rok, domena_email):

    znaki = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ś': 's', 'ż': 'z', 'ź': 'z'}
    imie = imie.lower()
    nazw = nazw.lower()

    for k, i in znaki.items():
        imie = imie.replace(k, i)
        nazw = nazw.replace(k, i)



    limie = len(imie)
    lnazw = len(nazw)
    t1 = f'{imie}{nazw[0:4]}{rok}'
    t2 = f'{rok[2:4]}{imie}{rok[2:4]}'
    t3 = f'{nazw}{imie}'
    t4 = f'{imie[0:limie-2]}{nazw[0:lnazw-2]}{rok[2:4]}'
    t5 = f'{nazw[0:int(lnazw/2)]}{nazw[0:int(lnazw/2)]}{randint(1, 9)}'
    t6 = f'{imie[0:int(limie/2)]}{imie[0:int(limie/2)]}{rok[2:4]}'
    templates = [t1, t2, t3, t4, t5, t6]
    first = choice(templates)
    return first + '@' + domena_email

class FakeLibrary:
    def __init__(self, plec='men'):
        if plec == 'men':
            self.im_men = load_text('im_men.txt')
            self.naz_men = load_text('naz_men.txt')
        self.domeny = load_text('domeny.txt')

class MakeFake(FakeLibrary):
    def __init__(self, plec='men', imie='', nazw='', data_ur='', email=''):
        self.plec = plec

        if self.plec == 'men':
            super().__init__(plec='men')

            if imie == '':
                self.imie = choice(self.im_men)
            else:
                self.imie = imie

            if nazw == '':
                self.nazw = choice(self.naz_men)
            else:
                self.nazw = nazw

            self.data_ur = generate_date_birth(data_ur)
            self.pesel = generate_pesel(self.data_ur, self.plec)
            if email == '':
                self.email = generate_email(self.imie, self.nazw, self.data_ur[2], choice(self.domeny))
            else:
                self.email = email

    def data_UR(self):
        new = ".".join(self.data_ur)
        return new

##### TEST


