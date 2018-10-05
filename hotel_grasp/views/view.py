from datetime import date

class View():
    def start(self):
        print("BuscOtel")
        return self.menu()
    
    def menu(self):
        print('---- Faça sua busca ----')
        cidade = input("Cidade: ")
        tipo = input("Tipo do quarto: ")
        preço = float(input("Faixa de preço: "))

        return {'cidade': cidade, 'tipo': tipo, 'preço': preço}
    
    def mostrar_quartos(self, quartos):
        print('\nResultado da busca:\n')
        opcoes = {}
        for quarto in quartos:
            print(f'{quarto.id} - {quarto.hotel.nome} - {quarto.tipo} - {quarto.preço} - {quarto.hotel.recomendacao}')
            opcoes[quarto.id] = quarto
        quarto_id = int(input('\nDigite o id do quarto que deseja reservar: '))

        return opcoes[quarto_id]

    def fazer_reserva(self):
        cliente = input("\nCliente: ")

        #Data de inicio
        entrada = input("Data de entrada [dd/mm/aaaa]: ")
        dia, mes, ano = entrada.split('/')
        entrada = date(int(ano), int(mes), int(dia))

        #Data de saída
        saida = input("Data de saída [dd/mm/aaaa]: ")
        dia, mes, ano = saida.split('/')
        saida = date(int(ano), int(mes), int(dia))

        #Modo pagamento
        modo = int(input('\n1: Boleto\n2: Cartão de crédito\nSelecione o modo de pagamento: '))

        return {'cliente': cliente, 'entrada': entrada, 'saida': saida, 'modo': modo}
        
    def mostrar_reservas(self, reservas):
        print('\nReservas:')
        for reserva in reservas:
            print(reserva)