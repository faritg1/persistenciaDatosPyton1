import core 
import os

diccPacient = {"data":[]}

def loadInfoPacient():
    global diccPacient
    if(core.checkFile("pacientes.json")):
        diccPacient = core.loadInfo("pacientes.json")
    else: 
        core.crearInfo("pacientes.json",diccPacient)

def mainMenu():
    os.system("clear")
    isPacientRun = True
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','Gestion de pacientes',' '))
    print('+','-'*55,'+')
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Mostrar informacion de un paciente")
    print("4. Volver al menu principal")

    op = int(input(": "))

    if(op == 1):
        num = 0
        if(len(diccPacient["data"]) >= 1):
            num = diccPacient["data"][-1]["id"] + 1
        else:
            num = 1
            
        nombrePaciente = input("Ingrese el nombre del paciente: ").lower()

        especiesAnimales = {
            "perro":["pitbull","pincher","bulldog","pastor aleman","rottweiler"],
            "gato":["persa","azul ruso","siames","angora turco","bengali"],
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

        elif especie == 2:
            tipo = list(especiesAnimales.keys())[1]
            for i, item in enumerate(especiesAnimales['gato']):
                print(f'{i+1}. {item}')
            raza = especiesAnimales['gato'][int(input(": "))-1]
        elif especie == 3:
            tipo = list(especiesAnimales.keys())[2]
            for i, item in enumerate(especiesAnimales['reptil']):
                print(f'{i+1}. {item}')
            raza = especiesAnimales['reptil'][int(input(": "))-1]
        elif especie == 4:
            tipo = list(especiesAnimales.keys())[3]
            for i, item in enumerate(especiesAnimales['ave']):
                print(f'{i+1}. {item}')
            raza = especiesAnimales['ave'][int(input(": "))-1]
        else:
            print("Opcion no valida")

        edad = int(input("Ingrese la edad del paciente: "))

        nombrePropietario = input("Ingrese el nombre del propietario:").lower()

        data = {
            "id":num,
            "nombre":nombrePaciente,
            "tipo":tipo,
            "raza":raza,
            "edad":edad,
            "propietario":nombrePropietario
        }

        diccPacient["data"].append(data)
        core.crearInfo("pacientes.json", data)

    elif(op == 2):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE PACIENTE',' '))
        print('+','-'*49,'+')
        print("1. Buscar por nombre")
        print("2. Buscar por tipo")
        print("3. Buscar por raza")

        opcion = int(input(": "))
        if(opcion == 1):
            pactSearch = input("Ingrese el nombre del paciente: ").lower()
            for i, item in enumerate(diccPacient["data"]):
                if pactSearch == item["nombre"]:
                    print(f'ID: {item["id"]}')
                    print(f'Paciente: {item["nombre"]}')
                    print(f'Tipo: {item["tipo"]}')
                    print(f'Raza: {item["raza"]}')
                    print(f'Edad: {item["edad"]}')
                    print(f'Propietario: {item["propietario"]}')
                    print(f'_______________________________')
                    input("")
        elif(opcion == 2):
            pactSearch = input("Ingrese el tipo del paciente: ").lower()
            for i, item in enumerate(diccPacient["data"]):
                if pactSearch == item["tipo"]:
                    print(f'ID: {item["id"]}')
                    print(f'Paciente: {item["nombre"]}')
                    print(f'Tipo: {item["tipo"]}')
                    print(f'Raza: {item["raza"]}')
                    print(f'Edad: {item["edad"]}')
                    print(f'Propietario: {item["propietario"]}')
                    print(f'_______________________________')
                    input("")
        elif(opcion == 3):
            pactSearch = input("Ingrese el raza del paciente: ").lower()
            for i, item in enumerate(diccPacient["data"]):
                if pactSearch == item["raza"]:
                    print(f'ID: {item["id"]}')
                    print(f'Paciente: {item["nombre"]}')
                    print(f'Tipo: {item["tipo"]}')
                    print(f'Raza: {item["raza"]}')
                    print(f'Edad: {item["edad"]}')
                    print(f'Propietario: {item["propietario"]}')
                    print(f'_______________________________')
                    input("")
        else:
            print("Opcion no valida")
    elif(op == 3):
        pass
    elif(op == 4):
        isPacientRun = False
    if(isPacientRun):
        mainMenu()





