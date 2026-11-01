#Según el punto 2, hay que crear una clase llamada horario, donde se tengan aspectos importantes para saber que días se dan las diferentes asignaturas. 

class Horario:
    def __init__(self, day, start_time, end_time, classroom):
        self.set_day(day)
        self.set_start_time(start_time)
        self.set_end_time(end_time)
        self.set_classroom(classroom)

    def get_day(self):
        return self._day
    
    def set_day(self, day):
        if day != "":
            self._day = day
        else:
            raise ValueError("El día no puede estar vacío")
    
    def get_start_time(self):
        return self._start_time
    
    def set_start_time(self, start_time):
        if start_time != "":
            self._start_time = start_time
        else:
            raise ValueError("La hora de inicio no puede estar vacía")
    
    def get_end_time(self):
        return self._end_time
    
    def set_end_time(self, end_time):
        if end_time != "":
            self._end_time = end_time
        else:
            raise ValueError("La hora de finalización no puede estar vacía")
        
    def get_classroom(self):
        return self._classroom 
    
    def set_classroom(self, classroom):
        if classroom != "":
            self._classroom = classroom
        else:
            raise ValueError("El salón no puede estar vacío")    
    
    def mostrar_informacion(self):
            print("Día:", self.get_day())
            print("Hora de inicio:", self.get_start_time())
            print("Hora de finalización:", self.get_end_time())
            print("Salón:", self.get_classroom())