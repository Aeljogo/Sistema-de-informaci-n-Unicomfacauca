# main.py - Actividad Colaborativa N°2
# La versión de la Actividad 1 se conserva en main_AC1.py y en el tag Entrega_AC1

from models.Persona import Persona
from models.Estudiantes import Estudiante
from models.Docentes import Docente
from models.Administrativos import Administrativo
from models.ProgramaAcademico import ProgramaAcademico
from models.Asignatura import Asignatura
from models.GrupoAcademico import GrupoAcademico
from models.SistemaAcademico import SistemaAcademico
from models.Excepciones import (EstudianteYaMatriculadoError,
                                GrupoLlenoError,
                                EstudianteNoMatriculadoError,
                                AsignaturaNoEncontradaError,
                                ProgramaNoEncontradoError)


def main():
    # 1. Persona es abstracta: no se puede crear directamente (Fase 1)
    print("Prueba: crear una Persona directamente")
    try:
        p = Persona("106170", "Alejandro Paredes", "AlejandroParedes@unicomfacauca.edu.co")
    except TypeError as e:
        print("Error controlado:", e)
    print()

    # 2. Creación de programas, asignaturas, docentes y estudiantes
    sistema=SistemaAcademico()
    sistema.agregar_programa(ProgramaAcademico("CP106", "Contaduría Pública", "Facultad de Ciencias Empresariales", 7))
    sistema.agregar_asignatura(Asignatura("AS106", "Finanzas II", 3, "Contaduría Pública"))
    sistema.agregar_asignatura(Asignatura("AS107", "Costos", 3, "Contaduría Pública"))

    docente1 = Docente("252776", "Claudia Gómez", "cgomez@unicomfacauca.edu.co", "DOC1020",
                       "Facultad de Ciencias Empresariales", "Tiempo Completo", 40)
    docente2 = Docente("252777", "Javier Montoya", "jmontoya@unicomfacauca.edu.co", "DOC1021",
                       "Facultad de humanidades", "Cátedra", 16)

    e1 = Estudiante("106170", "Alejandro Paredes", "AlejandroParedes@unicomfacauca.edu.co",
                    "EST001", "Contaduría Pública", 7, 4.5)
    e2 = Estudiante("106171", "Sofia Bedoya", "SofiaBedoya@unicomfacauca.edu.co",
                    "EST002", "Contaduría Pública", 7, 4.3)
    e3 = Estudiante("106172", "Camilo Ruiz", "camilo@unicomfacauca.edu.co",
                    "EST003", "Contaduría Pública", 6, 4.0)

    # 3. Dos grupos académicos (el grupo crea su propio Horario: composición)
    #    El segundo tiene capacidad 2 para poder probar el cupo
    print("--- Grupos académicos ---")
    g1 = GrupoAcademico("G1", sistema.buscar_asignatura("AS106"), docente1, 30,
                        "Lunes", "08:00 AM", "10:00 AM", "A-101")
    g2 = GrupoAcademico("G2", sistema.buscar_asignatura("AS107"), docente2, 2,
                        "Martes", "02:00 PM", "04:00 PM", "B-203")
    g1.mostrar_informacion_grupo()
    print()
    g2.mostrar_informacion_grupo()
    print()

    # 4. Matrícula correcta
    print("--- Matrícula ---")
    g2.matricular_estudiante(e1)
    g2.matricular_estudiante(e2)
    print()

    # 5. Excepción: estudiante ya matriculado
    print("Prueba: estudiante ya matriculado")
    try:
        g2.matricular_estudiante(e1)
    except EstudianteYaMatriculadoError as e:
        print("Error controlado:", e)
    print()

    # 6. Excepción: grupo lleno
    print(" Prueba: grupo lleno")
    try:
        g2.matricular_estudiante(e3)
    except GrupoLlenoError as e:
        print("Error controlado:", e)
    print()

    # 7. Retiro correcto
    print("Retiro de estudiante")
    g2.retirar_estudiante("EST001")
    g2.mostrar_estudiantes()
    print()

    # 8. Excepción: retirar a un estudiante que no está matriculado
    print("Prueba: retirar un estudiante no matriculado")
    try:
        g2.retirar_estudiante("EST999")
    except EstudianteNoMatriculadoError as e:
        print("Error controlado:", e)
    print()

    # 9. Excepción: asignatura inexistente
    print("Prueba: asignatura inexistente")
    try:
        sistema.buscar_asignatura("AS999")
    except AsignaturaNoEncontradaError as e:
        print("Error controlado:", e)
    print()

    # 10. Excepción: programa académico inexistente
    print("Prueba: programa académico inexistente")
    try:
        sistema.buscar_programa("XX000")
    except ProgramaNoEncontradoError as e:
        print("Error controlado:", e)
    print()

    # 11. Polimorfismo: sigue funcionando con Persona abstracta
    print("Polimorfismo")
    admin = Administrativo("45612378", "Juan José Gómez", "jgomez@unicomfacauca.edu.co", "ADM5001",
                           "Registro y Control", "Coordinador de Admisiones", "Diurna")
    personas = [e1, docente1, admin]
    for persona in personas:
        persona.mostrar_informacion()
        persona.realizar_actividad_principal()
        print("-" * 50)

    print("\nEl programa continuó su ejecución después de todas las excepciones.")


if __name__ == "__main__":
    main()       