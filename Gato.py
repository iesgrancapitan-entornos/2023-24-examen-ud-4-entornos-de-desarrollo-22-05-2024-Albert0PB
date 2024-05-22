"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""
class Gato:
    """
    Implementación de una clase 'Gato'
    """

    def maullar(self):
        """
        Método de los objetos de esta clase que hace que el Gato maúlle
        :return:
        """
        self.maulla = 'Miau'
        print('%s' % self.maulla);

g = Gato();
g.maullar();
