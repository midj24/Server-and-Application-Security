import socket
import time

#ovo je deo komunikacije
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(("127.0.0.1", 10013))
server.listen()
print("Server is listening...")
konekcija, adresa = server.accept()

print("Konekcija prihvacena od:", adresa)
time.sleep(2)

podaci = konekcija.recv(1024) #citanje dobijenih podataka od klijenta
dekodovani_podaci = podaci.decode("utf-8")
print("Stigli podaci od klijenta:", dekodovani_podaci)

time.sleep(2)

konekcija.close()
server.close()