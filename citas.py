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
    #os.system("clear")
    isCitaRun = True
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','Gestion de Citas',' '))
    print('+','-'*55,'+')
    print("1. Agregar Citas")
    print("2. Buscar Citas")
    print("3. Mostrar informacion de una cita")
    print("4. Volver al menu principal")

    op = int(input(": "))

    if op == 1:
        search = True
        if (len(diccCita['data'])) == 0:
            id = 1
        else:
            id = diccCita['data'][-1]['id'] + 1

        paciente = input('Ingrese nombre del paciente :').upper()
        for k in diccPacient['data']:
            if paciente == k['nombre']:
                idPac = k['id']
                especialista = input('Ingrese especialidad de la cita :').upper()
                while search:
                    for i,item in enumerate(diccVeterinario['data']):
                        if especialista == item['especialidad']:
                            vetSearch = item["nombre"]
                            print(f'Id veterinario : {item["id"]}\nNombre del especialista : {item["nombre"]}')     

                            agendar = True     
                            while agendar:
                                if len(item["agenda"]) == 0:
                                    now = datetime.now()
                                    newDate = now + timedelta(days=1)
                                    horaIni = datetime(now.year, now.month , newDate.day , 8, 00, 00, 00000)
                                    horaSal = datetime(now.year, now.month , newDate.day , 17, 00, 00, 00000)
                                    horaIniAlm = datetime(now.year, now.month , newDate.day , 11, 00, 00, 00000)
                                else:
                                    horaIni = datetime.strptime(item["agenda"][-1],'%Y-%m-%d %H:%M:%S')
                                    horaSal = datetime(horaIni.year, horaIni.month , horaIni.day , 17, 00, 00, 00000)
                                    horaIniAlm = datetime(horaIni.year, horaIni.month , horaIni.day , 11, 00, 00, 00000)
                                if horaIni < horaSal:
                                    if str(horaIni) in item["agenda"]:
                                        if horaIni == horaIniAlm:
                                            horaIni = horaIni + timedelta(hours=3)
                                            data ={
                                                "id": id,
                                                "fecha": str(horaIni),
                                                "nombreVet": vetSearch,
                                                "especialidad": especialista,
                                                "paciente": paciente,
                                                "idPac": idPac
                                                }

                                            item["agenda"].append(str(horaIni))
                                            core.editarDat("veterinarios.json",diccVeterinario)
                                            diccCita['data'].append(data)
                                            core.editarDat("citas.json",diccCita)
                                            agendar=bool(input("Pulse enter para continuar: "))
                                        else:
                                            horaIni = horaIni + timedelta(hours=1)
                                            data ={
                                                "id": id,
                                                "fecha": str(horaIni),
                                                "nombreVet": vetSearch,
                                                "especialidad": especialista,
                                                "paciente": paciente,
                                                "idPac": idPac
                                                }
                                            diccCita['data'].append(data)
                                            core.editarDat("citas.json",diccCita)
                                            item["agenda"].append(str(horaIni))
                                            core.editarDat("veterinarios.json",diccVeterinario)
                                            agendar=bool(input("Pulse enter para continuar: "))
                                    else:
                                        data ={
                                            "id": id,
                                            "fecha": str(horaIni),
                                            "nombreVet": vetSearch,
                                            "especialidad": especialista,
                                            "paciente": paciente,
                                            "idPac": idPac
                                            }
                                        diccCita['data'].append(data)
                                        core.editarDat("citas.json",diccCita)
                                        item["agenda"].append(str(horaIni))
                                        core.editarDat("veterinarios.json",diccVeterinario)
                                        agendar=bool(input("Pulse enter para continuar: "))
                                else:
                                    horaIni = horaIni + timedelta(days=1,hours=-9)
                                    horaSal = horaSal + timedelta(days=1)
                                    horaIniAlm = horaIniAlm + timedelta(days=1)
                                    data ={
                                        "id": id,
                                        "fecha": str(horaIni),
                                        "nombreVet": vetSearch,
                                        "especialidad": especialista,
                                        "paciente": paciente,
                                        "idPac": idPac
                                        }
                                    diccCita['data'].append(data)
                                    core.editarDat("citas.json",diccCita)
                                    item["agenda"].append(str(horaIni))
                                    core.editarDat("veterinarios.json",diccVeterinario)
                                    agendar=bool(input("Pulse enter para continuar: "))
                                print(f'La cita quedo agendada para {item["agenda"][-1]}')
                                agendar= False
                search=bool(input("Pulse enter para salir: "))
    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        isCitaRun = False
    if isCitaRun:
        mainMenu()