"""A proxy server that forwards requests from one port to another server.

To run this using Python 2.7:

% python proxy.py

It listens on a port (`LISTENING_PORT`, below) and forwards commands to the
server. The server is at `SERVER_ADDRESS`:`SERVER_PORT` below.
"""

# This code uses Python 2.7. These imports make the 2.7 code feel a lot closer
# to Python 3. (They're also good changes to the language!)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import library
import socket

# Where to find the server. This assumes it's running on the smae machine
# as the proxy, but on a different port.
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 7777

# The port that the proxy server is going to occupy. This could be the same
# as SERVER_PORT, but then you couldn't run the proxy and the server on the
# same machine.
LISTENING_PORT = 8888

# Cache values retrieved from the server for this long.
MAX_CACHE_AGE_SEC = 60.0  # 1 minute"""


def ForwardCommandToServer(command, server_addr, server_port):
    """Opens a TCP socket to the server, sends a command, and returns response.

    Args:
       command: A single line string command with no newlines in it.
       server_addr: A string with the name of the server to forward requests to.
       server_port: An int from 0 to 2^16 with the port the server is listening on.
    Returns:
       A single line string response with no newlines.
    """
    web_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    web_server_socket.connect((server_addr, server_port))
    web_server_socket.sendall(command)
    data = web_server_socket.recv(4096)
    
    # print("Data received is {}".format(data))
    return data

def ProxyClientCommand(client_socket, server_addr, server_port, cache):
    """Receives a command from a client and forwards it to a server:port.
    
     A single command is read from `sock`. That command is passed to the specified
    `server`:`port`. The response from the server is then passed back through
    `sock`.

    Args:
        sock: A TCP socket that connects to the client.
        server_addr: A string with the name of the server to forward requests to.
        server_port: An int from 0 to 2^16 with the port the server is listening on.
        cache: A KeyValueStore object that maintains a temorary cache.
        max_age_in_sec: float. Cached values older than this are re-retrieved from
        the server.
    """
    # Get the client's request/command
    request = library.ReadCommand(client_socket)
    cmd, name, text = library.ParseCommand(request)
     
    # Forward the request to the server and retrieve response
    data = ForwardCommandToServer(request, server_addr, server_port)
    
    # print("Data is here : {}".format(data))
    if cmd == "PUT":
        if name not in cache.Names():
            cache.StoreValue(name, text)
            client_socket.sendall('%s\n' % data)
        else:
            print("Key", name, "already exists")
            
    elif cmd == "GET":
        if name not in cache.Names():
            print("Key ", name, " does not exist")
        else:
            cache.GetValue(name, MAX_CACHE_AGE_SEC)
            client_socket.sendall('%s\n' % data)
            
    elif cmd == "DUMP":
        cache.Keys() 
        client_socket.sendall(data)
    
    client_socket.close()
    
def main():
    # Listen on a specified port...
    server_sock = library.CreateServerSocket(LISTENING_PORT)
    cache = library.KeyValueStore()
    # Accept incoming commands indefinitely.
    while True:
        # Wait until a client connects and then get a socket that connects to the
        # client.
        client_sock, (address, port) = library.ConnectClientToServer(server_sock)
        print('Received connection from %s:%d' % (address, port))
        ProxyClientCommand(client_sock, SERVER_ADDRESS, SERVER_PORT,cache)
        
main()