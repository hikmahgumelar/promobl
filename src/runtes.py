from bs4 import BeautifulSoup
import requests

base_url = 'http://www.rajakamar.com/flight/search?depart=DPS&return=CGK&depart_date=2018-09-08&return_date=&roundtrip=0&adult=1&child=0&infant=1'
    # print(base_url)
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")



print(soup.find('h2', class_="title-tiket").text)
print(soup.find('div', class_="date-tiket").text)
hasil = soup.find_all('div', class_="flight-numbers") 
for nilai in hasil:
    print(nilai.text)
    nomor_penerbangan = nilai.find('div', class_="price-final")
    print(nomor_penerbangan)


