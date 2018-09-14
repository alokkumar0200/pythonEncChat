#!/usr/share/python
from Crypto.Cipher import AES
import io
import socket
import sys
import os

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
    if os.name == 'nt':
        _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def main():
    host = input(bcolors.OKGREEN + "[*] Enter Host Address: " + bcolors.ENDC)
    port = int(input(bcolors.OKGREEN + "[*] Enter Port Number: " + bcolors.ENDC))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    clear()
    print(bcolors.OKBLUE + "[*] Connected to server." + bcolors.ENDC)
    print(bcolors.WARNING + "[*] Press Ctrl + C  or 'q' to exit" + bcolors.ENDC)

    while True:
        try:
            message = input(bcolors.OKGREEN + "--> " + bcolors.ENDC)
            if message == 'Q' or message == 'q':
                break
            s.send(encrypt(message))
            print(bcolors.OKBLUE + "[*] Waiting for reply " + bcolors.ENDC)
            data = s.recv(64 * 1024)
            data = decrypt(data)
            print(bcolors.OKGREEN + "\n[*] Message from Server: " + data.decode('ascii') + bcolors.ENDC)
        except KeyboardInterrupt:
        	break
    s.send(encrypt("Client Disconnected!"))
    s.close()


if __name__ == '__main__':
    main()
