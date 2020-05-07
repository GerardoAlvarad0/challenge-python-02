# Resolve the problem!!

# -*- coding: utf-8 -*-

import string
import random


SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
MINUSCULAS = list('abcdefghijklmnopqrstuvwxyz')
MAYUSCULAS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
NUMEROS = list('0123456789')
def generate_password():
    
    tam_pass = random.randint(8, 16)
    passwd = list()

    for i in range(tam_pass):
        select = random.randint(1, 4)
        if select == 1:
            rango = random.randint(0, 25)
            passwd.append(MINUSCULAS[rango])
        
        elif select == 2:
            rango = random.randint(0, 25)
            passwd.append(MAYUSCULAS[rango])
        
        elif select == 3:
            rango = random.randint(0, 9)
            passwd.append(NUMEROS[rango])
        
        else:
            rango = random.randint(0, 27)
            passwd.append(SYMBOLS[rango])
        
    print(passwd) #Imprime la constraseña
    password = " ".join(passwd) #Convirte la contraseña de lista a string
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False



def run():
    password = generate_password()
    
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
