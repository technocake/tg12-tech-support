#!/usr/bin/python
import locale
import curses
import time 

locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()


def go(one):
    curses.initscr()

    try:
        curses.cbreak()
        for i in range(4):
            time.sleep(1)
            curses.flash()
            print (chr(65+i))
        print( "Hello World" )
    finally:
        curses.endwin()



def main():
	curses.wrapper(go)


if __name__ == '__main__':
	main()
