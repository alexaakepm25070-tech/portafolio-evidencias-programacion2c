class cuentaBancaria:
    def _init_(self, saldo):
        self._saldo = saldo # _saldo, _saldo

    def depositar(self, cantidad):
        self._saldo += cantidad
      
    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad

        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo: {self._saldo}")



cuenta = cuentaBancaria(5000)
cuenta.set_saldo(-5000)
print(cuenta.get_saldo())
cuenta.mostrar_saldo()