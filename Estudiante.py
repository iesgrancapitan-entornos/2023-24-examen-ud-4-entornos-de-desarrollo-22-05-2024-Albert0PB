"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""


class Persona:
    """
    Implementación de una clase 'Persona'
    """
    apellidos = "Apellidos";
    nombre = "Nombre";
    nif = "11111111Z";


class Estudiante(Persona):
    """
    Implementación de una clase 'Estudiante' que hereda de la clase 'Persona'
    """
    curso = "Primaria";

    def __init__(self):
        """
        Constructor de la clase 'Estudiante'
        """
        pass;

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Constructor de la clase 'Estudiante'
        :param nif:
        :param curso:
        :param nombre:
        :param apellidos:
        """
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def nif(self):
        """
        Propiedad 'nif'
        :return:
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Setter de 'nif'
        :param value:
        :return:
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Propiedad 'curso'
        :return:
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Setter de 'curso'
        :param value:
        :return:
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        Propiedad 'nombre'
        :return:
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Setter de 'nombre'
        :param value:
        :return:
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        Propiedad 'apellidos'
        :return:
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Setter de 'apellidos'
        :param value:
        :return:
        """
        self.__apellidos = value
