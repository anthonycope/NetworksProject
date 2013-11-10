#client.py
#Anthony Cope and Matthew Weis

#=================================================== file = client.py ======
#=  .2. Email protocol implementation. Client sends message to server      =
#=   and displays upon receipt.                                     =
#===========================================================================
#=  Notes:                                                                 =
#=    1) Input from input file "in.dat" to stdin (see example below)       =
#=        * Comments are bounded by "&" characters at the beginning and    =
#=          end of a comment block                                         =
#=    2) Output is to stdout                                               =
#=-------------------------------------------------------------------------=
#=-------------------------------------------------------------------------=
#= Example output                                                          =
#=-------------------------------------------------------------------------=
#=  Bugs: None known                                                       =
#=-------------------------------------------------------------------------=
#=  Build/Execute: python client.py                                        =
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

#not sure if we have to put the ridiculous header here or not

#!/usr/bin/python           # This is client.py file


#source code from http://www.tutorialspoint.com/python/python_networking.htm
import socket               # Import socket module
import time                 # Import time module

#put in a menu with options for send/receive

def main():

    while True:
        print("(W)rite email or (E)xit")
        choice = raw_input()
        if choice.upper() == 'W':
            print 'Enter the IP Address of the recepient.'
            destinationAddress = raw_input()

            print 'Enter your e-mail message.'
            message = raw_input()   # gets e-mail contents from user

            send(message, destinationAddress)
        else:
            break

def send(message, destinationAddress):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #source code from http:#www.tutorialspoint.com/python/python_networking.htm
    host = socket.gethostname() #source code from http:#www.tutorialspoint.com/python/python_networking.htm
    udpSocketSend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocketRecv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 12345            #port for TCP
    portUDPSend = 23456     #port for sending UDP
    portUDPRecv = 34567     #port for receiving UDP 
    t_delay = 2             #amount of time after receiver comes online that message must be sent by
    t_offline = 5 * t_delay #amount of time until receiver deemed offline
    #s.bind((host,port))
    udpSocketRecv.bind((host,portUDPRecv))

    retryTime = 0 #Total amount time spent retrying
    sent = False

    #s.connect((host, port)) #source code from http://www.tutorialspoint.com/python/python_networking.htm
    #s.send(message)
    #print s.recv(1024)
    # s.close()
    # udpSocketRecv.close()
    # udpSocketSend.close()

    while retryTime < t_offline and not sent:

        try:            
            udpSocketRecv.setblocking(1)
            udpSocketRecv.settimeout(t_delay)
            udpSocketSend.sendto(message, (destinationAddress, portUDPSend))
            
            recvMessage, addr = udpSocketRecv.recvfrom(8192)
            print 'Received ACK from', addr
            udpSocketRecv.close()
            #break;
            s.connect((destinationAddress, port)) #source code from http://www.tutorialspoint.com/python/python_networking.htm
            s.send(message)
            #print s.recv(1024)
            sent = True
            print "Message Sent"

        except socket.timeout:
            print ("Timed out. Retry in {} seconds".format(t_delay))
            retryTime+= t_delay
            time.sleep(t_delay) 

        except socket.error as e:
            print str(e)
            print ("An error has occurred. Retry in {} seconds".format(t_delay))
            retryTime+= t_delay
            #udpSocketRecv.close()
            #udpSocketSend.close()
            #s.close()
            time.sleep(t_delay) 
       
    udpSocketRecv.close()
    udpSocketSend.close()
    s.close()      



        #     # try:
        #     #     s.settimeout(5) #Timeout occurs after 5 seconds
        #     #     s.connect((host, port)) #source code from http://www.tutorialspoint.com/python/python_networking.htm
        #     #     s.send(message)
        #     #     #t_offline = 10 seconds
        #     #     #if time > t_offline
        #     #         #

        #     #     print s.recv(1024)
        #     #     sent = True
        #     # except socket.error:
        #     #     print ("Recepient is offline. Retry in {} seconds".format(t_delay))
        #     #     retryTime+= t_delay
        #     #     s.close()
        #     #     time.sleep(t_delay)

        #     # except socket.timeout:
        #     #     print "Timed out"
        #     #     s.close()


if __name__ == "__main__":
    main()