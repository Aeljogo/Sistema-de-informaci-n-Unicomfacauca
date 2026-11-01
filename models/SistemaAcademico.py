

from models.Excepciones import AsignaturaNoEncontradaError, ProgramaNoEncontradoError

class SistemaAcademico:
    def __init__(self):
        self._programas = []
        self._asignaturas = []

    def agregar_programa(self, programa):
        self._programas.append(programa)

    def agregar_asignatura(self, asignatura):
        self._asignaturas.append(asignatura)

    def buscar_asignatura(self, code):
        for a in self._asignaturas:
            if a.get_code() == code:
                return a
        raise AsignaturaNoEncontradaError(code)

    def buscar_programa(self, code):
        for p in self._programas:
            if p.get_code() == code:
                return p
        raise ProgramaNoEncontradoError(code)