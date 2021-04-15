import socket
import pickle
import threading
soc = socket.socket()

soc.bind(("localhost", 5000))

soc.listen(100)

def clientUser():
    while True:
        data = conn.recv(2048)
        print(data)
        if not data:
            break
        if obj["z"] == "+":
            a = int(obj["one"]) + int(pbj["two"])
            coon.cend(a.encode())
        if obj["z"] == "-":
            a = int(obj["one"]) - int(pbj["two"])
            coon.cend(a.encode())
        if obj["z"] == "/":
            a = int(obj["one"]) // int(pbj["two"])

    conn.close()

while True:
    conn, addr = soc.accept()
    print(addr)
    threading.Thread(tarjet=clienUser, args=(conn,))





