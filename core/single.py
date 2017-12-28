#!/usr/bin/python

import socket


host=raw_input("enter target ip: ")
port=input("enter target port: ")
buffer1=input("enter your payload: ")



buffer = buffer1
#if raw_input == "quit":

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
  
print "[*]Sending evil buffer..."	
  
s.connect((host, port))	
data = s.recv(1024)
print data
s.send(buffer)
s.close()
print "\033[92m[*]Payload sent !"
