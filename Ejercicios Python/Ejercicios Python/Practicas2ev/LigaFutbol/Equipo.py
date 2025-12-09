
# Equipo.java
# Esta clase hace referencia a los equipos de la liga de fútbol. Cada uno de ellos debe estar formado por los siguientes
# tipos de datos:
# ● Nombre (String)
# ● Estadio (String)
# ● Fundación (int)
# ● Jugadores (Jugador[])
# ● Puntos (int)
# ● Partidos ganados (int)
# ● Partidos perdidos (int)
# ● Partidos empatados (int)
# Además, debe contener todos los métodos get y set necesarios para cada uno de los atributos de la clase.


class Equipo:
    def __init__(self, nombre, estadio, fundacion, jugadores=None, puntos=0, 
                 partidos_ganados=0, partidos_perdidos=0, partidos_empatados=0):
        """
        Constructor de la clase Equipo
        
        Args:
            nombre (str): Nombre del equipo
            estadio (str): Nombre del estadio del equipo
            fundacion (int): Año de fundación del equipo
            jugadores (list): Lista de objetos Jugador (por defecto lista vacía)
            puntos (int): Puntos acumulados en la liga
            partidos_ganados (int): Número de partidos ganados
            partidos_perdidos (int): Número de partidos perdidos
            partidos_empatados (int): Número de partidos empatados
        """
        self.__nombre = nombre
        self.__estadio = estadio
        self.__fundacion = fundacion
        self.__jugadores = jugadores if jugadores is not None else []
        self.__puntos = puntos
        self.__partidos_ganados = partidos_ganados
        self.__partidos_perdidos = partidos_perdidos
        self.__partidos_empatados = partidos_empatados

    # Métodos GET
    def get_nombre(self):
        """Obtiene el nombre del equipo"""
        return self.__nombre
    
    def get_estadio(self):
        """Obtiene el estadio del equipo"""
        return self.__estadio
    
    def get_fundacion(self):
        """Obtiene el año de fundación del equipo"""
        return self.__fundacion
    
    def get_jugadores(self):
        """Obtiene la lista de jugadores del equipo"""
        return self.__jugadores
    
    def get_puntos(self):
        """Obtiene los puntos acumulados del equipo"""
        return self.__puntos
    
    def get_partidos_ganados(self):
        """Obtiene el número de partidos ganados"""
        return self.__partidos_ganados
    
    def get_partidos_perdidos(self):
        """Obtiene el número de partidos perdidos"""
        return self.__partidos_perdidos
    
    def get_partidos_empatados(self):
        """Obtiene el número de partidos empatados"""
        return self.__partidos_empatados
    
    # Métodos SET
    def set_nombre(self, nombre):
        """Establece el nombre del equipo"""
        self.__nombre = nombre
    
    def set_estadio(self, estadio):
        """Establece el estadio del equipo"""
        self.__estadio = estadio
    
    def set_fundacion(self, fundacion):
        """Establece el año de fundación del equipo"""
        self.__fundacion = fundacion
    
    def set_jugadores(self, jugadores):
        """Establece la lista de jugadores del equipo"""
        self.__jugadores = jugadores
    
    def set_puntos(self, puntos):
        """Establece los puntos acumulados del equipo"""
        self.__puntos = puntos
    
    def set_partidos_ganados(self, partidos_ganados):
        """Establece el número de partidos ganados"""
        self.__partidos_ganados = partidos_ganados
    
    def set_partidos_perdidos(self, partidos_perdidos):
        """Establece el número de partidos perdidos"""
        self.__partidos_perdidos = partidos_perdidos
    
    def set_partidos_empatados(self, partidos_empatados):
        """Establece el número de partidos empatados"""
        self.__partidos_empatados = partidos_empatados

    def __str__(self):
        """Representación en string del equipo"""
        return f"Equipo: {self.__nombre}, Estadio: {self.__estadio}, Fundación: {self.__fundacion}, Jugadores: {len(self.__jugadores)}, Puntos: {self.__puntos}, Partidos: G{self.__partidos_ganados} P{self.__partidos_perdidos} E{self.__partidos_empatados}"