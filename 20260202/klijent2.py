import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.connect(("localhost", 10014))

godine = input(klijent.recv(32).decode("utf-8"))
klijent.send(bytes(godine, "utf-8"))

print("Server odgovorio:", klijent.recv(32).decode("utf-8"))

klijent.close()