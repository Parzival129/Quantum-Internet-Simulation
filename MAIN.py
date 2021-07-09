import time
import sys
import os
from rich.console import Console

c = Console()

print ("")
c.print ("  ██████╗       ███╗   ██╗███████╗████████╗", style = "purple")
c.print (" ██╔═══██╗      ████╗  ██║██╔════╝╚══██╔══╝", style = "purple")
c.print (" ██║   ██║█████╗██╔██╗ ██║█████╗     ██║   ", style = "purple")
c.print (" ██║▄▄ ██║╚════╝██║╚██╗██║██╔══╝     ██║   ", style = "purple")
c.print (" ╚██████╔╝      ██║ ╚████║███████╗   ██║   ", style = "purple")
c.print ("  ╚══▀▀═╝       ╚═╝  ╚═══╝╚══════╝   ╚═╝   ", style = "purple")
print (" Programmed By: Russell Tabata")
print ("")

print ("What would you like to send?")
print ("")
print ("1. HTML site")
print ("2. String message")
print ("")
option = input(">> ")

if option == "1":
    # put stiff for html
    os.system("python3 site_send.py")

elif option == "2":
    # put stuff for message
    os.system("python3 message_send.py")

else:
    print ("This is not a valid input!")
    
