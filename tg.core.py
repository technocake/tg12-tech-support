#!/usr/bin/python

def switchToInt(s):
	print s
	return (int(s.split('-')[0])-1)*4 + int(s.split('-')[1])

def intToSwitch(i):
	i-=1

	return "%s-%s" % ((i-(i%4))/4 +1 , i%4+1 )

def switchRange(S1, SN):
	return [switch for switch in range (switchToInt(S1), switchToInt(SN))]


def rowFromIp(sip):
	rawrow = int( sip.split('.')[-2] ) 
	return rawrow if rawrow %2 else rawrow-1



def main():
	print intToSwitch(switchToInt("3-2"))
	print rowFromIp("176.110.11.1")
	print rowFromIp("176.110.32.129")

if __name__ == '__main__':
	main()


R=84

FILTER = switchRange("26-1", "42-4")

print [intToSwitch(i) for i in range(1, R*2-1) if not i in FILTER]
