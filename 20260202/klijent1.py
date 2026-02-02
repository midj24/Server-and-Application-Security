import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.connect(("localhost", 10013))

prviBroj = input(klijent.recv(256).decode("utf-8"))
klijent.send(bytes(prviBroj, "utf-8"))

DrugiBroj = input(klijent.recv(256).decode("utf-8"))
klijent.send(bytes(DrugiBroj, "utf-8"))
        #odgovor sa servera
print("Rezultat je:",klijent.recv(256).decode("utf-8"))