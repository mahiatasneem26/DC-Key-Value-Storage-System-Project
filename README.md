# DC-Key-Value-Storage-System-Project

This project introduces the concept of client/server architecture and caching. 
It is an implementation of a simple web and proxy server that stores and retrieves key-value pairs 
using socket programming interface. 

## Commands Permitted:
The server only permits commands such as GET, PUT, and DUMP in the request field followed by the key and value stored. 

  #### GET returns the value of the key specified 
  #### PUT stores the key and a specified value on the server 
  #### DUMP lists all of the key value pairs contained in the server. 


## Use of Proxy Server:
When the client makes a GET request, this request is passed through the proxy server. If the server has made the same request using the same key, the key-value pair is retrieved from the proxy server instead of the server. 
