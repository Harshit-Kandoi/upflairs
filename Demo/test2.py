import socket
import datetime
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP - user datadram protocol
ip_address = " 192.168.1.97"
# ip_address = "127.0.01"  . # for self
port_no = 2525

complete_address = (ip_address,port_no)

s.bind(complete_address)
print("HEY i am listening...")

while True:
    file=open("data.txt","a")
    message = s.recvfrom(1000)
    message=message[0]
    message=message.decode("ascii")
    a=datetime.datetime.now()
    t=ip_address
    file.write("\n"+message+"\t\t"+str(a)+"\t\t"+str(t))
    print(message)
    file.close()
