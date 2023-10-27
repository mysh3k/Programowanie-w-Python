from email.message import EmailMessage
import smtplib
from secret_stuff import login, password

message = open('message.txt', 'r')

msg = EmailMessage()
msg['Subject'] = input("Podaj tytuł maila: ")
msg['From'] = "powiadomienia@biblioteka.krakow.pl"
msg['To'] = input("Podaj adres email adresata: ")
msg.set_content(message.read())
server = smtplib.SMTP("smtp.expro.pl")  # smtp server
server.set_debuglevel(1)
server.login(login, password)  # user & password
server.send_message(msg)
server.quit()
