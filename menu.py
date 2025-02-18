from InterfazVent import InterfazVent
from InterfazClient import InterfazCliente
from InterfazProd import InterfazProd

while True:
    print("1. Clientes")
    print("2. Productos")
    print("3. Ventas")
    print("4. Salir")

    opcion = input('Ingrese una opcion: ')

    if opcion == '1':
        interfaz = InterfazCliente().menu()

    elif opcion == '2':
        interfaz = InterfazProd().menu()

    elif opcion == '3':
        interfaz = InterfazVent().menu()

    elif opcion == '4':
        break