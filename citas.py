import os
import core 
from datetime import datetime
from datetime import timedelta

diccCita = {"data":[]}
diccPacient = {"data":[]}
diccVeterinario = {"data":[]}

def loadInfoCitas():
    global diccCita
    global diccPacient
    global diccVeterinario
    if(core.checkFile("citas.json")):
        diccCita = core.loadInfo("citas.json")
        diccPacient = core.loadInfo("pacientes.json")
        diccVeterinario = core.loadInfo("veterinarios.json")
    else:
        core.crearInfo("citas.json",diccCita)

def mainMenu():
    os.system("clear")
    isCitaRun = True
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','Gestion de Citas',' '))
    print('+','-'*55,'+')
    print("1. Agregar Citas")
    print("2. Buscar Citas")
    print("3. Mostrar informacion de un Citas")
    print("4. Volver al menu principal")

    op = int(input(": "))

    now = datetime.now()
    newDate = now + timedelta(days=1)
    horaIni = datetime(now.year,now.month,newDate.day,8,00,00,0000)
    horaSal = datetime(now.year,now.month,newDate.day,18,00,00,0000)
    
    if op == 1:
        nombrePaciente = input("Ingrese el nombre del paciente: ").lower()
        nombreVete = input("Ingrese el nombre del veterinario: ").lower()

        for i,item in enumerate(diccVeterinario["data"]):
            if nombreVete == item["nombre"]:
                print(f'id veterinario: {item["id"]}')
                print(f'citas: {item["hora"]}')
                if horaIni < horaSal:
                    if(str(horaIni) in item["hora"]):
                        horaIni = horaIni + timedelta(hours=1)
                        item["hora"].append(str(horaIni))
                        core.editarDat("veterinarios.json",diccVeterinario)
                    else:
                        item["hora"].append(str(horaIni))
                        core.editarDat("veterinarios.json",diccVeterinario)
    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        isCitaRun = False
    if isCitaRun:
        mainMenu()