import socket
import time



target_ip = input("Enter Targets Ip Address : ")

n = int(input("Enter Starting Port : "))
n2 = int(input("Enter Ending Port : "))


for i in range(n,n2):
    start_time = time.time()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connect = s.connect_ex((target_ip,6666))

    if connect == 0:
        print("Port {} is open".format(i))
    
    else:
        print("Port {} is closed".format(i))
    
    s.close()

    print("Time Taken : {}".format(time.time() - start_time))

