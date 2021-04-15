import socket
import threading
import pickle
soc = socket.socket()

soc.bind(("localhost", 5000))

soc.listen(5)

arrPos = {

}

def connectClient(con, index):
    while True:
        data = con.rect(1024)
        if not data:
            arrPos.pop(index)
            break

        obj = pickle.loads(data)
        arrPos[index] = obj
        con.send(pickle.dumps(arrPos))

    con.close()

i = 0
while True:
    con, ip = soc.accept()

    threading.Threand(target=connectClient, args=(con,)).start()
i += 1