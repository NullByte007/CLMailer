# Date : 21 May 2021
# Email Sending using Command Line in Linux ! 
# Code by : Aniket Nitin Bhagwate - NullByte007
# GitHub : https://github.com/NullByte007
# kindly read README.txt before using this tool.

import email
import os
import base64
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import re

def show_banner():

    banner = """
+===============================================+    
||     ____ _     __  __       _ _             ||
||    / ___| |   |  \/  | __ _(_) | ___ _ __   ||
||   | |   | |   | |\/| |/ _` | | |/ _ \ '__|  ||
||   | |___| |___| |  | | (_| | | |  __/ |     ||
||    \____|_____|_|  |_|\__,_|_|_|\___|_|     ||
+===============================================+    
+============ Command-Line-Mailer ==============+
+===============================================+    
+ Code by : Aniket Nitin Bhagwate (NullByte007) +
+===============================================+    
+ GitHub  : https://github.com/NullByte007      +
+===============================================+         
"""
    os.system("clear")
    print(banner)

helper_banner="""

"""

menu_banner="""
||========================================||
||                 ~ MENU ~               ||
||========================================||
|| {1} ONE Mail    | {2} MULTI Mail       ||
||========================================||
|| {3} BULK ATTACH MAIL  | {0} EXIT       ||
||========================================||
||          {101} HELPER MENU             ||
||========================================||
"""

# =============================================================================================

# METHOD FOR SENDING LOGIN AND SENDING THE MAIL ! 
def send_mail(email,password,message,receiver):
    sender = email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(email,password)
        server.sendmail(sender,receiver,message)
    except:
        print("\n \033[30;42;5m [X] MAIL NOT SENT !! \033[m \n")
        print("\n[!!] KINDLY CHECK \033[30;42m 'Allow less secure apps' \033[m IS SET TO {\033[30;42m ON \033[m} ")
        print("[!!] ALSO CHECK INTERNET CONNECTION ! ")
        print("\nVISIT THIS LINK TO CHECK : https://myaccount.google.com/lesssecureapps")
        input("\n<PRESS ENTER>")
        main()
    server.quit()

# =============================================================================================


# =============================================================================================
def ONE_mail(email,password):
    show_banner()

    # MAIL DATA INPUT
    receiver = input("[*] ENTER RECIIPENT EMAIL-ADDRESS : ")
    subject = input("[*] ENTER E-MAIL SUBJECT : ") + "\n"
    body = input("[*] ENTER E-MAIL BODY :  ") 
    
    # MESSAGE COMPILING 
    message = MIMEMultipart()
    message['From'] = email
    message['To'] = " ,".join(receiver)
    message['Subject'] = subject
    message.attach(MIMEText(body,'plain'))
    
    attachment_count = 0

    # METHOD TO ATTACH THE FILES 
    def singular_file_Attacher(number):
        print("\n \033[30;42;5m ATTACHMENT NO ==> ({}) \033[m ".format(number))
        filename = input("[*] ENTER FILENAME / PATH / DRAG THE FILE HERE ! ")
        f = open(filename,'rb') #opening file as read bytes !
        attachment = MIMEBase('application','octet-stream')
        attachment.set_payload((f).read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition',"attachment; filename=" + filename.split("/")[-1])
        message.attach(attachment)

    
    def bulk_file_Attacher(filename):
        f = open(filename,'rb') #opening file as read bytes !
        attachment = MIMEBase('application','octet-stream')
        attachment.set_payload((f).read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition',"attachment; filename=" + filename.split("/")[-1])
        message.attach(attachment)   
    

    choice_1 = input("[!] YOU WISH TO ADD ATTACHMENT ? <YES / NO> : " ).lower()
    
    # If choice to add attachment is YES !!!
    if choice_1=='yes' or choice_1=='y':
        choice_2 = input("[!] DO YOU WANT 'SINGULAR ATTACHMENTS' (S)  OR 'BULK ATTACHMENT' (B)  : ").lower()    
        
        # If choice to add singular attachments is YES !!
        if choice_2=='s':
            no_of_attachments = int(input("[*] ENTER NO OF ATTACHMENTS YOU WISH TO ATTACH : "))
            for x in range(no_of_attachments):
                singular_file_Attacher(x)
        
        # If choice to add BULK attachments is Yes !!
        elif choice_2=='b':
            attachment_folder_name = input("[*] ENTER ATTACHMENT FOLDER / DRAG FILE HERE :")
            if attachment_folder_name[-1]=="/":
                attachment_folder_name = attachment_folder_name[:-1]

            os.system("mkdir TEMP 1> /dev/null 2> /dev/null")
            os.system("ls " + attachment_folder_name + "> TEMP/index.txt")
            os.system("wc -l TEMP/index.txt | cut -d' ' -f1 > TEMP/attachment_count.txt")
        

            attachments = open("TEMP/index.txt","r")
            attachments  = attachments.read().split("\n")
            attachments.pop()

            attachment_count = open("TEMP/attachment_count.txt","r")
            attachment_count = attachment_count.read().split("\n")[0]
            print("\n")
            for x in range(int(len(attachments))):
                print("\033[30;42m [OK] [{}] ATTACHING ==> {} \033[m".format(x,attachments[x]))
                bulk_file_Attacher(str(attachment_folder_name) + "/" + str(attachments[x]))
     
    # If choice to add attachments is NO !!         
    else:
        pass
    
    # CONVERT TO STRING TO SEND
    text = message.as_string()
    print("\n[!] SENDING MAIL .............")

    # FUNCTION CALL
    send_mail(email,password,text,receiver)
    input("\n\033[30;42;5m [OK] MAIL SENT !.......... <PRESS ENTER> \033[m")
    main()
# =============================================================================================




# =============================================================================================

def MULTI_mail(email,password):
    show_banner()
    subject = input("[*] ENTER E-MAIL SUBJECT : ") + "\n"
    body = input("[*] ENTER E-MAIL BODY :  ") 
    recp_file = input("[*] ENTER THE FILE WITH RECIPIENTS EMAIL ADDRESSESS / DRAG FILE HERE !    : ")
    recipients = open(recp_file,'r')
    recipients = recipients.read().split()
    
    message = MIMEMultipart()
    message['From'] = email
    message['To'] = " ,".join(recipients)
    message['Subject'] = subject
    message.attach(MIMEText(body,'plain'))
    
    # METHOD TO ATTACH THE FILES 
    def singular_file_Attacher(number):
        print("\n \033[30;42;5m ATTACHMENT NO ==> ({}) \033[m ".format(number))
        filename = input("[*] ENTER FILENAME / PATH / DRAG THE FILE HERE ! ")
        f = open(filename,'rb') #opening file as read bytes !
        attachment = MIMEBase('application','octet-stream')
        attachment.set_payload((f).read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition',"attachment; filename=" + filename.split("/")[-1])
        message.attach(attachment)

    
    def bulk_file_Attacher(filename):
        f = open(filename,'rb') #opening file as read bytes !
        attachment = MIMEBase('application','octet-stream')
        attachment.set_payload((f).read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition',"attachment; filename=" + filename.split("/")[-1])
        message.attach(attachment)   
    

    choice_1 = input("[!] YOU WISH TO ADD ATTACHMENT ? <YES / NO> : " ).lower()
    
    # If choice to add attachment is YES !!!
    if choice_1=='yes' or choice_1=='y':
        choice_2 = input("[!] DO YOU WANT 'SINGULAR ATTACHMENTS' (S)  OR 'BULK ATTACHMENT' (B)  : ").lower()    
        
        # If choice to add singular attachments is YES !!
        if choice_2=='s':
            no_of_attachments = int(input("[*] ENTER NO OF ATTACHMENTS YOU WISH TO ATTACH : "))
            for x in range(no_of_attachments):
                singular_file_Attacher(x)
        
        # If choice to add BULK attachments is Yes !!
        elif choice_2=='b':
            attachment_folder_name = input("[*] ENTER ATTACHMENT FOLDER / DRAG FILE HERE :")
            if attachment_folder_name[-1]=="/":
                attachment_folder_name = attachment_folder_name[:-1]

            os.system("mkdir TEMP 1> /dev/null 2> /dev/null")
            os.system("ls " + attachment_folder_name + "> TEMP/index.txt")
            os.system("wc -l TEMP/index.txt | cut -d' ' -f1 > TEMP/attachment_count.txt")
        

            attachments = open("TEMP/index.txt","r")
            attachments  = attachments.read().split("\n")
            attachments.pop()

            attachment_count = open("TEMP/attachment_count.txt","r")
            attachment_count = attachment_count.read().split("\n")[0]

            for x in range(int(len(attachments))):
                print("\033[30;42m [OK] [{}] ATTACHING ==> {} \033[m".format(x,attachments[x]))
                bulk_file_Attacher(str(attachment_folder_name) + "/" + str(attachments[x]))
     
    # If choice to add attachments is NO !!         
    else:
        pass

    # CONVERT TO STRING TO SEND
    text = message.as_string()
    
    print("\n[!] SENDING MAIL .............")

    # FUNCTION CALL
    send_mail(email,password,text,recipients)
    input("\n\033[30;42;5m [OK] MAIL SENT !.......... <PRESS ENTER> \033[m")
    main()
# =============================================================================================


# =============================================================================================

def BULK_mail(email,password):
    message = MIMEMultipart()
    show_banner()
    subject_name = input("[*] ENTER SUBJECTS FILE / DRAG FILE HERE : ")
    body_name = input("[*] ENTER BODY FILE / DRAG FILE HERE : ")
    recipients_name = input("[*] ENTER RECIPIENTS FILE / DRAG FILE HERE : ")

    print("\n\n")

    subjects = open(subject_name,"r")
    subjects = subjects.read().split("\n")
    #subjects.pop()
    #print(subjects)

    body = open(body_name,"r")
    body = body.read().split("\n")
    #body.pop()

    recipients = open(recipients_name,"r")
    recipients = recipients.read().split()

    attachment_count = 0
    choice = input("[!] YOU WISH TO ADD ATTACHMENT ? <YES / NO> : " ).lower()
    if choice=='yes' or choice=='y':

        def file_Attacher(filename):
            #print("\n \033[30;42;5m ATTACHMENT NO ==> ({}) \033[m ".format(number))
            #filename = input("[*] ENTER FILENAME / PATH / DRAG THE FILE HERE ! ")
            f = open(filename,'rb') #opening file as read bytes !
            attachment = MIMEBase('application','octet-stream')
            attachment.set_payload((f).read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition',"attachment; filename=" + filename.split("/")[-1])
            message.attach(attachment)

        # INPUT Attachment Folder 
        attachment_folder_name = input("[*] ENTER ATTACHMENT FOLDER / DRAG FILE HERE :")
        if attachment_folder_name[-1]=="/":
            attachment_folder_name = attachment_folder_name[:-1]

        os.system("mkdir TEMP 1> /dev/null 2> /dev/null")
        os.system("ls " + attachment_folder_name + "> TEMP/index.txt")
        os.system("wc -l TEMP/index.txt | cut -d' ' -f1 > TEMP/attachment_count.txt")
    

        def natural_string_sort(l):
            convert = lambda text: int(text) if text.isdigit() else text
            alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
            return sorted(l, key = alphanum_key)

        attachments = open("TEMP/index.txt","r")
        attachments  = attachments.read().split("\n")
        attachments.pop()
        
        #print(attachments)
        
        z = open("TEMP/index.txt","w")
        for x in natural_string_sort(attachments):
            z.write(x+"\n")
        z.close()
        
        attachments = open("TEMP/index.txt","r")
        attachments  = attachments.read().split("\n")
        attachments.pop()

        attachment_count = open("TEMP/attachment_count.txt","r")
        attachment_count = attachment_count.read().split("\n")[0]

    else:
        pass

    show_banner()

    print("[**] THIS IS THE ACQUIRED DATA : \n")
    print("\033[30;42m [@] TOTAL SUBJECTS     : <{}> \033[m".format(len(subjects)))
    print("\033[30;42m [@] TOTAL BODY         : <{}> \033[m".format(len(body)))
    print("\033[30;42m [@] TOTAL RECIPIENTS   : <{}> \033[m".format(len(recipients)))
    print("\033[30;42m [@] TOTAL ATTACHMENTS  : <{}> \033[m".format(attachment_count))
    
    input("KINDLY CHECK THE INFORMATION ABOVE ...... < PRESS ENTER > AFTER CHECKING !")

    print("|-------------------------------------------------------------------------|")
    for x in range(int(len(recipients))):
        print(" <> RECIPIENT   => " + recipients[x])  
        print(" <> SUBJECT     => " + subjects[x]) 
        print(" <> BODY        => " + body[x])
        if choice=='yes' or choice=='y':   
            print(" <> ATTACHMENT  => " + attachments[x])
        print("|-------------------------------------------------------------------------|")

    input("CHECK THE ABOVE MAIL INFO ! <PRESS ENTER TO CONFIRM>")



    
    for x in range(int(len(recipients))):
        message['From'] = email
        message['To'] = recipients[x]
        message['Subject'] = subjects[x]
        message.attach(MIMEText(body[x],'plain'))
        if choice=='yes' or choice=='y':
            file_Attacher(str(attachment_folder_name) + "/" + str(attachments[x]))
        
        # CONVERT TO STRING TO SEND
        text = message.as_string()

        # FUNCTION CALL
        send_mail(email,password,text,recipients[x])
        print("[OK] MAIL => {} <=  SENT SUCCESSFULLY !".format(x))
        message = MIMEMultipart()

# =============================================================================================



# =============================================================================================

def helper():
    show_banner()
    try:
        f = open("helper.txt","r")
        f = f.read()
        print(f)
    except:
        print("[!!] ERROR ACCESSING THE HELPER.TXT FILE.")
        print("[*] KINDLY RUN THIS COMMAND TO GET THE FILE :\n wget https://raw.githubusercontent.com/NullByte007/CLMailer/main/helper.txt ")
    
    input("< PRESS ENTER AFTER READING >")
    main()
# =============================================================================================



# =============================================================================================

def main():
    show_banner()

    if os.path.isfile("creds.txt"):
        f = open("creds.txt","r")
        f = f.read().split(":")
        email = base64.b64decode(f[0]).decode()
        password = base64.b64decode(f[1]).decode()
    
    else:
        print("[!!] LOOKS LIKE creds.txt FILE IS NOT PRESENT ! KINDLY RUN Init.py BEFORE RUNNING CLMailer.py ")
        input("<PRESS ENTER>")
        sys.exit()

    print(menu_banner)
    choice = input("==> ")
    if choice =='1':
        ONE_mail(email,password) # Single recipient
    elif choice =='2':
        MULTI_mail(email,password) # Add recipients from a file
    elif choice =='3':
        BULK_mail(email,password) # add subject, body, attachments from a file for a bulk mail
    elif choice =='101':
        helper()  # Shows helper menu and explains when to use which option
    elif choice =='0':
        sys.exit()
    else:
        input("[!!] INVALID CHOICE ! .... <PRESS ENTER>")
        main()
# =============================================================================================




if __name__ == "__main__":
    main()
