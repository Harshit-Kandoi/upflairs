# from datetime import datetime
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP
# # ip_address = "192.168.110.166"
# ip_address = "127.0.0.1"
# # default ip_address for your system = "127.0.0.1"
# port_no = 2525

# complete_address = (ip_address,port_no)
# s.bind(complete_address)

# print("I KNEW YOUR DARKEST SECRETS.....")

# while True:
#     receiver_file = open("receiver_message.txt","a")
#     message = s.recvfrom(100)
#     message_decoded = message.decode('ascii')
#     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     receiver_file.write(f"{timestamp} - {message_decoded}\n")
#     print(f" Receined message: {message.decode('ascii')}")

import socket
import datetime
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP - user datadram protocol
# ip_address = " 192.168.1.102"
ip_address = "192.168.110.166"   # for self
port_no = 2525

complete_address = (ip_address,port_no)

s.bind(complete_address)
print("HEY i am listening...")

while True:
    file=open("data.txt","a")
    message = s.recvfrom(1000)
    message1=message[0]
    message2=message1.decode("ascii")
    a=datetime.datetime.now()
    t=ip_address
    file.write("\n"+message2+"\t\t"+str(a)+"\t\t"+str(t))
    print(message2)
    file.close()