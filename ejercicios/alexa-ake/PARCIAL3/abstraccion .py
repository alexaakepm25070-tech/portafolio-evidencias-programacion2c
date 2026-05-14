class cafetera:
    def preparar_cafe(self):
        self._hervir_agua() 
        self._mover_cafe()
        print("cafe listo!")

    def _hervir_agua(self):
        print("Hirviendo el agua")

    def _moler_cafe(self):
        print("Moliendo cafe")

def main():
    cafetera = cafetera()
    cafetera.preparar_cafe()
     
if __name__ == "_main_":
    main()
    
    
        
        
        
                        

