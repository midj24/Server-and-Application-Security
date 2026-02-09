import requests

BASE_URL = "https://wizard-world-api.herokuapp.com"

houses_url = f"{BASE_URL}/houses" 

response = requests.get(houses_url)

print(response.status_code)
print(response.headers.get("Content-Type"))

podaci = response.json() 
print(podaci)

for kuca in podaci:
    trenutni_id = kuca["id"]
    print("Naziv kuce:", kuca["name"])
    
    # zahtev za detalje
    url = f"{BASE_URL}/houses/{trenutni_id}"

    odgovor = requests.get(url)
    detalji_kuce = odgovor.json()
    ocekivani_status_kod = 200
    
    print(ocekivani_status_kod == odgovor.status_code)

    print("***********")
    print("Detalji:")
    print("Boje:", detalji_kuce["houseColours"])
    print("Zivotinja:", detalji_kuce["animal"])
    print("######################################")


    