# Lab 2

## Sockets

- Create a github repository for this lab and initialize a clean Python3 virtual environment.

- Make a file called client.py which uses the socket library to connect to www.google.com and requests a page.

- Make your program output whatever was sent to it onto the terminal.

### Question 1: How do you specify a TCP socket in Python?
- You use `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
-------------------------------------------------------------

- Make a file called echo_server.py that listens for incoming connections and echos any received data.

- Test echoing example: $ echo "Foobar" | nc localhost 8001 -q 1 should return Foobar, provided the port used is 8001

### Question 2: What is the difference between a client socket and a server socket in Python?
- Client socket created to connect and listen to a server while the server socket created to bind onto a port and listen for connection from a client.
-------------------------------------------------------------

- Print out information about what is connected to the server socket to the terminal.

### Question 3: How do we instruct the OS to let us reuse the same bind port?
- We use `setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`. `SO_REUSEADDR` is to force bind to a port in use by another socket. Any value other than 0 is 'yes'
-------------------------------------------------------------

### Question 4: What information do we get about incoming connections?
- We get the address of the client and the connection port.
-------------------------------------------------------------

- Print out whatever is sent to your server program.

### Question 5: What is returned by recv() from the server after it is done sending the HTTP request?
- Return the value of the message from the server.
-------------------------------------------------------------

- Create a file called proxy_server.py and connect to Google. Create a file called proxy_client.py and connect to your proxy server.

- Forward whatever is received on the server socket to www.google.com. Take the response from www.google.com and send it to the original connection.

- Make your proxy server and echo server forking so multiple programs can use it simultaneously.

- Push your code to GitHub.

### Question 6: Provide a link to your code on GitHub.
- https://github.com/rcs-tringuyen/cmput404_lab/tree/main/Lab2
