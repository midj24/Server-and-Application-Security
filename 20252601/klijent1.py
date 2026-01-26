import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

klijent.connect(("127.0.0.1", 10013))

klijent.sendall(b"Hello!")

klijent.close()