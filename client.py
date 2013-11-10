#=================================================== file = client.py ======
#=  .2. Email protocol implementation. Client sends message to server      =
#=   and displays upon receipt.                                            =
#===========================================================================
#=  Notes:                                                                 =
#=-------------------------------------------------------------------------=
#=  Example output:                                                        =
#=  (W)rite email or (E)xit                                                =
#=  w                                                                      =
#=  Enter the IP Address of the recepient.                                 =
#=  192.168.1.130                                                          =
#=  Enter your e-mail message.                                             =
#=  test                                                                   =
#=  Message Sent                                                           =
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
#=  History: ADC (11/10/13) - Finalized with UDP/TCP                       =
#===========================================================================
#----- Include files -------------------------------------------------------
import socket               
import time               

#===== Main program ========================================================

#not sure if we have to put the ridiculous header here or not

#!/usr/bin/python           # This is client.py file

def main():

    while True:

        #determine whether to compose email or exit program
        print("(W)rite email or (E)xit")
        choice = raw_input()

        # if user enters w, input IP address and message
        if choice.upper() == 'W':
            print 'Enter the IP Address of the recepient.'
            destinationAddress = raw_input()

            print 'Enter your e-mail message.'
            message = raw_input() 

            #call send function
            send(message, destinationAddress)
        else:
            break

#=============================================================================
# Function to send a message to a specified IP address                       =
#-----------------------------------------------------------------------------
# Inputs: message, the message to be sent, and destinationAdress, IP address =
#         that message will be sent to                                       =
# Returns: Nothing, message will be sent if successful, output error if not  =
#=============================================================================
def send(message, destinationAddress):
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udpSocketSend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocketRecv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #source code from http:#www.tutorialspoint.com/python/python_networking.htm
    host = socket.gethostname() 
    port = 12345            #port for TCP
    portUDPSend = 23456     #port for sending UDP
    portUDPRecv = 34567     #port for receiving UDP 
    t_delay = 2             #amount of time after receiver comes online 
    t_offline = 5 * t_delay #amount of time until receiver deemed offline
    retryTime = 0 #Total amount time spent retrying
    sent = False

    #bind socket for receiving ACKs
    udpSocketRecv.bind((host,portUDPRecv))

    #Try to send message until a set amount of time has passed
    while retryTime < t_offline and not sent:

        try:         
            #set blocking and timeout for socket, then send UDP message   
            udpSocketRecv.setblocking(1)
            udpSocketRecv.settimeout(t_delay)
            udpSocketSend.sendto(message, (destinationAddress, portUDPSend))
            
            #source code from http://www.tutorialspoint.com/python/python_networking.htm
            #receive ACK from receiver and close socket
            recvMessage, addr = udpSocketRecv.recvfrom(8192)
            #print 'Received ACK from', addr
            udpSocketRecv.close()

            #break;

            #source code from http://www.tutorialspoint.com/python/python_networking.htm
            #create TCP connection to receiver and send message
            tcpSocket.connect((destinationAddress, port)) 
            tcpSocket.send(message)
            #print tcpSocket.recv(1024)
            sent = True
            print "Message Sent"

        #if there is a timeout, retry in t_delay seconds
        except socket.timeout:
            print ("Timed out. Retry in {} seconds".format(t_delay))
            retryTime+= t_delay
            time.sleep(t_delay) 

        #if another error has occurred, retry in t_delay seconds
        except socket.error as e:
            print str(e)
            print ("An error has occurred. Retry in {} seconds".format(t_delay))
            retryTime+= t_delay
            time.sleep(t_delay) 
       
    #close all sockets
    udpSocketRecv.close()
    udpSocketSend.close()
    tcpSocket.close()      

if __name__ == "__main__":
    main()