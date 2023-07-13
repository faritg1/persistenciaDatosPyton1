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

for i,item in enumerate(especiesAnimales.values()):
    print(f'{i+1}. {item}')
