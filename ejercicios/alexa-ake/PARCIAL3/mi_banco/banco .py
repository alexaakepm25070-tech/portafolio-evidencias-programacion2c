from cuenta import cuenta 

class  Banco:

    def transferir(self, origen, destino, cantidad):
        if origen.retirar(cantidad):
            destino.deposito(cantidad)
            return True
        return False