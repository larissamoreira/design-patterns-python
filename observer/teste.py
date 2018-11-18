from subject import Subject
from observer_objects import JornalTempo, NoticiasTempo

# Tempo
empresa_tempo = Subject()

# Observadores
jornal_observador = JornalTempo()
noticias_observador = NoticiasTempo()

# Registrando os observadores para serem notificados
empresa_tempo.attach(jornal_observador)
empresa_tempo.attach(noticias_observador)

# Empresa do tempo manda mensagem para observadores
# Anunciando mudança no tempo hehe
empresa_tempo.notify('update', msg="Vai chover!!", graus="15 C")
