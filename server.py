#=================================================== file = server.py ======
#=  .2. Email protocol implementation. Server receives message from        =
#=  client, and displays upon receipt.                                     =
#===========================================================================
#=  Notes:                                                                 =
#=-------------------------------------------------------------------------=
#=-------------------------------------------------------------------------=
#=  Example output:                                                        =
#=  Received message from ('192.168.1.130', 57541)                         =
#=  Test Message                                                           =
#=-------------------------------------------------------------------------=
#=  Bugs: None known                                                       =
#=-------------------------------------------------------------------------=
#=  Build/Execute: python server.py                                        =
#=-------------------------------------------------------------------------=
#=  Authors: Anthony Cope & Matthew Weis                                   =
#=           University of South Florida                                   =                                  
#=           Email: anthonycope@mail.usf.edu & weis@mail.usf.edu           =
#=-------------------------------------------------------------------------=
#=  History: ADC (10/13/13) - Intial creation                              =
#=  History: ADC (11/10/13) - Finalized with UDP/TCP                       =
#===========================================================================
#----- Include files -------------------------------------------------------
import socket     
import time      

#===== Main program ========================================================

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
udpSocketRecv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocketSend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#source code from http:#www.tutorialspoint.com/python/python_networking.htm
host = socket.gethostname() 
port = 12345                #port for TCP
portUDPRecv = 23456			#port for receiving UDP message
portUDPSend = 34567			#port for sending UDP message

#source code from http:#www.tutorialspoint.com/python/python_networking.htm
tcpSocket.bind((host, port))                   
#source code from http:#www.tutorialspoint.com/python/python_networking.htm
udpSocketRecv.bind((host,portUDPRecv))

while True:
    #wait for UDP message and send ACK back to sender
    message, addr = udpSocketRecv.recvfrom(1024)
    #print message
    #print 'Received ACK request from', addr
    udpSocketSend.sendto('ACK', (addr[0], portUDPSend))

    #listen for TCP connection request
    tcpSocket.settimeout(2)
    tcpSocket.listen(5)

    try:
        #accept TCP request from sender and assign to socket
        clientSocket, addr = tcpSocket.accept()     #source code from http:#www.tutorialspoint.com/python/python_networking.htm
        clientSocket.settimeout(2)
        clientSocket.setblocking(1)

        #uses time to randomly generate 
        messageName = 'recv' + str(time.time()) + '.txt'
        outputFile = open(messageName, 'w')
        #loop based on example given at http://docs.python.org/2/library/socket.html
        while True:
            #receive message from sender 1024 bytes at a time and output to file
            message = clientSocket.recv(1024)   #maximum message size is 5000 chars, so 5000 bytes, should be a power of 2 so use 8192
            if message:
                #print message
                outputFile.write(message)
            else:
                break

        outputFile.close()
        print 'Received message from', addr

        #acknowledge message received and close socet
        clientSocket.send('Message Received') 
        clientSocket.close() 

    #reset loop if no TCP connection received
    except socket.timeout:
        print "TCP Connection timed out"

#close all sockets on exit        
tcpSocket.close()
udpSocketSend.close()
udpSocketRecv.close()

