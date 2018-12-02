from abc import ABC, abstractmethod

class Casa(ABC):
    def __init__(self):
        pass
    
class Basica(Casa):
    def __init__(self):
        self.piso = 'Cerâmica'
        self.parede = 'Gesso'
        self.porta = 'MDF'
        self.tinta = 'Látex'
        self.metal = 'Ferro'
        self.louça = 'Genérica'
    
    def __str__(self):
        return self.piso

class Conforto(Casa):
    def __init__(self):
        self.piso = 'Cerâmica Esmaltada'
        self.parede = 'Alvenaria'
        self.porta = 'Madeira'
        self.tinta = 'Acrílica'
        self.metal = 'Alumínio'
        self.louça = 'Elizabeth'

    def __str__(self):
        return self.piso

class Luxo(Casa):
    def __init__(self):
        self.piso = 'Porcelanato'
        self.parede = 'Dry Wall'
        self.porta = 'Madeira de lei'
        self.tinta = 'Superlavável'
        self.metal = 'Inox'
        self.louça = 'DECA'
    
    def __str__(self):
        return self.piso

class CriarCasaFactory(ABC):
    @abstractmethod
    def criar_casa(self):
        pass

class LuxoFactory(CriarCasaFactory):
    def criar_casa(self):
        return Luxo()
    
class BasicaFactory(CriarCasaFactory):
    def criar_casa(self):
        return Basica()

class ConfortoFactory(CriarCasaFactory):
    def criar_casa():
        return Conforto()

if __name__ == '__main__':
    casa = BasicaFactory()
    print(casa.criar_casa())