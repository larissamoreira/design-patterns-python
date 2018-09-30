class Hotel:
    instances = []
    def __init__(self, nome, cidade, endereço, dist_centro, recomendacao):
        self.nome = nome
        self.cidade = cidade
        self.endereço = endereço
        self.dist_centro = dist_centro
        self.recomendacao = recomendacao
        self.quartos = []
        self.instances.append(self)

    # Adiciona obj Quarto ao hotel
    def add_quarto(self, Quarto):
        self.quartos.append(Quarto)

    # Retorna os quartos disponiveis do hotel por tipo, é opcional filtrar pelo preço do quarto.
    def get_quartos(self, tipo, preço=None):
        r = []
        for quarto in self.quartos:
            if quarto.disponivel:
                if quarto.tipo == tipo:
                    if preço:
                        if quarto.preço <= preço:
                            r.append(quarto)
                    else:
                        r.append(quarto) 
        return r

    def __str__(self):
        return f'{self.nome}'