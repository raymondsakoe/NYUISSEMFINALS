#This is just an example of a testcase
#Vulnerability Name - same Password

import socket


soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

HOST_ADDR = '127.0.0.1'
HOST_PORT = 23456

def authenticate(pd, pwd):
    soc.sendto(b"AUTH %s" % pwd, ("127.0.0.1", pd))
    a, b = soc.recvfrom(1024)
    return a.strip()

def passTest(pass0, pass1):
    try:
        Tok1 = authenticate(pass0, b"!Q#E%T&U8i6y4r2w")
        Tok2 = authenticate(pass1, b"!Q#E%T&U8i6y4r2w")
        assert(Tok1 and Tok2)
    except Exception as ee:
        print(ee)
        assert (1 == 2)

