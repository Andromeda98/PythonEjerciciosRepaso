# Jugador.java
# Esta clase hace referencia a los jugadores de un equipo de fútbol. Cada uno de ellos debe estar formado por los
# siguientes tipos de datos:
# ● Nombre (String)
# ● Dorsal (int)
# ● Goles (int)
# ● Tarjetas rojas (int)
# ● Tarjetas amarillas (int)
# Además, debe contener todos los métodos get y set necesarios para cada uno de los atributos de la clase.


class Jugador:
    def __init__(self, nombre, dorsal, goles, tarjetasRojas, tarjetasAmarillas):
       
        self.__nombre = nombre
        self.__dorsal = dorsal
        self.__goles = goles
        self.__tarjetasRojas = tarjetasRojas
        self.__tarjetasAmarillas = tarjetasAmarillas


    # Métodos GET
    def get_nombre(self):
        """Obtiene el nombre del jugador"""
        return self.__nombre        
    def get_dorsal(self):
        """Obtiene el dorsal del jugador"""
        return self.__dorsal
    
    def get_goles(self):
        """Obtiene el número de goles del jugador"""
        return self.__goles
    
    def get_tarjetasRojas(self):
        """Obtiene el número de tarjetas rojas del jugador"""
        return self.__tarjetasRojas
    
    def get_tarjetasAmarillas(self):    
        """Obtiene el número de tarjetas amarillas del jugador"""
        return self.__tarjetasAmarillas
    
    # Métodos SET
    def set_nombre(self, nombre):
        """Establece el nombre del jugador"""
        self.__nombre = nombre

    def set_dorsal(self, dorsal):
        """Establece el dorsal del jugador"""
        self.__dorsal = dorsal
    
    def set_goles(self, goles):
        """Establece el número de goles del jugador"""
        self.__goles = goles

    def set_tarjetasRojas(self, tarjetasRojas):
        """Establece el número de tarjetas rojas del jugador"""
        self.__tarjetasRojas = tarjetasRojas

    def set_tarjetasAmarillas(self, tarjetasAmarillas):
        """Establece el número de tarjetas amarillas del jugador"""
        self.__tarjetasAmarillas = tarjetasAmarillas

    def __str__(self):
        """Representación en string del jugador"""
        return f"Jugador: {self.__nombre}, Dorsal: {self.__dorsal}, Goles: {self.__goles}, Tarjetas Rojas: {self.__tarjetasRojas}, Tarjetas Amarillas: {self.__tarjetasAmarillas}"
      