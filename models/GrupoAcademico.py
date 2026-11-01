#Posteriormente, paso a crear el Grupo Academico, que también se solicita dentro de la fase dos.

from models.Horario import Horario
from models.Excepciones import (EstudianteYaMatriculadoError, GrupoLlenoError,  EstudianteNoMatriculadoError)



from models.Asignatura import Asignatura
from models.Docentes import Docente





class GrupoAcademico:
    def __init__(self, Group_code, Asignatura, Professor_in_charge, maximum_capacity, day, start_time, end_time, classroom):
        self.set_Group_code(Group_code)
        self.set_Asignatura(Asignatura)
        self.set_Professor_in_charge(Professor_in_charge)
        self.set_maximum_capacity(maximum_capacity)
        self._registered_students= []          #Le pedí a gemini que me corrigieria el error, ya que estaba poniendo el registered_students como si tuviera ya estudiantes. pero me dice la IA que un grupo debe iniciar de cero
        self._schedule=Horario (day, start_time, end_time, classroom)
        
        
    def get_Group_code(self):
        return self._Group_code
    
    def set_Group_code(self, Group_code):
        if Group_code !="":
            self._Group_code=Group_code
        else:
            raise ValueError("El código del grupo no puede estar vacio")
   
    def get_Asignatura(self):
        return self._Asignatura
        
    def set_Asignatura (self, Asignatura):
        if Asignatura!="":
            self._Asignatura=Asignatura
        else:
            raise ValueError ("El grupo necesita una asignatura")  
          
    def get_Professor_in_charge(self):
            return self._Professor_in_charge 
            
    def set_Professor_in_charge (self, Professor_in_charge):
            if Professor_in_charge !="":
                self._Professor_in_charge=Professor_in_charge
            else:
                raise ValueError ("El grupo necesita un profesor responsable")    
    
    def get_maximum_capacity(self):
            return self._maximum_capacity
            
    def set_maximum_capacity (self, maximum_capacity):
            if maximum_capacity > 0:
                self._maximum_capacity=maximum_capacity
            else:
                raise ValueError ("La capacidad debe ser mayor a cero")   
            
            
    def get_registered_students(self):
        return self._registered_students
    def set_registered_students(self, registered_students):
        if isinstance(registered_students, list):
            self._registered_students=registered_students
        else: 
            raise ValueError("Los estudiantes matriculados debn estarr en una lista")       
        
    def get_schedule(self):
            return self._schedule  
                      
                     
                
                
    def mostrar_informacion_grupo(self):
                print("Código de grupo", self.get_Group_code())
                print("Asignatura", self.get_Asignatura().get_name())
                print("Profesor encargado:", self.get_Professor_in_charge().get_name())
                print(f"Capacidad Máxima: {len(self._registered_students)}/{self.get_maximum_capacity()}") 
                self.get_schedule().mostrar_informacion()
        
              
    def matricular_estudiante(self, estudiante):
        
        for est in self._registered_students:
            if est.get_student_code() == estudiante.get_student_code():
                raise EstudianteYaMatriculadoError(estudiante.get_student_code(), self.get_Group_code())
        
        if len(self._registered_students) >= self.get_maximum_capacity():
            raise GrupoLlenoError(self.get_Group_code(), self.get_maximum_capacity())
       
        self._registered_students.append(estudiante)
        print(f"¡Estudiante {estudiante.get_name()} matriculado con éxito en el grupo {self.get_Group_code()}!")

    def retirar_estudiante(self, student_code):
        for est in self._registered_students:
            if est.get_student_code() == student_code:
                self._registered_students.remove(est)
                print(f"Estudiante con código {student_code} retirado del grupo {self.get_Group_code()}")
                return
        raise EstudianteNoMatriculadoError(student_code, self.get_Group_code())

    def mostrar_estudiantes(self):
        print(f"Estudiantes matriculados en el grupo {self.get_Group_code()}:")
        if len(self._registered_students) == 0:
            print("  (no hay estudiantes matriculados)")
        else:
            for est in self._registered_students:
                print(f"{est.get_student_code()}  {est.get_name()}")      
                
                
                 
                