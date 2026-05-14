class ave:
    def _init_(self, color = "verde"):
        self.color = color

    def volar(self):
        print("Puedo volar")

    
class canario(Ave):
    def _init_(self,color, nombre):
        super()._init_(color)
        self.nombe = nombre

    def informacion(self):
        pass

canario = canario("Amarillo", "fulnito")
print(canario.color)
canario.volar()
print(canario.color)



     