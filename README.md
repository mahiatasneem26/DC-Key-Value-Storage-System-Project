# DC-Key-Value-Storage-System-Project

This project introduces the concept of client/server architecture and caching. 
It is an implementation of a simple web and proxy server that stores and retrieves key-value pairs 
using socket programming interface. 

## Commands Permitted:
The server only permits commands such as GET, PUT, and DUMP in the request field followed by the key and value stored. 

#### GET returns the value of the key specified if it is not older than 60 seconds
#### PUT stores the key and a specified value on the server 
#### DUMP lists all of the key value pairs contained in the server. 


## Use of Proxy Server:
When the client makes a GET request, this request is passed through the proxy server. If the server has made the same request using the same key, the key-value pair is retrieved from the proxy server instead of the server. 

## Connecting to the Server via a Client
To establish a connection with the server:
#### 1. Install telnet. 
#### 2. Run server.py and proxy.py on separate terminal shells ( python server.py and python proxy.py )
#### 3. Open a terminal and connect to the client using the command : telnet localhost <port#> ( Port# should be 7777 to connect directly to the web server and 8888 to connect to the web server via the proxy server )
