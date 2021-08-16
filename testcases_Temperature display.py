#This is just an example of a testcase
#Vulnerability Name - Temperature display

import socket


soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

HOST_ADDR = '127.0.0.1'
HOST_PORT = 23456

def authenticate(pd, pwd):
    soc.sendto(b"AUTH %s" % pwd, ("127.0.0.1", pd))
    a, b = soc.recvfrom(1024)
    return a.strip()

def temp_test(val):
    try:
        incToken = authenticate(p, b"!Q#E%T&U8i6y4r2w")
        soc.sendto(b"%s;SET_DEGC" % incToken, ("127.0.0.1", val))
        soc.sendto(b"%s;GET_TEMP" % incToken, ("127.0.0.1", val))
        a, b = s.recvfrom(1024)
        c = float(a.decode("utf-8"))
        display_temp = c - 273
        assert(display_temp < -200)
    except Exception as e:
        print(e)
        assert(1 == 2)

