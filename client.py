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

    #print("(W)rite email or (R)ead latest message")
    #choice = raw_input()
    #if choice == 'W':
    print 'Enter your e-mail message.'
    message = raw_input()   # gets input from user
    send(message)

def send(message):
    s = socket.socket()         #source code from http:#www.tutorialspoint.com/python/python_networking.htm
    host = socket.gethostname() #source code from http:#www.tutorialspoint.com/python/python_networking.htm
    port = 12345                #source code from http:#www.tutorialspoint.com/python/python_networking.htm
    t_delay = 2 #amount of time after receiver comes online that message must be sent by
    t_offline = 5 * t_delay #amount of time until receiver deemed offline


    retryTime = 0 #Total amount time spent retrying
    sent = False
    while retryTime < t_offline and not sent:

        try:
            s.settimeout(5) #Timeout occurs after 5 seconds
            s.connect((host, port)) #source code from http://www.tutorialspoint.com/python/python_networking.htm
            s.send(message)
            #t_offline = 10 seconds
            #if time > t_offline
                #

            print s.recv(1024)
            sent = True
        except socket.error:
            print ("Recepient is offline. Retry in {} seconds".format(t_delay))
            retryTime+= t_delay
            s.close()
            time.sleep(t_delay)

        except socket.timeout:
            print "Timed out"
            s.close()


if __name__ == "__main__":
    main()

