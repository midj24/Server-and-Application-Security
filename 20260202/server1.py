import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 10013))
server.listen()


klijent, adresa = server.accept()
klijent.send(b"Unesite prvi broj: ")
PrviBroj = int(klijent.recv(32).decode("utf-8"))

klijent.send(b"Unesite drugi broj: ")
DrugiBroj = int(klijent.recv(32).decode("utf-8"))

rezultat = format(PrviBroj + DrugiBroj)
klijent.send(bytes(rezultat, "utf-8"))