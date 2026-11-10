gastos = []

def agregar_gastos():
    categoria = input("Categoria: ")
    descripcion = input("Descripcion: ")
    while True:
        try:
            monto = int(input("Monto: $"))
            if monto > 0:
                break
            else: 
                print("solo numeros positivos")
        except ValueError:
            print("solo valores numericos")
    gastos.append([categoria, descripcion, monto])


def ver_gastos():
    for gasto in gastos:
        print(f"{gasto[0]} - {gasto[1]}  ${gasto[2]}")
    
def total_gastos():
    total = 0
    for gasto in gastos:
        total += gasto[2]
    print(f"total gastado ${total}")


while True:
    while True:
        try:
            opcion= int(input("\n 1. agregar gastos \n 2.ver gastos \n 3. ver total de gastos \n 4. salir \n elige una opcion: "))
            break
        except ValueError:
            print("Solo datos numericos del 1 al 4")

    if opcion == 1:
        agregar_gastos()
    elif opcion == 2:
        ver_gastos()
    elif opcion == 3:
        total_gastos()
    elif opcion == 4:
        break
    else: 
        print("Opcion no valida")
print("vuelva pronto...")



