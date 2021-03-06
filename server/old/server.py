#!/usr/bin/env python

#ref: https://pymotw.com/2/socket/tcp.html

print("hello")

import socket
import sys


import signal


def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
#server_address = ('localhost', 10002)
server_address = ('10.0.0.41', 10006)
print("starting up on ",server_address[0]," port ",server_address[1])
sock.bind(server_address)


# Listen for incoming connections
sock.listen(1)

try:
	while True:
		# Wait for a connection
		print("waiting for a connection")
		connection, client_address = sock.accept()
		
		try:
			print("connection from:", client_address)
			hello_msg = "welcome client!"
			connection.sendall(hello_msg.encode())
			#connection.send(hello_msg.encode())
			
			# Receive the data in small chunks and retransmit it
			while True:
				data = connection.recv(16)
				print("received:",data)
				if data:
					print("sending data back to the client")
					connection.sendall(data)
				else:
					print("no more data from ", client_address)
					break
			
		finally:
			# Clean up the connection
			connection.close()

except KeyboardInterrupt:
	print("W: interrupt received, stopping…")
	connection.close()
          