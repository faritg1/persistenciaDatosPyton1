import os 

if __name__ == "__main__":
    isActivate = True
    op=0
    while isActivate:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^24}|".format(' ','ADMINISTRACION DEL CENTRO VETERINARIO',' '))
        print('+','-'*55,'+')
        print("1. Gestion de pacientes")
        print("2. Gestion de veterinarios")
        print("3. Gestion de citas medicas")
        print("4. Terminar programa")
        op = int(input("Ingrese una opcion: "))

        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            isActivate = False
        else:
            print("Opcion no valida")
            input("")
