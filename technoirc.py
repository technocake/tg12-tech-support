#!/usr/bin/python
#coding: utf-8
import socket,time, threading

class PidgeonBot:

   def __init__(self, nick, channel):
      network = 'irc.homelien.no'
      port = 6667
      irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
      irc.connect ( ( network, port ) )

      print irc.recv(4096)

      irc.send ( 'NICK %s\r\n' % nick) 
      irc.send ( 'USER %s %s %s :Tech:Support @ TG on IRC\r\n' % (nick, nick, nick))
      irc.send ( 'JOIN #%s\r\n' % channel)
   
      self.irc = irc
      self.channel = channel
      self.nick = nick


   def fly(self, msg):
      self.irc.send('PRIVMSG #%s :%s' % (self.channel, msg))

   def returnHomeWithMessage(self):
      letter = self.irc.recv(4096)
      return letter

def waitSome():
   while True:
      data = irc.recv ( 4096 )
      if data.find ( 'PING' ) != -1:
         irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
      if data.find ( 'slaps botty' ) != -1:
         irc.send ( 'PRIVMSG #paul :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
      print data

def main():
   pidgeon = PidgeonBot('TGpidgeon', 'technocake')
   pidgeon.fly('Some onions has arrived')
   print pidgeon.returnHomeWithMessage()
   threading.Thread(target=waitSome)




if __name__ == '__main__':
   main()