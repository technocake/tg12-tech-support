#!/usr/bin/env python
# Simple mail script for testing an smtp server.
#	@author technocake
#	
#	28052011 technocake	made the initial version - based on the example from smtplib documentation
#	28052011 technocake	expanded it, made it python 3 compatible and added subject
#	28952911 tecnocake	Fixed Proper subject handling and added usage etc.
#
###################
import sys, re
import smtplib
SMTP_SERVER = "smtp.tg12.gathering.org"

def usage():
	return """
		Usage:	%s [file]

		if run without file argument, it will be ran in interactive mode;
		taking the from / to / subject / message from cli.

		If you provide a filename as the second argument, it will send the mail based on that file
		[NOT IMPLEMENTED YET]
		""" % (sys.argv[0],)


#in python 3, raw_input is renamed to input. In python v <3. input does something else.
def prompt(text):
        try:
                return raw_input(text)
        except:
                try:
                        return input(text)

                except:
                        exit()



def mailFromfile(filename):
	f = open(filename)



def mailFromCli():

	fromaddr = prompt("From: ")
	toaddrs  = prompt("To: ").split()
	subject = prompt("Subject: ")
	print "Enter message, end with ^D (Unix) or ^Z (Windows):"

	# Add the From: and To: headers at the start!
	msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
	       % (fromaddr, ", ".join(toaddrs), subject))

	while 1:
	    try:
        	line = prompt("")
	    except EOFError:
	        break
	    if not line:
	        break
	    if line == ".":
		break
	    msg = msg + line

	sendMail(fromaddr, toaddrs, msg)

def sendMail(fromaddr, toaddrs, msg):
	#print "Message length is " + repr(len(msg))
	server = smtplib.SMTP(SMTP_SERVER)
	server.set_debuglevel(0)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

if __name__=="__main__":
	print (usage())
	if not len(sys.argv) > 1:
		mailFromCli()
	else:
		mailFromFile(sys.argv[1])
