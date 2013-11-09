#=================================================== file = server.py ======
#=  .2. Email protocol implementation. Server receives message from        =
#=  client, and displays upon receipt.                                     =
#===========================================================================
#=  Notes:                                                                 =
#=    1) Input from input file "in.dat" to stdin (see example below)       =
#=        * Comments are bounded by "&" characters at the beginning and    =
#=          end of a comment block                                         =
#=    2) Output is to stdout                                               =
#=-------------------------------------------------------------------------=
#=-------------------------------------------------------------------------=
#= Example output (for above "in.dat"):                                    =
#=                                                                         =
#=   ---------------------------------------------- summary1.c -----       =
#=     Total of 11 values                                                  =
#=       Minimum  = 39.000000 (position = 6)                               =
#=       Maximum  = 61.000000 (position = 3)                               =
#=       Sum      = 561.000000                                             =
#=       Mean     = 51.000000                                              =
#=       Variance = 52.545455                                              =
#=       Std Dev  = 7.248824                                               =
#=       CoV      = 0.142134                                               =
#=   ---------------------------------------------------------------       =
#=-------------------------------------------------------------------------=
#=  Bugs: None known                                                       =
#=-------------------------------------------------------------------------=
#=  Build/Execute: python server.py                                        =
#=-------------------------------------------------------------------------=
#=  Authors: Anthony Cope & Matthew Weis                                   =
#=          University of South Florida                                    =                                  
#=          Email: anthonycope@mail.usf.edu & weis@mail.usf.edu            =
#=-------------------------------------------------------------------------=
#=  History: ADC (10/13/13) - Intial creation                              =
#===========================================================================
#----- Include files -------------------------------------------------------

#----- Defines -------------------------------------------------------------

#----- Global variables ----------------------------------------------------

#----- Function prototypes -------------------------------------------------

#===== Main program ========================================================

#!/usr/bin/python           # This is server.py file

#source code from http:#www.tutorialspoint.com/python/python_networking.htm

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #source code from http:#www.tutorialspoint.com/python/python_networking.htm
udpSocketRecv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocketSend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname() #source code from http:#www.tutorialspoint.com/python/python_networking.htm
port = 12345                #source code from http:#www.tutorialspoint.com/python/python_networking.htm
portUDPRecv = 23456			#port for receiving UDP message
portUDPSend = 34567			#port for sending UDP message
s.bind((host, port))        #source code from http:#www.tutorialspoint.com/python/python_networking.htm
#s.listen(5)                 #source code from http:#www.tutorialspoint.com/python/python_networking.htm
udpSocketRecv.bind((host,portUDPRecv))
#udpSocket.bind((()))

while True:

	message, addr = udpSocketRecv.recvfrom(8192)
	print message
	print 'Received message from', addr
	udpSocketSend.sendto('ACK', (host, portUDPSend))
	s.listen(5)
	c, addr = s.accept()     #source code from http:#www.tutorialspoint.com/python/python_networking.htm
	message = c.recv(8192)   #maximum message size is 5000 chars, so 5000 bytes, should be a power of 2 so use 8192
	print message
	print 'Received message from', addr
	c.send('Message Received')
	# s.close()
	# udpSocketSend.close()
	# udpSocketRecv.close()
	#exit()
	#break
