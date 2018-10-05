class Quarto:
    def __init__(self, id, tipo, preço, hotel):
        self.id = id
        self.tipo = tipo
        self.preço = preço
        self.hotel = hotel
        self.disponivel = True

    def reservar(self):
        self.disponivel = False
    
    def __str__(self):
       return f'{self.tipo} - R${self.preço}'
