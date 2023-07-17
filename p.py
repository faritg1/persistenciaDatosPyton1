""" horarioDiurno = {
    "lunes":[6,7,8,9,10,11,12,13,14,15,16,17,18],
    "martes":[6,7,8,9,10,11,12,13,14,15,16,17,18],
    "miercoles":[6,7,8,9,10,11,12,13,14,15,16,17,18],
    "jueves":[6,7,8,9,10,11,12,13,14,15,16,17,18],
    "viernes":[6,7,8,9,10,11,12,13,14,15,16,17,18]
}

horarioNocturno = {
    "lunes":[12,13,14,15,16,17,18,19,20,21,22,23,24],
    "martes":[12,13,14,15,16,17,18,19,20,21,22,23,24],
    "miercoles":[12,13,14,15,16,17,18,19,20,21,22,23,24],
    "jueves":[12,13,14,15,16,17,18,19,20,21,22,23,24],
    "viernes":[12,13,14,15,16,17,18,19,20,21,22,23,24]
}

especiesAnimales = {
    "perro":["pitbull","pincher","bulldog","pastor aleman","rottweiler"],
    "gato":["Persa","Azul ruso","siames","Angora turco","bengali"],
    "reptil":["camaleon","caiman","tortuga","iguana","lagarto"],
    "ave":["gallinas","pavos","gansos","palomas","loros"]
}

for i,item in enumerate(especiesAnimales.keys()): # keys, items, values
    print(f'{i+1}. {item}')

especie = int(input(": "))

if especie == 1:
    tipo = list(especiesAnimales.keys())[0]
    for i, item in enumerate(especiesAnimales['perro']):
        print(f'{i+1}. {item}')
    raza = especiesAnimales['perro'][int(input(": "))-1]
    print(tipo,raza) """
    
