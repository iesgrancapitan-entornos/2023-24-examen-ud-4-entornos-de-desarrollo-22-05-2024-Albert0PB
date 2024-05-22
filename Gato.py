"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""
class Gato:

    def maullar(self):
        self.maulla = 'Miau'
        print('%s' % self.maulla);

g = Gato();
g.maullar();
