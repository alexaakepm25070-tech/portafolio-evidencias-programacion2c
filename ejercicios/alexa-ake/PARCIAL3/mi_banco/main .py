from banco import Banco
from cuenta import Cuenta

def main():
    def menu():
        print("MENU DEL PROGRAMA MI BANCO")
        print("1. Aperturar nueva Cuenta")
        print("2. Ver clientes")
        print("3. Depositar a cuenta")
        print("4. Retirar de una Cuenta")
        print("5. Transferencia entre cuentas")
        print("6. Buscar Cuenta")
        print("7. Eliminar una Cuenta")
        print("8. Salir del programa")
    banco = Banco()
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            numero_cuenta = input("Ingrese el número de cuenta: ")
            print(f"Cuenta creada para {nombre_cliente} con número de cuenta {numero_cuenta}")
        elif opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            pass
        elif opcion == "8":
            print("Gracias por usar Mi Banco. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "_main_":
    main()

   


    
    




