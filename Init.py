import base64
email = base64.b64encode(input("[*] Enter the primary Email ID you wish to use for sending mail : ").encode())
password = base64.b64encode(input("[*] Enter the password : ").encode())
f = open("creds.txt","w")
f.write(str(email.decode()) + ":" + str(password.decode()))
f.close()
#print(base64.b64decode(email.decode()).decode())
#print(base64.b64decode(password).decode())