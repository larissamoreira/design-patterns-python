from quarto import Quarto
from hotel import Hotel
from tipo_quarto import Tipo

#Hoteis
hotel1 = Hotel('Hotel Maravilha', 'João Pessoa', 'Epitácio Pessoa, 221', '20', '9.6')
hotel1.add_quarto(Quarto(Tipo.SINGLE, 98.00))
hotel1.add_quarto(Quarto(Tipo.DUPLO, 70.50))
hotel1.add_quarto(Quarto(Tipo.TRIPLO, 40.50))
hotel1.add_quarto(Quarto(Tipo.PRESIDENCIAL, 160.70))

hotel2 = Hotel('Hotel Caravelas', 'João Pessoa', 'Ranieri Mazilli, 221', '40', '7.9')
hotel2.add_quarto(Quarto(Tipo.SINGLE, 18.00))
hotel2.add_quarto(Quarto(Tipo.DUPLO, 20.50))
hotel2.add_quarto(Quarto(Tipo.TRIPLO, 30.50))
hotel2.add_quarto(Quarto(Tipo.PRESIDENCIAL, 100.70))

hotel3 = Hotel('Hotel PAD', 'Campina Grande', 'Avenida Haddad, 43', '10', '10')
hotel3.add_quarto(Quarto(Tipo.SINGLE, 50.00))
hotel3.add_quarto(Quarto(Tipo.SINGLE, 54.00))
hotel3.add_quarto(Quarto(Tipo.DUPLO, 70.50))
hotel3.add_quarto(Quarto(Tipo.TRIPLO, 80.50))
hotel3.add_quarto(Quarto(Tipo.PRESIDENCIAL, 200.00))


def busca(cidade, tipo, preço=None):
    for hotel in Hotel.instances:
        if hotel.cidade == cidade:
            quartos = hotel.get_quartos(tipo, preço)
            for quarto in quartos:
                print(f'{hotel.nome} - R${quarto.preço} - {hotel.recomendacao}')
    
    
busca('João Pessoa', 'Duplo')
