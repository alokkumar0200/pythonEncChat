#!/usr/bin/python
from Crypto.Cipher import AES
import io
import socket
import sys
from os import system, name
from _thread import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
try:
    key = input(bcolors.OKGREEN + "[*] Enter Your Key For This Chat: " + bcolors.ENDC)
    IV = key = input(bcolors.OKGREEN + "[*] Enter Your IV This Chat: " + bcolors.ENDC)
except KeyboardInterrupt:
    sys.exit(0)

def encrypt(message):
	obj = AES.new(key, AES.MODE_CFB, IV)
	Ciphertext = obj.encrypt(message)
	return Ciphertext

def decrypt (message):
	obj = AES.new(key, AES.MODE_CFB, IV)
	return obj.decrypt(message)

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def threaded(c,addr):
	while True:
		data = c.recv(64 * 1024)
		data = decrypt(data)
		if not data:
			break
		print(bcolors.OKGREEN + "\n[*] Message from: " + str(addr[0]) + " " + data.decode('ascii') + bcolors.ENDC)
		data = input(bcolors.OKGREEN + "--> " + bcolors.ENDC)
		#data = encrypt(data)
		c.sendall(encrypt(data))
		print(bcolors.OKBLUE + "[*] Waiting for reply " + bcolors.ENDC)
	c.close()


def main():
    host = input(bcolors.OKGREEN + "[*] Enter Host Address: " + bcolors.ENDC)
    port = int(input(bcolors.OKGREEN + "[*] Enter Port Number: " + bcolors.ENDC))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    clear()
    print(bcolors.OKBLUE + "[*] Socket Bind Success. " + bcolors.ENDC)
    s.listen(5)
    print(bcolors.OKBLUE + "[*] Socket Listening For Connection" + bcolors.ENDC)
    print(bcolors.WARNING + "[*] Press Ctrl + C to exit" + bcolors.ENDC)	
    while True:
        try:
            c,addr = s.accept()
            print(bcolors.OKGREEN + "[*] Connected to: " +str(addr[0]) + " " + str(addr[1]) + bcolors.ENDC)
            start_new_thread(threaded, (c,addr,))
        except KeyboardInterrupt:
            s.send(encrypt("Server Disconnected!"))
            s.close()
            sys.exit(0)
    s.close()

if __name__ == '__main__':
	main()