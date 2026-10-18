

from models.Persona import Persona

class Docente(Persona):
    def __init__(self, identification, name, email, teacher_code, teacher_program, employment_type, hours_per_week):
        super().__init__(identification, name, email)
       
        self.set_teacher_code(teacher_code)
        self.set_teacher_program(teacher_program)
        self.set_employment_type(employment_type)
        self.set_hours_per_week(hours_per_week)
    
    def get_teacher_code(self):
        return self._teacher_code
    
    def set_teacher_code(self, teacher_code):
        if teacher_code != "":
            self._teacher_code = teacher_code
        else:
            raise ValueError("El código del docente no puede estar vacio")
        
    def get_teacher_program(self):
        return self._teacher_program
    
    def set_teacher_program(self, program):
        if program != "":
            self._teacher_program = program
        else:
            raise ValueError("La facultad del docente no puede estar vacia")
        
    def get_employment_type(self):
        return self._employment_type
    
    def set_employment_type(self, employment_type):
        if employment_type != "":
            self._employment_type = employment_type
        else:
            raise ValueError("El tipo de empleo no puede estar vacio")
        
    def get_hours_per_week(self):
        return self._hours_per_week
    
    def set_hours_per_week(self, hours_per_week):
        if hours_per_week > 0:
            self._hours_per_week = hours_per_week
        else:
            raise ValueError("Las horas por semana no pueden ser negativas")
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Número de docente:", self.get_teacher_code())
        print("Facultad:", self.get_teacher_program())
        print("Tipo de empleo:", self.get_employment_type())
        print("Horas por semana:", self.get_hours_per_week())
        
    #Para el cuarto punto, se crea lo solicitado, que se relaciona con los comportamientos similares de las clases Estuadiante, Docente y Administrativo.
    
    def realizar_actividad_principal(self):
        print(f"Actividad principal: dicta clases en la facultad {self.get_teacher_program()} y trabaja {self.get_hours_per_week()} horas por semana")
        
        
    
    
    
      
        
        
        

   
        