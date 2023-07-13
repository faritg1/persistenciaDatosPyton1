import core 
import os

diccPacient = {"data":[]}

def loadInfoPacient():
    global diccPacient
    if(core.checkFile("pacientes.json")):
        diccPacient = core.loadInfo("pacientes.json")
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','Gestion de pacientes',' '))
    print('+','-'*55,'+')

    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Mostrar informacion de un paciente")
    print("4. Volver al menu principal")

    op = int(input(": "))

    if(op == 1):
        pass
    num = 0

    if(len(diccPacient["data"]) >= 1):
        num = len(diccPacient["data"][-1]["id"]) + 1
    else:
        num = 1




