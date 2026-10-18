# Y por último, esto fue relizado para el primer punto, donde se solicitaba crear la clase Asignatura, con su información además de un main para probar que la clase funcionara correctamente.

class Asignatura: 
    def __init__(self, code, name, credits, academic_program):
        self.set_code(code)
        self.set_name(name)
        self.set_credits(credits)
        self.set_academic_program(academic_program)
    
    def get_code(self):
        return self._code
    def set_code(self, code):
        if code !="":
            self._code=code
        else:
            raise ValueError("El código no puede estar vacio")
        
    def get_name(self):
        return self._name
    def set_name(self, name):
        if name !="":
            self._name=name
        else:
            raise ValueError("El nombre no puede estar vacio")
      
    #Para el segungo punto (Punto 2) hay que hacer una modificación en el def de los creditos por materia, ya que se solicita que el número de créditos sea mayor a cero     
    def get_credits(self):
        return self._credits
    def set_credits(self, credits):
        if credits > 0:
            self._credits=credits
        else:
            raise ValueError("Los créditos no pueden ser menores a cero")
        
    def get_academic_program(self):
        return self._academic_program
    def set_academic_program(self, academic_program):
        if academic_program !="":
            self._academic_program=academic_program
        else:
            raise ValueError("El programa académico no puede estar vacio")
        
    def mostrar_informacion(self):
        print("code:", self.get_code())    
        print("name:", self.get_name())
        print("credits:", self.get_credits())
        print("academic_program:", self.get_academic_program())
        
        