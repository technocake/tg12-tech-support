#!/usr/bin/python
#coding: utf-8
import math, sys
import ping, sendmail
import time, random, datetime
from timer import Timer


def switchToInt(s):
	print s
	return (int(s.split('-')[0])-1)*4 + int(s.split('-')[1])

def intToSwitch(i):
	i-=1

	return "%s-%s" % ((i-(i%4))/4 +1 , i%4+1 )

def switchRange(S1, SN):
	return [range (switchToInt(S1), switchToInt(SN))]


def rowFromIp(sip):
	rawrow = int( sip.split('.')[-2] ) 
	return rawrow if rawrow %2 else rawrow-1

def switchFromIp(sip):
	[a,b] = [int(c) for c in sip.split('.')[-2:]]
	return "%s-%d" % ( 
		rowFromIp(sip), (2 * (0 if a%2 else 1) +  (0 if a == 1 else 1)) 
		)

R=78*4
count = 8
processing_time = 600000.00  #ms => 10min
FILTER = [a.strip() for a in open("switch-filter.txt").readlines()]

switches = []
switches_currently_being_processing  = {}


def mailAlert(to, sip):
	try:
		sendmail.sendMail(
		'Tech.Support@tg', 
		to, 

		"""Subject: Power down on row %s, switch (%s)\n\r
	
		Switch: %s at row %s is possible indicating a power surge!!\n\r\n\r""" % (rowFromIp(sip), switchFromIp(sip), switchFromIp(sip),rowFromIp(sip))
		)	
	except Exception as e:
		print e, ", Pidgeon did not fly!"


def SmokeSignal(s):
	#	Checking old incidence
	sys.stdout.write("%s " % datetime.datetime.now())
	try:
		for switch in switches_currently_being_processing.values():
			if not switch.timeLeft():
				del switches_currently_being_processing[switch]
	except Exception as e:
		print e
		print ("could not check processing loop")


	###		Not spamming if already being processed.
	if s in switches_currently_being_processing:
		print ( "Switch %s at row %s down, but already notified" % (s, rowFromIp(s)) )
		return

	switches_currently_being_processing[s] = Timer(processing_time)

	print "ROW %s \tPOWER DOWN!!!"%rowFromIp(s), s	
	mailAlert('jfrhammer@gmail.com')
	#mailAlert('orrebakken@gmail.com')
	#mailAlert('ANNAR')
	mailAlert('robin.garen@gmail.com')


#
#	Achimê!
#

print "MONITORING"


#	Building the switch-list (ip's to ping)
#	
for a in range(1, (R-1)/2):
	
	switch = "176.110.%d.%d" % ( 
 		int( math.floor( (a+1)/2 ) ), 
 		 
 			((a-1)%2)*(128)+1 
 	,) 
 	
	if not switch in FILTER: switches.append(switch)


################################
#	MONITORING
################################


try:
	while 1:
		for switch in switches:

			attempt = count
			testing = True

			#if  ping.do_one(switch, 0.5) == None: print "POWER DOWN!!!", switch  
			while testing and attempt:
				attempt -= 1
				try:
					if not ping.do_one(switch, 0.5) == None:
						testing = False
				except Exception as e:
					print "No Internetz", e

			if testing: SmokeSignal(switch)
		time.sleep(random.randrange(30))
except Exception as e:
	print e
finally:
	pass