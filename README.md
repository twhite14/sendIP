# sendIP
Send a device's local IP addresses to a specified email address when it changes.

## Requirements
 - python 2.7.x (I'm running 2.7.10)
 - email address provided by gmail (to send mail from)
 - a periodic task scheduler (Windows Task Scheduler or Crontab)
 - an internet connection

## Execution
I recommend placing this file in your python Scripts directory if you'll be running it periodically. The script will only send an email in the event of a change.

1. Make a copy of "sendIP_accounts_template.py" and give it the name "sendIP_accounts.py".
2. Enter your source email address, source email password, and the destination email addresses into the file "sendIP_accounts.py".
3. Change "content" on line 26 of "sendIP.pyw" to give your message a personal touch.
4. Add the file to a scheduled task in either Windows Task Scheduler or Crontab and you're done. 

## Known Issues
This function does not work as expected on the Raspberry Pi and returns only the local loopback IP address, 127.0.1.1.