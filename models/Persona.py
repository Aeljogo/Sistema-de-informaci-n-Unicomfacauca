#Esto fue relizado para el primer punto, donde se solicitaba crear la clase persona, con su información además de un main para probar que la clase funcionara correctamente.

class Persona:
    
    def __init__(self, identification, name, email):
        
        self.set_identification(identification)
        self.set_name(name)
        self.set_email(email)
        
    def get_identification(self):
            return self._identification
        
    def set_identification(self, identification):
        if(identification!=""):
            self._identification = identification
        else: 
            raise ValueError("La identificación no puede ser vacia")
        
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
                if(name!=""):
                    self._name = name
                else: 
                    raise ValueError("El nombre no puede estar vacio")
                
    def get_email(self):
                    return self._email
                
                
    def set_email(self, email):
                if(email!=""):
                    self._email=email
                else: 
                    raise ValueError("El correo no puede estar vacio")  
                
         
    def mostrar_informacion(self):
        print("Identificación:", self.get_identification())
        print("Nombre:", self.get_name())
        print("Email:", self.get_email())
        