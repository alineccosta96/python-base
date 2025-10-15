'''
Para enviar e-mails podemos usar a smtplib, esta biblioteca permite o envio de mensagens formatadas no padrão SMTP.
Padrão SMTP
'''
import smtplib

# setamos algumas constantes
SERVER = "localhost"
PORT = 8025
FROM = "eu@server.com"
TO = ["destino@outroserver.com", "outro@server.com"]
SUBJECT = "Assunto do e-mail"
TEXT = "Este é meu e-mail enviado via Python no terminal :)"

# interpolamos a mensagem
message = f"""\
From: {FROM}
To: {', '.join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))

'''
Antes de rodar o script precisamos ter um servidor de e-mails, é possível se conectar a um servidor externo, como por exemplo o do google com:

server.starttls()
server.login(username, password)

Porém localmente você pode rodar um servidor de testes embutido no próprio Python, este servidor não envia e-mails, apenas imprime na tela para debugging.

Execute isso em um terminal:

python -m smtpd -c DebuggingServer -n localhost:8025 (funciona até o python 3.11)
python -m aiosmtpd -n -l localhost:8025 (do python 3.11 para cima)
Deixe o comando acima rodando e em outro terminal e execute esse smpt.py em outro. 
O email não vai mandar mas vai mostrar no terminal que vc executou o aiosmtpd
'''

'''
Usando mailtrap.io - para enviar email de verdade
Façá login em mailtrap.io e altere as informações de login para as suas próprias disponíveis em show credentials na pagina principal da sua inbox.

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login(user="83f1618af77272", password="ff77c56ae6ef22")
    server.sendmail(FROM, TO, message.as_string())
Agora os e-mails serão enviados para a caixa de mensagens da mailtrap.io

'''