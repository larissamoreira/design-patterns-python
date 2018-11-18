from controllers.controller import ControllerHotel
from models.hotel import Hotel
from models.quarto import Quarto
from models.tipo_quarto import TipoQuarto

if __name__ == '__main__':
    
    #Cadastros

    hotel1 = Hotel('Hotel Maravilha', 'João Pessoa', 'Epitácio Pessoa, 221', '20', '7.0')
    hotel1.add_quarto(Quarto(1, TipoQuarto.SINGLE, 98.00, hotel1))
    hotel1.add_quarto(Quarto(2, TipoQuarto.DUPLO, 70.50, hotel1))
    hotel1.add_quarto(Quarto(3, TipoQuarto.TRIPLO, 40.50, hotel1))
    hotel1.add_quarto(Quarto(4, TipoQuarto.PRESIDENCIAL, 160.70, hotel1))

    hotel2 = Hotel('Hotel Caravelas', 'João Pessoa', 'Ranieri Mazilli, 221', '40', '9.6')
    hotel2.add_quarto(Quarto(5, TipoQuarto.SINGLE, 18.00, hotel2))
    hotel2.add_quarto(Quarto(6, TipoQuarto.DUPLO, 20.50, hotel2))
    hotel2.add_quarto(Quarto(7, TipoQuarto.TRIPLO, 30.50, hotel2))
    hotel2.add_quarto(Quarto(8, TipoQuarto.PRESIDENCIAL, 100.70, hotel2))

    hotel3 = Hotel('Hotel PAD', 'Campina Grande', 'Avenida Haddad, 43', '10', '10')
    hotel3.add_quarto(Quarto(9, TipoQuarto.SINGLE, 50.00, hotel3))
    hotel3.add_quarto(Quarto(10, TipoQuarto.SINGLE, 54.00, hotel3))
    hotel3.add_quarto(Quarto(11, TipoQuarto.DUPLO, 70.50, hotel3))
    hotel3.add_quarto(Quarto(12, TipoQuarto.TRIPLO, 80.50, hotel3))
    hotel3.add_quarto(Quarto(13, TipoQuarto.PRESIDENCIAL, 200.00, hotel3))
    
    main = ControllerHotel()
    main.start()