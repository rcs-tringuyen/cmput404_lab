#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()

            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()

            print("Started process ", p)

"""We basically move the while loop of the echo_server.py down to this function. 
In the while loop, we replace it with the multiprocessing handler"""
def handle_echo(addr, conn):
    conn, addr = s.accept()
    print("Connected by", addr)

    #recieve data, wait a bit, then send it back
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    #RDWR means disable further send & receive operation
    #WR means disable further send  operation
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == "__main__":
    main()