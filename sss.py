import socket

z = input("Знак: ")
one = input("Первое число")
two = input("Второе число")

sendObj = {
    "z": z,
    "one": one,
    "two": two
}

soc = socket.socket()

soc.connect(("localhost", 5000))

soc.send(pickle.dumrs(sendObj))
data = soc.recv(1024)

print(data)
