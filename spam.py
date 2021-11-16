from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# probé el bot y por dia podes mandar hasta 600 mails

host = "smtp.gmail.com"
port = 587
#escribi tu email
#username = "ginessanches@gmail.com"
username = "rellenar"
#escribi la contraseña del mail
#password ="asijdia"
password ="rellenar"
from_email = username
#en el to_list van los mails a spammear, podes poner 1 o mas. mientras mas pongas mas lento es el envio
to_list = ["ACA VAN LOS EMAIL"]
# to_list =["hola@gmail.com","jeaa@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.starttls()
email_conn.login(username, password)

the_msg = MIMEMultipart("")
#asunto del email
the_msg['Rellenar'] = "Rellenar"
the_msg["Rellenar"] = "Rellenar"


plain_txt = "Rellenar con texto"




while i<1000:
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    print("EL BOT MANDO EL MAIL NUMERO " + str(i+1) + " a" + to_list) 
    i=i+1

print("Mandaste " + str(i) + " Emails")    
email_conn.quit()