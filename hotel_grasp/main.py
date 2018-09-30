from quarto import Quarto
from hotel import Hotel
from tipo_quarto import Tipo


hotel = Hotel('Hotel Maravilha', 'João Pessoa', 'Epitácio Pessoa, 221', '20', '9.6')
hotel.add_quarto(Quarto(Tipo.SINGLE, 98.00))
hotel.add_quarto(Quarto(Tipo.SINGLE, 70.50))
hotel.add_quarto(Quarto(Tipo.SINGLE, 40.50))
hotel.add_quarto(Quarto(Tipo.PRESIDENCIAL, 160.70))


quartos = hotel.get_quartos('Presidencial', 40.40)
if quartos:
    for quarto in quartos:
        print(quarto)
else:
    print('Não há quartos nesses parâmetros.')
