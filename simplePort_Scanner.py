#!/bin/python3

import sys
import socket
from datetime import datetime

#Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
   
else:
      print("Invalid amount of arguments")
      print("Syntax: error")

#Banner
print("-" * 50)
print("Scanning Started " +target)
print("Time Started: "+str(datetime.now()))
print("-" * 50)

try:
      for port in range (20,100):
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          socket.setdefaulttimeout(1)
          result = s.connect_ex((target,port))
          if result == 0:
               print("Port {} is open".format(port))
     
      s.close()
     

except KeyboardInterrupt:
       print("\nExiting program")
       sys.exit()
       
except socket.gaierror:
       print("Hostname could not be resplved")
       sys.exit()
       
except socket.error:
       print("Could not connect to the server")
       sys.exit()
