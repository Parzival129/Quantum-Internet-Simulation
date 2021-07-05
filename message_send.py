import time
import os
from rich.console import Console
from rich.progress import track
from rich.table import Table
from time import sleep
 
from qchat.client import QChatClient
from qchat.server import QChatServer
from cqc.pythonLib import CQCConnection

"""
SuperDense coding messaging of 
different kinds of media
"""
# Cool looking bar

for step in track(range(100), description="Booting up Q-NET : "):
    sleep(0.01)

c = Console()
print ("")

def main():
    # Create Simulaqron connections for each component
    with CQCConnection(name="Alice") as cqc_alice, CQCConnection(name="Bob") as cqc_bob, \
            CQCConnection(name="Eve") as cqc_eve:

        # Start up root server
        root = QChatServer(name="Eve", cqc_connection=cqc_eve)
        # time.sleep(2)

        # Start up users
        alice_client = QChatClient(name="Alice", cqc_connection=cqc_alice)
        bob_client = QChatClient(name="Bob", cqc_connection=cqc_bob)
        time.sleep(1)

        # Send a superdense coded message

        msg = input("Message to Send >> ")
        
        c.print ("Sending message: " + msg, style = "green")
        print ("")
        alice_client.sendSuperDenseMessage("Bob", msg)

        while True:
            messages = bob_client.getMessageHistory()
            if messages:
                
                byte_msg = messages["Alice"][0]
                string_msg = byte_msg.decode('UTF-8')
                byte_array = bytearray(string_msg, 'utf8')
                byte_list = []

                for byte in byte_array:
                    binary_representation = bin(byte)
                    byte_list.append(binary_representation)
                    
                print ("")

                def listToString(s):

                    str1 = ""
                    for ele in s:
                        str1 += ele
                    return str1
                    
                byte_info = listToString(byte_list)

                c.print ("[BYTE] : " + byte_info, style = "green")
                print ("")
                c.print ("[STRING] : " + string_msg, style = "green")                
                print ("")                
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("FORMAT")
                table.add_column("MESSAGE")

                table.add_row("Byte", byte_info)
                table.add_row("String", string_msg)
                c.print(table)
                
                break
                
            # time.sleep(1)

#        bob_client.sendSuperDenseMessage("Alice", "Hello to you too!")

#        while True:
#            messages = alice_client.getMessageHistory()
#            if messages:
#                print("[Alice] : Got messages!: {}".format(messages))
#                break
            # time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except:
        c.print_exception()
