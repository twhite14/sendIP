# sendIP
Send a device's local IP addresses to a specified email address periodically.

## Requirements:
 - python 2.7.x (I'm running 2.7.10)
 - email address provided by gmail (to send mail from)
 - a periodic task scheduler (Windows Task Scheduler or Crontab)
 - an internet connection

## Execution:
Enter your source email address, source email password, and the destination email addresses in the fields marked REDACTED on lines 38, 39, and 40 respectively. Change the "content" field on line 23 to give your message a personal touch. Add the file to a scheduled task in either Windows Task Scheduler or Crontab and you're done. The script will only send an email in the event of a change.