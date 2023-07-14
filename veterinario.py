import core 
import os 
from datetime import datetime

"""
La información que se debe tener en cuenta para los veterinarios es la siguiente:
a. Id Veterinario
b. Nombres
c. Título profesional
d. Fecha de registro

2. Gestión de veterinarios:
• Agregar nuevos veterinarios con su información básica (nombre,
especialidad, número de teléfono, etc.).
• Buscar veterinarios por nombre o especialidad.
• Mostrar la información completa de un veterinario, incluyendo su
horario de trabajo.
"""

diccVeterinario = {"data":[]}

def loadInfoVeterinario():
    global diccVeterinario
    if(core.checkFile("veterinarios.json")):
        diccVeterinario = core.loadInfo("veterinarios.json")
    else:
        core.crearInfo("veterinarios.json",diccVeterinario)

def mainMenu():
    os.system("clear")
    isPacientRun = True
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','Gestion de veterinario',' '))
    print('+','-'*55,'+')
    print("1. Agregar veterinario")
    print("2. Buscar veterinario")
    print("3. Mostrar informacion de un veterinario")
    print("4. Volver al menu principal")

    op = int(input(": "))

    if op == 1:

        data = {
            "id": input("Ingrese el id del veterinario: "),
            "nombre": input("Ingrese el nombre del veterinario: "),
            "especialidad": input("Ingrese el titulo profesional del veterinario: "),
            "fecha": str(datetime.now())
        }

        diccVeterinario["data"].append(data)
        core.crearInfo("veterinarios.json",data)
    elif op == 2:
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE VETERINARIO',' '))
        print('+','-'*49,'+')
        print("1. Buscar por nombre")
        print("2. Buscar por especialidad")

        opcion = int(input(": "))

        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            print("Opcion no valida")
    elif op == 3:
        pass
    elif op == 4:
        isPacientRun = False
    if isPacientRun:
        mainMenu()