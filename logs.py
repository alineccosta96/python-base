''''
Aprendendo sobre log -> https://docs.python.org/3/library/logging.html
O tipo logging debug e o info só funciona em modo de desenvolvimento.
Para isso criamos uma var log chamado DEBUG.

%(asctime)s → data e hora do log
%(name)s → nome do logger (no seu caso, "Aline")
%(levelname)s → nível do log (DEBUG, INFO, WARNING etc.)
%(lineno)d → número da linha onde o log foi chamado
%(filename)s → nome do arquivo Python
%(message)s → mensagem que você passou no log
'''

import os
import logging
from logging import handlers #para salvar log em arquivo

#Mostrando o log debug precisa de: Instacia, level, formatação, destino
log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()
# Instancia: Cria o canal de log
log = logging.Logger("Aline", log_level)
# Level: Define a importância
#ch = logging.StreamHandler() #Esse aqui manda para o terminal/Console o erro
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meu_log.log", #nome doa rquivo de log
    maxBytes=100, #recomandado usar 10**6
    backupCount=10, #quantos eu vou salvar quando estuourar o maxBytes


)
fh.setLevel(log_level)
# Formatacao: Define o estilo da mensagem
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
# Destino: Define onde o log vai aparecer
#log.addHandler(ch)
log.addHandler(fh)


'''#Tipo de loggings
log.debug("Mensagem para desenvolvedor")
log.info("Mensagel eral para usuário")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro cirtico que afeta todo mundo. Ex. Banco de dados sumiu")'''

print("=" * 50)



try:
    1/0
except ZeroDivisionError as e:
    #print(f"Deu erro: {str(e)}")
    log.error("Deu erro: %s", str(e)) #Na bibiloteca de log não funciona do jeito acima somente por %s
