import random

def gen_sum(dicc, cant = 1): #Dos argumentos: el diccionario al que se agregarán, y cuántos problemas generará (1 por defecto)
    for x in range(cant):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        dicc[f"{a} + {b}"] = a + b  #Ej: {'2 + 7': 9}


def gen_res(dicc, cant = 1): #Dos argumentos: el diccionario al que se agregarán, y cuántos problemas generará (1 por defecto)
    for x in range(cant):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        dicc[f"{max(a,b)} - {min(a,b)}"] = max(a,b) - min(a,b) #Ej: {'7 - 2': 5}

def gen_mul(dicc, cant = 1): #Dos argumentos: el diccionario al que se agregarán, y cuántos problemas generará (1 por defecto)
    for x in range(cant):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        dicc[f"{a} * {b}"] = a * b #Ej: {'7 * 2': 14}

def gen_div(dicc, cant = 1): #Dos argumentos: el diccionario al que se agregarán, y cuántos problemas generará (1 por defecto)
    x = 1
    while cant >= x:
        a = random.randint(1, 10)
        b = random.randint(2, 10)
        if a % b == 0 and f"{a} / {b}" not in dicc.keys(): 
            dicc[f"{a} / {b}"] = int(a / b) #Ej: {'8 / 2': 4}
            x += 1

#Pruebas:   
'''
dics, dicr, dicm, dicd = {}, {}, {}, {}

gen_sum(dics, 10)
gen_res(dicr, 10)
gen_mul(dicm, 10)
gen_div(dicd, 10)

print(dics)
print(dicr)
print(dicm)
print(dicd)
'''