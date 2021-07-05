# import many, many modules
import time
import os
import sys

# rich for pretty terminal stuff
from rich.console import Console
from rich.progress import track
from rich.table import Table
from rich.syntax import Syntax
from time import sleep

# qchat for communications
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
os.system("simulaqron start --nodes Alice,Bob,Eve")

# Initiate console var for pretty terminal
c = Console()
print ("")

# main function
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

        # Inputing html file to send
        print ("")
        file = input("html file to Send >> ")
        # Display file contents with syntax highlighting
        try:
            print ("")
            c.print ("SITE CONTENTS: ", style="blue")
            content = open(file, 'r').read()
            syntax = Syntax(content, "html", theme="monokai", line_numbers=True)
            c.print(syntax)           

        # Error handling if file does not exist          
        except:
            print ("Whoops! The file was not found!")

        # Send html file as string, with Super Dense Coding protocol
        alice_client.sendSuperDenseMessage("Bob", content)
        print ("")

        # Await messges being sent
        while True:
            messages = bob_client.getMessageHistory()
            
            if messages:

                # cool looking tasks list
                tasks = ["Generating Binary Array", "Constructing html list", "Displaying Info"]

                with c.status("[bold green]Working on processing...") as status:
                    while tasks:
                        task = tasks.pop(0)
                        if task == "Generating Binary Array":

                            # creating binary array from string
                            byte_msg = messages["Alice"][0]
                            string_msg = byte_msg.decode('UTF-8')
                            byte_array = bytearray(string_msg, 'utf8')
                            byte_list = []

                            for byte in byte_array:
                                binary_representation = bin(byte)
                                byte_list.append(binary_representation)
                    
                            c.log(f"{task} complete!")

                        elif task == "Constructing html list":
                            time.sleep(1)
                            c.log(f"{task} complete!")

                        elif task == "Displaying Info":
                            time.sleep(1)             
                            c.log(f"{task} complete!")
                print ("")
                def listToString(s):

                    str1 = ""
                    for ele in s:
                        str1 += ele
                    return str1
                    
                byte_info = listToString(byte_list)

                #c.print ("[BYTE] : " + byte_info, style = "green")
                #print ("")
                #c.print ("[STRING] : " + string_msg, style = "green")                
                #print ("") 

                # console table for displaying results
                table = Table(show_header=True, header_style="bold magenta")
                
                table.add_column("FORMAT")
                table.add_column("MESSAGE")

                table.add_row("Byte", byte_info)
                table.add_row("String", string_msg)
                c.print(table)

                # convert recieved string in html file
                lines = string_msg.split("\n")
                with open("recieved_file.html", "w") as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')

                # stoping quantum net
                os.system("simulaqron stop")
                # opening recieved html file in chromium
                os.system("chromium recieved_file.html")                    
                                
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
