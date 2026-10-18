#Esto fue relizado para el primer punto, donde también se solicitaba crear la clase Programa Académico, con su información además de un main para probar que la clase funcionara correctamente.

class ProgramaAcademico:
    def __init__(self, code, name, department, semesters):
        self.set_code(code)
        self.set_name(name)
        self.set_department(department)
        self.set_semesters(semesters)
        
    def get_code(self):
        return self._code
         
    def set_code(self, code):
        if code != "":
            self._code = code
        else: 
            raise ValueError("El código no puede ser vacio")
         
    def get_name(self):
        return self._name
     
    def set_name(self, name):
        if name != "":
            self._name = name
        else: 
            raise ValueError("El nombre no puede estar vacio")
                 
    def get_department(self):
        return self._department
                 
    def set_department(self, department):
        if department != "":
            self._department = department
        else: 
            raise ValueError("La facultad no puede estar vacia")         
        
    def get_semesters(self):
        return self._semesters
    
    #Para el segungo punto (punto 2) hay que hacer una modificación en el def de semestre, ya que se solicita que el semestre sea mayor a cero 
        
    def set_semesters(self, semesters):
        if semesters > 0:
            self._semesters = semesters
        else: 
            raise ValueError("El número de semestres no puede ser menor a cero")         
        
    def mostrar_informacion(self):
        print("code:", self.get_code())
        print("name:", self.get_name())
        print("department:", self.get_department())
        print("semesters:", self.get_semesters())


     
       
                