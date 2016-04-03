#sendIP v1.2
#Periodically executed using Windows Task Scheduler. If the local IP address of this PC has changed since last run, email it to the specified address.
#This comes in handy when your IP is subject to change without warning.

import socket                           #To obtain local IP
import smtplib                          #To send email 
from email.mime.text import MIMEText    #To format email
from sendIP_accounts import *           #sourceAddress, sourcePassword, destinationAddress

#Make sure the log file exists. Really only needed for first run.
directory = './'
try:
  lastMSG = open(directory + 'last.txt', 'r')
except IOError:
  lastMSG = open(directory + 'last.txt', 'w')
  lastMSG.close()
  lastMSG = open(directory + 'last.txt', 'r')

#Add local IPs to a list
ipList = []
pcName = socket.gethostname()
for ip in (socket.gethostbyname_ex(pcName)[2]):
  ipList.append(ip)

#Create the content of the email message. Also used in a comparison to check if a new message is required.
content = 'The Local IP address of ' + pcName + ' has changed. It is now one of these:\n'
for ip in ipList:
  content = content + ip + '\n'

#Get the contents of the last message sent
lastMSGTxt = lastMSG.read()

#Compare, send message if needed. Close files.
if(lastMSGTxt != content):
  #Write the new data to the log file.
  lastMSG.close()
  lastMSG = open('last.txt', 'w')
  lastMSG.write(content)
  lastMSG.close()

  #Create an email message
  msg = MIMEText(content)
  msg['Subject'] = 'New IP Address for '+ pcName
  msg['From'] = sourceAddress
  msg['To'] = destinationAddress

  #Connect to the SMTP server
  #This section will change depending on your email provider. I use gmail.
  mail = smtplib.SMTP('smtp.gmail.com', 587)
  #Server handshakes
  mail.ehlo()
  mail.starttls()

  #Send the message
  mail.login(sourceAddress, sourcePassword)
  mail.sendmail(sourceAddress, destinationAddress, msg.as_string())
  mail.quit
else:
  lastMSG.close()