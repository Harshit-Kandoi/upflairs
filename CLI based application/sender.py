import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP

# target_ip = "192.168.1.64"
target_ip = "127.0.0.1"
target_port = 2525

while True:
    message = input("plz enter your message : ")
    message = message.encode('ascii')
    s.sendto(message,(target_ip , target_port))
    print("your secret has been leaked! ")