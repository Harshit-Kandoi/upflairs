import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP
# ip_address = " 192.168.1.94"
ip_address = "127.0.0.1"
# default ip_address for your system = "127.0.0.1"
port_no = 2525

complete_address = (ip_address,port_no)
s.bind(complete_address)

print("I KNEW YOUR DARKEST SECRETS.....")
while True:
    message = s.recvfrom(100)
    print(message)