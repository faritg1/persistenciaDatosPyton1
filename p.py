# especiesAnimales = [
#     {
#         "perro":["pitbull","pincher","bulldog","pastor aleman","rottweiler"]
#     },
#     {
#         "gato":["Persa","Azul ruso","siames","Angora turco","bengali"],
#     },
#     {
#         "reptil":["camaleon","caiman","tortuga","iguana","lagarto"],
#     },
#     {
#         "ave":["gallinas","pavos","gansos","palomas","loros"]
#     }
# ]

# for i, item in keys(especiesAnimales):
#     print(i)
#     print(item)


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
    print(tipo,raza)
    
# elif especie == 2:
#     print("GATO")
#     for i,item in enumerate(especiesAnimales.values()):
#         print(f'{i+1}. {item}')
#     raza = int(input(": "))
#     especieRaza = "gatos"
# elif especie == 3:
#     print("reptil")
#     for i,item in enumerate(especiesAnimales.values()):
#         print(f'{i+1}. {item}')
#     raza = int(input(": "))
#     especieRaza = "reptil"
# elif especie == 4:
#     print("ave")
#     for i,item in enumerate(especiesAnimales.values()):
#         print(f'{i+1}. {item}')
#     raza = int(input(": "))
#     especieRaza = "ave"
