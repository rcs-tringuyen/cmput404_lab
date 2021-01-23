#!/usr/bin/env python3
import socket 
from multiprocessing import Pool

HOST = ''
PORT = 8001
BUFFER_SIZE = 1024
host = 'www.google.com'
payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'

def connect(addr):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(addr)
		s.sendall(payload.encode())
		s.shutdown(socket.SHUT_WR)

		#receive the data from the proxy_end
		#althought the socket is shutdown, we still can listen from it, it's just not sending data 
		full_data = s.recv(BUFFER_SIZE)

		print(full_data)


	except Exception as e:
		print(e)

	finally:
		s.close()

def main():
	address = [(HOST, PORT)]
	with Pool() as p:
		p.map(connect, address*10)

if __name__ == "__main__":
	main()