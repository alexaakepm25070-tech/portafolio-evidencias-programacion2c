class Cuenta:
    """
    Clase que representa una cuenta bancaria.
    """
    
    def _init_(self, cliente, cuenta, saldo):
        """
        Inicializa una nueva cuenta.
        
        Args:
            cliente (str): Nombre del cliente.
            cuenta (str): Número de cuenta.
            saldo (float): Saldo inicial.
        """
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo

    def deposito(self, cantidad):
        """
        Deposita una cantidad en la cuenta.
        
        Args:
            cantidad (float): Monto a depositar.
            
        Returns:
            bool: True si se realizó el depósito, False si no.
        """
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta.
        
        Args:
            cantidad (float): Monto a retirar.
            
        Returns:
            bool: True si se realizó el retiro, False si no.
        """
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

def main():
    """Función principal del programa."""
    pass

if __name__== '_main_':
    main()
