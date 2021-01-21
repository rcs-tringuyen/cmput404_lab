#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

#referrence from client.py
def get_remote_ip(host):
	print(f'Getting IP for {host}')
	try:
		remote_ip = socket.gethostbyname( host )
	except socket.gaierror:
		print ('Hostname could not be resolved. Exiting')
		sys.exit()

	print (f'Ip address of {host} is {remote_ip}')
	return remote_ip

def main():
	host = 'www.google.com'
	port = 80
	#referrence from echo_server.py
	#this basically listen to the local port on your computer
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
		print('Starting proxy server')
		proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		proxy_start.bind((HOST, PORT))
		#set to listening, queue of pending connection is 1
		proxy_start.listen(1)
		while True:
			conn, addr = proxy_start.accept()
			#this should be your localhost
			print("Connected by ", addr)
			#this part is to connect with google's end
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
				#find out google's ip
				remote_ip = get_remote_ip(host)

				#connect to google's ip at port 80 which is the HTTP port
				proxy_end.connect((remote_ip, port))
				#grabbing the data from the client, then send it to google
				send_full_data = conn.recv(BUFFER_SIZE)
				print(f"Sending recieved data {send_full_data} to google")
				proxy_end.sendall(send_full_data)
				proxy_end.shutdown(socket.SHUT_WR)

				#now grabbing the data from google, sending it back to the client
				data = proxy_end.recv(BUFFER_SIZE)
				print(f'Sending recieved data {data} to client')
				conn.sendall(data)

			conn.close()
if __name__ == "__main__":
    main()

