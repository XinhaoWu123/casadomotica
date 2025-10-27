import random

def menu_principal():
    while True:
        print("1. Control de llums")
        print("2. Control de temperatura")
        print("3. Alarma de CO₂")
        print("4. Sortir del programa")
        opcio: int = int(input("Tria una opció (1-4): "))

        match opcio:
            case 1:
                llums()
            case 2:
                control_temperatura()
            case 3:
                alarma()
            case 4:
                print("Fins aviat!")
                break
            case _:
                print("Opció no vàlida, prova de nou.")

# Ejecutamos el menú principal
menu_principal()
def missatge(habitacio: str, llums: bool):
    print(f"room {habitacio} : LLums {llums} correctly")
    print(f"All the rooms {llums} correctly")

def opcionsllums():
    print("1 Sel·lecciona la habitació :")
    print("2 Sel·lecciona totes les habitacions :")
    print("3 Show the real state of the lights :")
    print("4 Exit :")

def llums():
    llums: bool = False
    opcionsllums()
    opcio: int = int(input("Sel·lecciona quina opcio vols 1-4 :"))

    match opcio:
        case 1:
            habitacio: str = input("Introdueix la habitació ")
            manual: str = input("turn on or turn off: (on/off)")
            if manual == "on":
                print("Manual encesa")
                llums = True
                missatge(habitacio, llums)
            else:
                print("Manual no engegada")
            missatge(habitacio, llums)

        case 2:
            manual: str = input("turn on or turn off: (on/off)")
            if manual == "on":
                print("Manual encesa")
                llums = True
                missatge(habitacio, llums)
            else:
                print("Manual no engegada")
            missatge(habitacio, llums)

        case 3:
            if llums:
                print("LLums encesas")
                missatge(habitacio, llums)
            else:
                print("LLums no encesas")
            missatge(habitacio, llums)

        case 4:
            print("Sortint")
            return
        case _:
            opcionsllums()

llums()

def missatge(min_temp: float, max_temp: float, temp_actual: float, calefactor: bool):
    print(f"Límit mínim: {min_temp} °C  |  Límit màxim: {max_temp} °C")
    print(f"Temperatura actual: {temp_actual} °C")
    print(f"Calefactor: {'ACTIVAT' if calefactor else 'APAGAT'}")
    print("-" * 40)

def mostrar_menu() :
    print("1 Configurar límits de temperatura")
    print("2 Veure estat actual")
    print("3 Sortir")

def control_temperatura() :
    minim = None
    maxim = None
    temps: float = random.randint(10,30)
    calefactor: bool = False

    while True:
        mostrar_menu()
        opcio: int = int(input("Selecciona una opció (1-3): "))

        match opcio:
            case 1:
                minim = float(input("Introdueix Temperatura MÍNIMA (°C): "))
                maxim = float(input("Introdueix Temperatura MÀXIMA (°C): "))

            case 2:
                while minim is None or maxim is None:
                    try:
                        minim = int(input("Introdueix el mínim: "))
                        maxim = int(input("Introdueix el màxim: "))
                        if minim >= maxim:
                            minim = maxim = None
                    except ValueError:
                        minim = maxim = None

                temps = float(input("Introdueix temperatura ACTUAL (°C): "))

                if temps < minim:
                    calefactor = True
                elif temps >= maxim:
                    calefactor = False

                missatge(minim, maxim, temps, calefactor)

            case 3:
                return

control_temperatura()

def missarge(limit: float, co2_actual: float, alarma: bool):
    print(f"Límit de CO₂ establert: {limit} ppm")
    print(f"Nivell actual de CO₂: {co2_actual} ppm")
    print(f"Alarma: {'ACTIVADA' if alarma else 'DESACTIVADA'}")

def menu_alarma() :
    print("1 Configurar límit de CO₂")
    print("2 Veure estat actual")
    print("3 Sortir")

def alarma() :
    limit: float = None
    alarma: bool = False

    while True:
        menu_alarma()
        opcio: int = int(input("Selecciona una opció (1-3): "))

        match opcio:
            case 1:
                limit = float(input("Introdueix el límit MÀXIM de CO₂ (ppm): "))

            case 2:
                co2_actual: float = float(input("Introdueix el nivell ACTUAL de CO₂ (ppm): "))
                if co2_actual > limit:
                    alarma = True
                else:
                    alarma = False
                missarge(limit, co2_actual, alarma)

            case 3:
                return

alarma()
