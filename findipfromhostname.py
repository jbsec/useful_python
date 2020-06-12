# credit to code snail 

import socket

print("***Find IP address of hostname***")

hostname = input("Enter hostname")
IPAddr = socket.gethostbyname(hostname)
print("IP Address is:" + IPAddr)