#This is just an example of a testcase
#Vulnerability Name - Unencrypted Communications

import socket

soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

HOST_ADDR = '127.0.0.1'
HOST_PORT = 23456

def authenticate(pd, pwd):
    soc.sendto(b"AUTH %s" % pwd, ("127.0.0.1", pd))
    a, b = soc.recvfrom(1024)
    return a.strip()

def unencryptedTest(val):
    try:
        Tok = authenticate(val, b"!Q#E%T&U8i6y4r2w")
        soc.sendto(b"%s;GET_TEMP" % Tok, ("127.0.0.1", val))
        a, b = soc.recvfrom(1024)
        c = float(a.decode("utf-8"))
        assert (isinstance(c, float))
    except Exception as e:
        print(e)
        assert (1 == 2)

