import unittest

from cuenta import cuenta
from banco import banco

class TestIntegracionBanco(unittest.TesCase):

    def setUp(self):
        self.cuenta1 = Cuenta("Fulanito perez","001", 1000)
        self.cuenta2 = Cuenta("Perezcila Sanchez", "002")

        self.banco = Banco()

    def test_transferencia_exitosa(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 350)
        self.assertTrue(resultado, "Deberia realizarse de manera correcta la transferencia")
        self.assertEqual(self.cuenta1.saldo, 650, "El saldo de la cuenta 1 deberia ser 650")
        self.assertEqual(self.cuenta2.saldo, 350,  "Elsa saldo de la cuenta destino deneria ser 350")

    def test_transferencia_saldo_insuficiente(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 1200)
        self.assertFalse(resultado, "La transferencia no se deberia realizar a no disponer del saldo suficiente")
        self.assertEqual(self.cuenta1.saldo, 1000, "El saldo deberia mantenerse sin cambios")
        self.assertEqual(self.cuenta2.saldo, 0, "El saldo de la cuenta destino deberia ser 0")

                         
    
                              
        
        
        
