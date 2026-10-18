
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
    print("Intentando asignar un correo vacío...")
    p.set_email("")
except ValueError as e:
    print("Validación exitosa:", e)


from models.ProgramaAcademico import ProgramaAcademico

try:
    print("Intentando crear un programa con 0 semestres...")
    pa = ProgramaAcademico("CP106", "Contaduría Pública", "Facultad de Ciencias Empresariales", 0)
except ValueError as e:
    print("Validación exitosa:", e)



from models.Asignatura import Asignatura
from models.ProgramaAcademico import ProgramaAcademico

pa = ProgramaAcademico("CP106", "Contaduría Pública", "Facultad de Ciencias Empresariales", 7)

try:
    print("Intentando crear una asignatura con créditos negativos...")
    a = Asignatura("AS106", "Finanzas II", -2, pa)
except ValueError as e:
    print("Validación exitosa:", e)


