

from models.Persona import Persona

class Administrativo(Persona):
    def __init__(self, identification, name, email, administrative_code, administrative_division, administrative_role, work_schedule):
        
        super().__init__(identification, name, email)
        self.set_administrative_code(administrative_code)
        self.set_administrative_division(administrative_division)
        self.set_administrative_role(administrative_role)
        self.set_work_schedule(work_schedule)
        
    def get_administrative_code(self):    
        return self._administrative_code
    def set_administrative_code(self, administrative_code):
        if administrative_code != "":
            self._administrative_code = administrative_code
        else:
            raise ValueError("El código del administrativo no puede estar vacio")
    def get_administrative_division(self):
        return self._administrative_division
    def set_administrative_division(self, division):
        if division != "":
            self._administrative_division = division
        else:
            raise ValueError("La división del administrativo no puede estar vacia")
    def get_administrative_role(self):
        return self._administrative_role
    def set_administrative_role(self, role):
        if role != "":
            self._administrative_role = role
        else:
            raise ValueError("El rol del administrativo no puede estar vacio")
    def get_work_schedule(self):
        return self._work_schedule
    def set_work_schedule(self, work_schedule):
        if work_schedule != "":
            self._work_schedule = work_schedule
        else:
            raise ValueError("El horario de trabajo no puede estar vacio")
        
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Código del administrativo:", self.get_administrative_code())
        print("División:", self.get_administrative_division())
        print("Rol:", self.get_administrative_role())
        print("Horario de trabajo:", self.get_work_schedule())
        
        
    #Para el cuarto punto, se crea lo solicitado, que se relaciona con los comportamientos similares de las clases Estuadiante, Docente y Administrativo.
        
    def realizar_actividad_principal(self):
        print(f"Actividad principal: trabaja en la división {self.get_administrative_division()} y tiene el rol de {self.get_administrative_role()}")
        
            
        
        
        