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

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   message = c.recv(8192)   # maximum message size is 5000 chars, so 5000 bytes, should be a power of 2 so use 8192
   print message
   print 'Received message from', addr
   c.send('Thank you for connecting')
  # c.close()                # Close the connection