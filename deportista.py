class Deportista:
   
    def __init__(self, deporte, años):
        self._deporte = deporte
        self._añosPracticando = años
      
    def setDeporte(self, deporte):
        self._deporte = deporte
    def getDeporte(self):
        return self._deporte
    
    def setAñosPracticando(self, años):
        self._añosPracticando = años
    def getAñosPracticando(self):
        return self._añosPracticando
    