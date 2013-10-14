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

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

print 'Enter your e-mail message.'
message = raw_input()   # gets input from user

s.connect((host, port))
s.send(message)
#need error handling if receiver is offline
#t_delay = 2 seconds
#t_offline = 10 seconds
#if time > t_offline
    #

print s.recv(1024)
s.close()                     # Close the socket when done

