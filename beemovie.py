
#Imports :)
import time
import smtplib

#You might have to change settings in your google account
auth = ("<your google email>", '<your google password>')

#Start server & login
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login(auth[0], auth[1])

#If you use this make sure this script and the txt file are in the same place
beemovie = open('beemovie.txt', 'r')
for word in beemovie.read().split():
    time.sleep(1)
    #Remove comment to have it printed in the console
    #print(word)

    #Use the phone number + thhe provider the reciever uses. I've listed some below.
    server.sendmail( auth[0], '<phonennumber@provider.net>', word)

    ##The above miggghhtt not work to improved security standards, but I've found a work
    ##around (for some providers) with adding headers as follows:

    message = ("From: <myname>"
             + "To: <theirame>"
             + "Subject: <beemovie>"
             + "\r\n"
             + word)
    server.sendmail(auth[0], '<phonennumber@provider.net>', word)

    # Some providers:
    # AT&T @mms.att.net
    # T-Mobile @tmomail.net
    # Virgin 'phonenumber@virgin.net'
    # Sprint: @pm.sprint.com
    # Verizon: @vtext.com
