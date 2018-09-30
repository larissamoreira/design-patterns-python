from quarto import Quarto
from hotel import Hotel
from tipo_quarto import TipoQuarto

#Hoteis
hotel1 = Hotel('Hotel Maravilha', 'João Pessoa', 'Epitácio Pessoa, 221', '20', '7.0')
hotel1.add_quarto(Quarto(TipoQuarto.SINGLE, 98.00))
hotel1.add_quarto(Quarto(TipoQuarto.DUPLO, 70.50))
hotel1.add_quarto(Quarto(TipoQuarto.TRIPLO, 40.50))
hotel1.add_quarto(Quarto(TipoQuarto.PRESIDENCIAL, 160.70))

hotel2 = Hotel('Hotel Caravelas', 'João Pessoa', 'Ranieri Mazilli, 221', '40', '9.6')
hotel2.add_quarto(Quarto(TipoQuarto.SINGLE, 18.00))
hotel2.add_quarto(Quarto(TipoQuarto.DUPLO, 20.50))
hotel2.add_quarto(Quarto(TipoQuarto.TRIPLO, 30.50))
hotel2.add_quarto(Quarto(TipoQuarto.PRESIDENCIAL, 100.70))

hotel3 = Hotel('Hotel PAD', 'Campina Grande', 'Avenida Haddad, 43', '10', '10')
hotel3.add_quarto(Quarto(TipoQuarto.SINGLE, 50.00))
hotel3.add_quarto(Quarto(TipoQuarto.SINGLE, 54.00))
hotel3.add_quarto(Quarto(TipoQuarto.DUPLO, 70.50))
hotel3.add_quarto(Quarto(TipoQuarto.TRIPLO, 80.50))
hotel3.add_quarto(Quarto(TipoQuarto.PRESIDENCIAL, 200.00))
