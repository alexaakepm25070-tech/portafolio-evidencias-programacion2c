
from cuenta import Cuenta
from banco import Banco
from cuenta import Cuenta 

def main():
    def menu():
        print("\n=== MENU DEL PROGRAMA MI BANCO ===")
        print("1. Aperturar nueva Cuenta")
        print("2. Ver clientes")
        print("3. Depositar a cuenta")
        print("4. Retirar de una Cuenta")
        print("5. Transferencia entre cuentas")
        print("6. Buscar Cuenta")
        print("7. Eliminar una Cuenta")
        print("8. Salir del programa")
    
    banco = Banco()
    lista_cuentas = []
    
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            numero_cuenta = input("Ingrese el número de cuenta: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            nueva_cuenta = Cuenta(nombre_cliente, numero_cuenta, saldo_inicial)
            lista_cuentas.append(nueva_cuenta)
            print(f"Cuenta creada para {nombre_cliente} con número {numero_cuenta}")
            
        elif opcion == "2":
            if not lista_cuentas:
                print("No hay cuentas registradas")
            else:
                print("------ LISTA DE CLIENTES ------")
                for cuenta in lista_cuentas:
                    cuenta.mostrar_info()
                    
        elif opcion == "3":
            num = input("Número de cuenta: ")
            monto = float(input("Monto a depositar: "))
            for cuenta in lista_cuentas:
                if cuenta.numero_cuenta == num:
                    cuenta.depositar(monto)
                    print("Depósito exitoso")
                    break
            else:
                print("Cuenta no encontrada")
                
        elif opcion == "4":
            num = input("Número de cuenta: ")
            monto = float(input("Monto a retirar: "))
            for cuenta in lista_cuentas:
                if cuenta.numero_cuenta == num:
                    if cuenta.retirar(monto):
                        print("Retiro exitoso")
                    else:
                        print("Fondos insuficientes")
                    break
            else:
                print("Cuenta no encontrada")
                
        elif opcion == "5":
            origen = input("Número de cuenta origen: ")
            destino = input("Número de cuenta destino: ")
            monto = float(input("Monto a transferir: "))
            
            cuenta_origen = None
            cuenta_destino = None
            
            for cuenta in lista_cuentas:
                if cuenta.numero_cuenta == origen:
                    cuenta_origen = cuenta
                if cuenta.numero_cuenta == destino:
                    cuenta_destino = cuenta
            
            if cuenta_origen and cuenta_destino:
                if banco.transferir(cuenta_origen, cuenta_destino, monto):
                    print("Transferencia exitosa")
                else:
                    print("No se pudo realizar la transferencia")
            else:
                print("Una o ambas cuentas no existen")
                
        elif opcion == "6":
            num = input("Número de cuenta a buscar: ")
            for cuenta in lista_cuentas:
                if cuenta.numero_cuenta == num:
                    cuenta.mostrar_info()
                    break
            else:
                print("Cuenta no encontrada")
                
        elif opcion == "7":
            num = input("Número de cuenta a eliminar: ")
            for i, cuenta in enumerate(lista_cuentas):
                if cuenta.numero_cuenta == num:
                    del lista_cuentas[i]
                    print("Cuenta eliminada")
                    break
            else:
                print("Cuenta no encontrada")
                
        elif opcion == "8":
            print("Gracias por usar Mi Banco. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "_main_":
    main()

    
    




