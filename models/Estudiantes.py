#

from models.Persona import Persona

class Estudiante(Persona):
    
    def __init__(self, identification, name, email, student_code, program, semester, promedio):
        super().__init__(identification, name, email)
        self.set_student_code(student_code)
        self.set_student_program(program)
        self.set_student_semester(semester)
        self.set_promedio(promedio)
        
    def get_student_code(self):
        return self._student_code
    def set_student_code(self, student_code):
        if student_code != "":
            self._student_code = student_code
        else: 
            raise ValueError("El código del estudiante no puede estar vacio")
        
    def get_student_program(self):
        return self._student_program
    def set_student_program(self, program):
        if program != "":
            self._student_program = program
        else:
            raise ValueError("El programa académico no puede estar vacio")
        
    def get_student_semester(self):
        return self._student_semester
    def set_student_semester(self, semester):
        if semester > 0:
            self._student_semester = semester
        else:
            raise ValueError("El semestre del estudiante no puede ser menor a cero")
        
        
    def get_promedio(self):
        return self._promedio
    def set_promedio(self, promedio):
        if promedio >= 0.0:
            self._promedio = promedio
        else:
            raise ValueError("El promedio del estudiante no puede ser negativo")
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Código del estudiante:", self.get_student_code())
        print("Programa académico:", self.get_student_program())
        print("Semestre:", self.get_student_semester())
        print("Promedio:", self.get_promedio())
        
     #Para el cuarto punto, se crea lo solicitado, que se relaciona con los comportamientos similares de las clases Estuadiante, Docente y Administrativo. 
     
    def realizar_actividad_principal(self):
        print(f"Actividad principal: cursa el programa {self.get_student_program()} y se encuentra en el semestre {self.get_student_semester()}")
        
        