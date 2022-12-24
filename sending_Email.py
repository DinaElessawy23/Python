import smtplib
import ssl
from email.message import EmailMessage

subject= "Email from python"
body = "This is a test email from python!"
sender_email="dina.23elessawy@gmail.com"
receiever_email="dina.esawy3@gmail.com"
password=input("Enter your Password : ")

message= EmailMessage()
message["From"]=sender_email
message["TO"]= receiever_email
message["Subject"]=subject
message.set_content(body)

print("Sendin Email!")

context= ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as server:
  server.login(sender_email,password)
  server.sendmail(sender_email,receiever_email,message.as_string())
  
print("Success")	
