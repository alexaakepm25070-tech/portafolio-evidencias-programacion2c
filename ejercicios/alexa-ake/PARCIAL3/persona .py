"""
Crea una clase persona con los siguientes atributos: nombre, edad , genero , y nacionalidad
Agregar un metodo para imprimir los datos de la persona y otro metodo para  calcular el año de nacimiento
de la persona.
Crea un objeto de la clase persona y utiliza los metodos para mostar su informacion y
Calcular su año de nacimieno.
"""
class persona:

    def _init_(self, nombre, edad, genero, nacionalidad = "Mexico"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad


    def  informacion(self) :
        print("------Informacion------")
        print(f"Edad: {self.edad}")
        print(f"Genero: {self.genero}")
        print(f"nacionalidad: {self.nacionalidad}")
          
    def calcularNacimiento(self):
        year = datetime.date.today().year
        return year . self.edad
    
def main():
    objPersona = personas("Juan", 30, "Masculino")
    objPersona.informacion()
    print(f"Año de nacimiento:  {objPersona.calcularNacimiento()}")
 
if'_name_' == '_main_':
    main()
    