import random # Agafem un numero random

def missatge(habitacio, llums): #Creem una funcio per als missatges 
    print(f"room {habitacio} : LLums {llums} correctly") # Agafem les dues variables per als missatges
    print(f"All the rooms {llums} correctly")

def opcionsllums(): #Creem una funcio al menu
    print("1 Sel·lecciona la habitació :")
    print("2 Sel·lecciona totes les habitacions :")
    print("3 Show the real state of the lights :")
    print("4 Exit :")

def llums():
    llums = False
    opcionsllums()
    opcio = int(input("Sel·lecciona quina opcio vols 1-4 :")) #Preguntem al usuari
    match opcio: #Comprobem l'opció del usuari
        case 1: #Si es l'opció 1 farà això
            habitacio = input("Introdueix la habitació ")
            manual = input("turn on or turn off: (on/off)")
            if manual == "on":
                print("Manual encesa")
                llums = True #Configurem les llums etc
                missatge(habitacio, llums)
            else:
                print("Manual no engegada")
            missatge(habitacio, llums)

        case 2:
            manual = input("turn on or turn off: (on/off)")
            if manual == "on":
                print("Manual encesa")
                llums = True
                missatge(habitacio, llums)
            else:
                print("Manual no engegada")
            missatge(habitacio, llums)

        case 3:
            if llums == True:
                print("LLums encesas")
                missatge(habitacio, llums)
            else:
                print("LLums no encesas")
            missatge(habitacio, llums)

        case 4: #Sortim
            print("Sortint")
            return
        case _:
            opcionsllums()

llums()

def missatge(min_temp, max_temp, temp_actual, calefactor):
    print(f"Límit mínim: {min_temp} °C  |  Límit màxim: {max_temp} °C")
    print(f"Temperatura actual: {temp_actual} °C")
    print(f"Calefactor: {'ACTIVAT' if calefactor else 'APAGAT'}")
    print("-" * 40)

def mostrar_menu():
    print("1 Configurar límits de temperatura")
    print("2 Veure estat actual")
    print("3 Sortir")

def control_temperatura():
    minim = None
    maxim = None
    temps = random.randint(10,30)
    calefactor = False

    while True:
        mostrar_menu()
        opcio = int(input("Selecciona una opció (1-3): "))

        match opcio:
            case 1:
                minim = float(input("Introdueix Temperatura MÍNIMA (°C): "))
                maxim = float(input("Introdueix Temperatura MÀXIMA (°C): "))
                print("Límits guardats.\n")

            case 2:
                while minim is None or maxim is None:
                    try:
                        minim = int(input("Introdueix el mínim: "))
                        maxim = int(input("Introdueix el màxim: "))
                        if minim >= maxim:
                            print("El mínim ha de ser més petit que el màxim.\n")
                            minim = maxim = None
                    except ValueError:
                        print("Has d'introduir números!\n")
                        minim = maxim = None

                temps = float(input("Introdueix temperatura ACTUAL (°C): "))

                if temps < minim:
                    calefactor = True
                elif temps >= maxim:
                    calefactor = False

                missatge(minim, maxim, temps, calefactor)

            case 3:
                print("Sortint")
                return

            case _:
                print("Opció no vàlida, prova de nou.\n")

control_temperatura()

def missarge(limit, co2_actual, alarma):
    print(f"Límit de CO₂ establert: {limit} ppm")
    print(f"Nivell actual de CO₂: {co2_actual} ppm")
    print(f"Alarma: {'ACTIVADA' if alarma else 'DESACTIVADA'}")

def menu_alarma():
    print("1 Configurar límit de CO₂")
    print("2 Veure estat actual")
    print("3 Sortir")

def alarma():
    limit = None
    alarma = False

    while True:
        menu_alarma()
        opcio = int(input("Selecciona una opció (1-3): "))

        match opcio:
            case 1:
                limit = float(input("Introdueix el límit MÀXIM de CO₂ (ppm): "))
                print("Límit guardat.\n")

            case 2:
                if limit is None:
                    print("Primer has de configurar el límit!\n")
                    continue

                co2_actual = float(input("Introdueix el nivell ACTUAL de CO₂ (ppm): "))

                if co2_actual > limit:
                    alarma = True
                else:
                    alarma = False

                missarge(limit, co2_actual, alarma)

            case 3:
                print("Sortint")
                return

            case _:
                print("Opció no vàlida, prova de nou.\n")

alarma()

