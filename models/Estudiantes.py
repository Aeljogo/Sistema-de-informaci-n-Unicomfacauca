#

from models.Persona import Persona

class Estudiante(Persona):
    
    def __init__(self, identification, name, email, program):
        super().__init__(identification, name, email)
        self.set_student_code(identification)
        self.set_student_program(program)
        self.set_student_semester(1)
        self.set_promedio(0.0)
        
    def get_student_code(self):
        return self._student_code
    def set_student_code(self, student_code):
        if student_code != "":
            self._student_code = student_code
        else: 
            raise ValueError("El código del estudiante no puede estar vacio")
        
        
        