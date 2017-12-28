#!/usr/bin/python

import socket


host=raw_input("enter target ip: ")
port=input("enter target port: ")
buffer1=input("input first payload: ")

buffer2=input("input second payload: ")

buffer3=input("input third payload: ")

buffer = buffer1 + buffer2 + buffer3
#if raw_input == "quit":

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
  
print "[*]Sending evil buffer..."	
  
s.connect((host, port))	
data = s.recv(1024)
print data
s.send(buffer)
s.close()
print "\033[92m[*]Payload sent !"
