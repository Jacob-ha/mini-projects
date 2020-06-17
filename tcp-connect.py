
import socket


# set target host
t_host = 'google.com' #change to any host that's valid

# set target port
t_port = 80 #change to any port that's valid

# create the connecting client
connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client 
connector.connect((t_host, t_port))

# send whatever data ;)
connector.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #change site to the host

# did they accept you? check your recieving data ;)
am_i_worthy = connector.recv(1337)

print(am_i_worthy)
