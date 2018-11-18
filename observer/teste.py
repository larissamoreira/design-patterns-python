from subject_object import WeatherData
from observer_objects import CondicoesAtuais, Estatisticas, Previsao

# Tempo
estacao = WeatherData(22, 10, 10)

# Observadores
condicoes = CondicoesAtuais()
estatisticas = Estatisticas()
previsao = Previsao()

# Registrando os observadores para serem notificados
estacao.attach(condicoes)
estacao.attach(estatisticas)
estacao.attach(previsao)

# Estação realiza mudanças no tempo e notifica os observadores
estacao.set_temp(15)
estacao.set_humidity(12)
estacao.set_pressure(5)
