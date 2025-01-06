from ecommerce.Models.Carrello import Carrello
from ecommerce.Models.Articolo import Articolo

class Principale:

    carrelloArticoli = []
    carrello = Carrello()
    articolo = Articolo()

    def __init__(self,nome_negozio):
        self.nome_negozio = nome_negozio

        pass

    def aggiungiArticolo(self):
        pass
    def totaleCarrello(self):
        pass
    def rimuoviArticolo(self):
        pass
    def stampaCarrello(self):
        pass
    def totaleLibri(self):
        pass
    def totaleVideogiochi(self):
        pass


if __name__== "__main__":
    #Questo è il mio main
    ogg = Principale("gamestop")
    #Mi occupo di fare i metodi
