class Perro:
    
    
    # Constructor de la clase Perro
    def _init_(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

# Método para imprimir los datos del perro
    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} edad")
        print("especie: ", self.especie)


#Creacion de un objeto de la clase Perro
def main():
    perro1 = Perro("Firulais", "Labrador", 5)
    perro1.imprimirDatos()
    perro2 = Perro("Rex", "Pastor Alemán", 3)
    perro2.imprimirDatos()
    print("Información del perro 2:",perro2.nombre, perro2.raza, perro2.edad)
    perro3 = Perro("Max", "Bulldog", 2)
    perro3.imprimirDatos()
    perro4 = perro("Dante")
    perro4.edad = 4
    perro4.imprimirDatos()
    perro2.raza = "Pastor Belga"
    perro2.imprimirDatos()
    perro5 = perro("Raya", "Siames", 1)
    perro5.especie = "Felis catus"
    perro5.imprimirDatos()
    

    
    if __name__ == "_main_":
        main()


    