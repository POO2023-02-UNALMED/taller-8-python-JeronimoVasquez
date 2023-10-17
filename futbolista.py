from deportista import Deportista
from persona import Persona
class Futbolista(Persona, Deportista):
    
    listaFutbolistas = []
    def __init__(self,nombre, edad, altura, sexo, años, golesMarcados, tarjetas, pierna):
        super(Persona, self).__init__(nombre, edad, altura, sexo)
        super(Deportista, self).__init__("Futbol", años)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetas
        self._piernaHabil = pierna
        Futbolista.listaFutbolistas.append(self)

    def setGolesMarcados(self, goles):
        self._golesMarcados = goles
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setTarjetasRojas(self, tarjetas):
        self._tarjetasRojas = tarjetas
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setPiernaHabil(self, pierna):
        self._piernaHabil = pierna
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def __str__(self):
        return f'Mi nombre es {self.getNombre()} soy profesional\
            en el deporte {self.getDeporte()}. Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte'
