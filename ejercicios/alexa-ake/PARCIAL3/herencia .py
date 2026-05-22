class ave:
    def _init_(self, color = "verde"):
        self.color = color
    
    def volar(self):
        print("Puedo volar")

class canario(ave):  # 'ave' con minúscula porque así se llama la clase padre
    def _init_(self, color, nombre):
        super()._init_(color)

    def informacion(self):
        pass

canario = canario("Amarillo", "fulnito")
print(canario.color)
canario.volar()
print(canario.color)



     