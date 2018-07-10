import smtplib
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
import sys
import commands

#More Added line to test jenkins
def fun(foo, emailadd, smtpserver):
	
	dirlist = os.listdir("/home")

	cmd = commands.getstatusoutput("df -h | awk 'FNR==2 {print $3 $4}'")
	values = cmd[1].split("G")
	print values[0]
	print values[1]
	val = float(values[1]) - float(values[0])

	if ( val <= 10 and val >=5):
	    bodyVal = "between 5 and 10"
	elif(val == 12):
	    bodyVal = "12"
	elif(val == 13):
	    bodyVal = "13"    
	elif(val == 11):
	    bodyVal = "11"
	elif(val == 12):
	    bodyVal = "12"
	elif(val < 5  and val >=2):
	    bodyVal = "greater than or equal to 2 and less 5"
	elif(val == 1):
	    bodyVal = "1"
	else:
	    bodyVal = str(val)
	    
	#cmd = os.system("df -h | awk '{print $3 $4}'")
	#print cmd

	fromaddr = emailadd
	#toaddr = "EMAIL ADDRESS YOU SEND TO"






	 
	msg = MIMEMultipart()
	## 
	msg['From'] = fromaddr

	msg['Subject'] = "Python email"
	## 
	body = "Size of server: " + bodyVal + " G"
	## 
	msg.attach(MIMEText(body, 'plain'))
	## 
	##filename = "NAME OF THE FILE WITH ITS EXTENSION"
	##attachment = open("PATH OF THE FILE", "rb")
	## 
	##part = MIMEBase('application', 'octet-stream')
	##part.set_payload((attachment).read())
	##encoders.encode_base64(part)
	##part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	## 
	##msg.attach(part)
	#print "memem"
	server = smtplib.SMTP_SSL(smtpserver, 465)
	#print "youyouyou"
	#server.ehlo()
	#server.starttls()
	#server.ehlo()
	#server.esmtp_features['auth'] = 'LOGIN PLAIN'
	server.set_debuglevel(1)

	server.login(emailadd[0:emailadd.index('@')], foo)
	text = msg.as_string()

	#print "youyou"

	for i in range(len(dirlist)):
	    strVal ='/home/' + dirlist[i] + "/mail/"
	    #print strVal
	    #print os.path.isdir(strVal)
	    
	    if(os.path.isdir(strVal) and val < 15):
		    #print "you"
		    toaddr = dirlist[i] + emailadd[emailadd.index('@'):len(emailadd)]
		    #print "to", toaddr

		    #s = smtplib.SMTP_SSL('localhost')
	    	    #s.send_message(text)

		    server.sendmail(fromaddr, toaddr, text)
		    msg['To'] = toaddr
		    print toaddr
	    
	print "me"

	server.quit()


if __name__ == '__main__':
    from optparse import OptionParser
    
    parser = OptionParser()
    
    parser.add_option("-f", "--foofoo", dest="foo", help="hello world", metavar="$1")
    parser.add_option("-e", "--email", dest="emailadd", help="sender email address", metavar="$2")
    parser.add_option("-s", "--smtpserver", dest="smtpserver", help="fqdn of serevr", metavar="$3")
    
    

    (options, args) = parser.parse_args()
    #print 'options: %s, args: %s' % (options, args)


    if not(options.foo or options.emailadd or options.smtpserver):
	print 'need this, really really need this'

    else:
    	fun(options.foo, options.emailadd, options.smtpserver)
    
    	
    	sys.exit(True)
