# Liga.java
# Esta clase hace referencia al conjunto de equipos y jugadores. Una liga debe estar formada por lo siguiente:
# ● Nombre (String)
# ● Clasificacion (Equipo[])
# Además, debe contener todos los métodos get y set necesarios para cada uno de los atributos de la clase.


class Liga:
    def __init__(self, nombre, clasificacion=None):
       
        self.__nombre = nombre
        self.__clasificacion = clasificacion


    # Métodos GET
    def get_nombre(self):
        """Obtiene el nombre de la liga"""
        return self.__nombre    
    
    def get_clasificacion(self):
        """Obtiene la clasificación de la liga"""
        return self.__clasificacion
    
    # Métodos SET
    def set_nombre(self, nombre):
        """Establece el nombre de la liga"""
        self.__nombre = nombre

    def set_clasificacion(self, clasificacion):
        """Establece la clasificación de la liga"""
        self.__clasificacion = clasificacion

    def __str__(self):
        """Representación en string de la liga"""
        return f"Liga: {self.__nombre}, Clasificacion: {len(self.__clasificacion)} equipos"
    


