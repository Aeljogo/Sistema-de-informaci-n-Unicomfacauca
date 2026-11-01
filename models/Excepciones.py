

class EstudianteYaMatriculadoError(Exception):
    def __init__(self, student_code, Group_code):
        super().__init__(f"El estudiante {student_code} ya está matriculado en el grupo { Group_code}")

class GrupoLlenoError(Exception):
    def __init__(self, Group_code, maximum_capacity):
        super().__init__(f"El grupo {Group_code} alcanzó su capacidad máxima de {maximum_capacity} estudiantes")

class EstudianteNoMatriculadoError(Exception):
    def __init__(self, student_code, Group_code):
        super().__init__(f"El estudiante {student_code} no está matriculado en el grupo {Group_code}")

class AsignaturaNoEncontradaError(Exception):
    def __init__(self, code):
        super().__init__(f"La asignatura con código {code} no existe")

class ProgramaNoEncontradoError(Exception):
    def __init__(self, code):
        super().__init__(f"El programa académico con código {code} no existe")
        
        