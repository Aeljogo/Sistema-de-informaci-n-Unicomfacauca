
#Main para el la clase persona
from models.Persona import Persona

p = Persona ("106170", "Alejandro Paredes", "AlejandroParedes@unicomfacauca.edu.co")

# print(p.get_identification())
# print(p.get_name())
# print(p.get_email())

p= Persona("106170", "Alejandro Paredes", "AlejandroParedes@unicomfacauca.edu.co")
p.mostrar_informacion()

#Main para la clase del programa Academico
from models.ProgramaAcademico import ProgramaAcademico

pa = ProgramaAcademico("CP106", "Contaduría Pública", "Facultad de Ciecias Empresariales", 7 )

pa.mostrar_informacion()

#Main para la clase de la Asignatura

from models.Asignatura import Asignatura


a = Asignatura("AS106", "Finanzas II", 3, "Contaduría Pública")
a.mostrar_informacion()



#Con ayuda de Gemini, realicé la creaición de un main para probar las validaciones de las actulizaciones que se realizaron en las clases de Programa Académico y a su vez de Asignatura. 
from models.Persona import Persona

p = Persona("106170", "Alejandro Paredes", "AlejandroParedes@unicomfacauca.edu.co")

try:
 
    p.set_email("")
except ValueError as e:
    print("Validación exitosa:", e)


from models.ProgramaAcademico import ProgramaAcademico

try:
    
    pa = ProgramaAcademico("CP106", "Contaduría Pública", "Facultad de Ciencias Empresariales", 1)
except ValueError as e:
    print("Validación exitosa:", e)



from models.Asignatura import Asignatura
from models.ProgramaAcademico import ProgramaAcademico

pa = ProgramaAcademico("CP106", "Contaduría Pública", "Facultad de Ciencias Empresariales", 7)

try:
    
    a = Asignatura("AS106", "Finanzas II", 3, pa)
except ValueError as e:
    print("Validación exitosa:", e)


#Para probar parte del tercer punto, le pedí a gemini que creara un main para probar las clases de Estudiante, Docente y Administrativo. 

from models.Estudiantes import Estudiante
from models.Docentes import Docente
from models.Administrativos import Administrativo

def main():
   
    try:
        # 1. Prueba de la clase Estudiante
        print("--- REGISTRO DE ESTUDIANTE ---")
        estudiante = Estudiante(
            identification="1061700",
            name="Alejandro Paredes",
            email="AlejandroParedes@unicomfacauca.edu.co",
            student_code="CP106",
            program="Contaduría Pública",
            semester=7,
            promedio=4.5
        )
        estudiante.mostrar_informacion()
        print()

        # 2. Prueba de la clase Docente
        print("--- REGISTRO DE DOCENTE ---")
        docente = Docente(
            identification="252776",
            name="Claudia Gómez",
            email="cgomez@unicomfacauca.edu.co",
            teacher_code="DOC1020",
            teacher_program="Facultad de Ciencias Empresariales",
            employment_type="Tiempo Completo",
            hours_per_week=40
        )
        docente.mostrar_informacion()
        print()

        # 3. Prueba de la clase Administrativo
        print("--- REGISTRO DE ADMINISTRATIVO ---")
        administrativo = Administrativo(
            identification="45612378",
            name="Juan José Gómez",
            email="jgomez@unicomfacauca.edu.co",
            administrative_code="ADM5001",
            administrative_division="Registro y Control",
            administrative_role="Coordinador de Admisiones",
            work_schedule="Diurna"
        )
        administrativo.mostrar_informacion()
        print()

    except ValueError as e:
        print(f"Error de validación: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()

#Para el cuarto punto, le solicité a Gemini nuevamente, que creara un main para probar los comportamientos similares de las clases Estudiante, Docente y Administrativo.


from models.Estudiantes import Estudiante
from models.Docentes import Docente
from models.Administrativos import Administrativo

def main():
    print("==================================================")
    print("      SISTEMA ACADÉMICO - FASE 4 (POLIMORFISMO)  ")
    print("==================================================\n")

    try:
        # 1. Crear instancias usando los parámetros exactos de tus clases
        estudiante = Estudiante(
            identification="106170",
            name="Alejandro Paredes",
            email="AlejandroParedes@unicomfacauca.edu.co",
            student_code="CP106",
            program="Contaduría Pública",
            semester=7,
            promedio=4.5
        )

        docente = Docente(
            identification="252776",
            name="Claudia Gómez",
            email="cgomez@unicomfacauca.edu.co",
            teacher_code="DOC1020",
            teacher_program="Facultad de Ciencias Empresariales",
            employment_type="Tiempo Completo",
            hours_per_week=40
        )

        administrativo = Administrativo(
            identification="45612378",
            name="Juan José Gómez",
            email="jgomez@unicomfacauca.edu.co",
            administrative_code="ADM5001",
            administrative_division="Registro y Control",
            administrative_role="Coordinador de Admisiones",
            work_schedule="Diurna"
        )

        # 2. Guardar las personas en una lista para probar el polimorfismo
        personas = [estudiante, docente, administrativo]

        # 3. Recorrer la lista y ejecutar los métodos solicitados
        for persona in personas:
            persona.mostrar_informacion()
            persona.realizar_actividad_principal()
            print("-" * 50 + "\n")

    except ValueError as e:
        print(f"Error de validación: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()



#Para el punto 5, se desarrolla lo solicitado en el taller, donde dice que se deben crear como minimo dos estudiantes, dos docentes y dos administrativos
#Además de aplicar el ciclo solicitado y a su vez el polimorfismo que se indica. 

    try: 
        personas =  [
        Estudiante("106170", "Alejandro Paredes", "AlejandroParedes@unicomfacauca.edu.co", "CP106", "Contaduría Pública", 7, 4.5), 
        Estudiante("106171", "Sofia Bedoya", "SofiaBedoya@unicomfacauca.edu.co", "CP107", "Administración de Empresas", 7, 4.2), 
        ]
        
        