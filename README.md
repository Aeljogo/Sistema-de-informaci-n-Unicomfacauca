-----Entrega 1.Entrega_AC1
-Sistema de Gestión Académica 
-Realizado por: David Alejandro Paredes Gómez, Segundo semestre Ingeniería de sistemas
-Descripción: Este sistema se basa en la aplicación de todos los conceptos que se han visto hasta el momento, en este caso en Phyton, empleando todo lo que se trató en las clases de programación orientada a objetos. 
El propósito es administrar la información básica de una comunidad educativa, para este caso, emplee el nombre para el ejercicio práctico de la universidad (Unicomfacauca) donde estudio mi otra carrera (Contaduría Pública) para hacerlo un poco mas "real"
-Estructura del Archivo: El archivo está compuesto por la carpeta models, que contiene las clases principales que son: Personas, Programa Académico y Asignatura, y a su vez contiene subclases como; Estudiantes, Docentes y Administrativos.
Contiene un main.py, donde realizaron las pruebas de funcionamiento de los códigos, para lograr corregir errores que estos tuvieran.
Algunos de estos mains, fueron construidos con ayuda de la inteligencia artificial de GEMINI, a quien le solicité colaboración para crear lo que me permitiera corroborar en que estaba fallando el código y lograr mejorarlo. 
-Instrucciones para ejecución: 
Primero es importante resaltar o saber que se debe tener Python para ejecutar el código
Posteriormente se pueden tomar los archivos de la carpeta models y del main del repositorio y pegarlos en phyton 
O si se quiere, se pueden descargar los archivos, ubicarlos en una carpeta del Pc donde se descarga y realizar la apertura con Phyton. 
-Herencia: Primero diseñé la clase "principal" llamada "Persona", que contiene los atributos comunes o importantes como; (Identificación, nombre y correo), posteriormente al crear a los estudiantes, profesores y administrativos, heredan esos "atributos" por medio de la función super().__init(), haciendo que el código no se repita para estas clases.
-Sobre Escritura: Hice que cada clase o subclase en este caso (Estudiantes, Docentes y administrativos), tuvieran su propia versión de mostrar_información, para que a los datos o atributos generales se les añadieran o sumaran los atributos de cada rol, teniendo en cuenta a su vez el método de realizar_actividad_principal().
-Polimorfismo:  Lo que se solicitó a cada clase es que por medio del método de realizas_actividad_principal(), es que se definiera que era a lo que se dedicaba cada clase , para que hagan la misma acción pero un resultado diferente ya que tienen diferentes funciones cada persona. Cabe aclarar que el main para que se hiciera el recorrido y la creación de los usuarios fue con ayuda de GEMINI



-----Entrega 2-Entrega_AC2

Este repositorio contiene la evolución del sistema de gestión académica que he venido realizando, de acuerdo a mi otra universidad (Unicomfacauca), desarrollado como parte de la Actividad  Nro 2. 

-En la clase Abstracta, la Persona se convirtió en clase abstracta (ABC), esto no permite instanciación directa y exige la implementación de realizar_actividad_principal().
-Oferta Académica, se hace la creación del modelo Grupo Academico, para la gestión de docentes, asignaturas, capacidad de cupos y estudiantes matriculados.
-Relación de composición, Se Incorpora el modelo Horario dentro de GrupoA cademico.
-Excepciones personalizadas corresponde al Control explícito de errores durante la matrícula, retiro de estudiantes y búsqueda de asignaturas o programas.
-La continuidad,  Demostración de captura de excepciones en `mainII.py` sin detener la ejecución del programa.
 Un grupo académico no es un horario, sino que tiene un horario.
 El horario nace dentro del grupo y solo existe mientras el grupo exista. Si el grupo se elimina, su horario asociado desaparece automáticamente.
Así se debe ver la estructura dentro del proyecto
 Persona.py              Clase abstracta base
 Estudiantes.py          Subclase con actividad principal
 Docentes.py              Subclase con actividad principal
 Administrativos.py       Subclase con actividad principal
 Asignatura.py            Modelo de Asignatura
 ProgramaAcademico.py    Modelo de Programa Académico
 Horario.py              Modelo de Horario (Día, Horas, Salón)
 GrupoAcademico.py        Modelo de Grupo con Composición y Excepciones
 SistemaAcademico.py     Módulo gestor de búsquedas
 Excepciones.py           Clases de excepciones personalizadas
 main.py                  Pruebas de la Fase 1
 mainII.py               Pruebas principales de ejecución para la entrega 2

