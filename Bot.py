from bs4 import BeautifulSoup
from dotenv import load_dotenv
import re
import time
import os
import requests
load_dotenv()

HEADER = {'User-Agent': 'Mozilla / 5.0 (iPhone; CPU iPhone OS 10_3 come Mac OS X) AppleWebKit / 602.1.50 (KHTML, come Gecko) CriOS / 56.0.2924.75 Mobile / 14E5239e Safari / 602.1 RuxitSynthetic / 1.0 v8266421968 t1099441676816697146 ath9b965f92 altp ='}
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
BASE_URL_1 = 'https://www.idealo.it/confronta-prezzi/'
BASE_URL_2 = 'https://www.trovaprezzi.it/'
BASE_URL_3 = 'https://www.amazon.it/'

print('Inviando')
print('.')
testo_inizio = "⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️"
print('.')
i = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_inizio}')
print('.')
print('Inviato!')

print('Inviando')
ora = time.strftime("%H:%M:%S")
print('.')
data = time.strftime("%d/%m/%Y")
print('.')
testo_tempo = "Sono le " + ora + " del " + data + ", quindi:"
print('.')
t = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_tempo}')
print('Inviato!')

def main(event={}, context={}):
    name = 'Intel Core i5-10600K'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '200332057/intel-core-i5-10600k-box-socket-1200-14nm-bx8070110600k.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result1_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_1_1 = result1_1[0] + '.' + result1_1[1]
    prezzo_virgola_1_1 =result1_1[0] + ',' + result1_1[1]
    print('.')
    print (prezzo_virgola_1_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'prezzo_processori_i_5_10600k.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', style= "white-space:nowrap").text
    print('.')
    result1_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_1_2 = result1_2[0] + '.' + result1_2[1]
    prezzo_virgola_1_2 =result1_2[0] + ',' + result1_2[1]
    print('.')
    print (prezzo_virgola_1_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Intel-Core-i5-10600K-attacco-LGA1200/dp/B0883NTLXM/ref=pd_sbs_5?pd_rd_w=WFz8m&pf_rd_p=467d4f56-31c8-431b-b939-b3298e95b84d&pf_rd_r=8A05BVXPZGZ7QC6A13K2&pd_rd_r=0cacb9a2-1ebf-4ef8-954d-f9a4f6860b82&pd_rd_wg=XM3rv&pd_rd_i=B0883NTLXM&psc=1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result1_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_1_3 = result1_3[0] + '.' + result1_3[1]
    prezzo_virgola_1_3 =result1_3[0] + ',' + result1_3[1]
    print('.')
    print (prezzo_virgola_1_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo1 = min (prezzo_finale_1_1, prezzo_finale_1_2, prezzo_finale_1_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo1 + ' €')
    print('Inviato!')
    
    database1 = open ("Minimi1.txt", "r").read()
    lista1 = re.findall(r'\b\d+\b', database1)
    risultato1 = lista1[-2] + '.' + lista1[-1]
    risultato_virgola1 = lista1[-2] + ',' + lista1[-1]
    
    if minimo1 == risultato1:
        andamento1 = '😴 (fermo)'
    elif minimo1 < risultato1:
        andamento1 = '📉 (sta calando da ' + risultato_virgola1 + ' €)'
    else:
        andamento1 = '📈 (sta salendo da ' + risultato_virgola1 + ' €)'
    
    testo_messaggio1_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_1_1 + ' €' + "*" + " su Idealo " + "\n" + andamento1
    testo_messaggio1_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_1_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento1
    testo_messaggio1_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_1_3 + ' €' + "*" + " su Amazon " + "\n" + andamento1
    
    if prezzo_finale_1_3 == minimo1:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio1_3}')
    elif prezzo_finale_1_1 == minimo1:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio1_1}')
    else:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio1_2}')
    
    database1 = open ("Minimi1.txt", "a")
    database1.write ("\n" + minimo1)
    database1.close ()
    
    time.sleep(3)

if __name__ == '__main__':
    main()

def main(event={}, context={}):
    name = 'Intel Core i7-10700K'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '200331878/intel-core-i7-10700k.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result2_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_2_1 = result2_1[0] + '.' + result2_1[1]
    prezzo_virgola_2_1 =result2_1[0] + ',' + result2_1[1]
    print('.')
    print (prezzo_virgola_2_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'prezzo_processori_i_7_10700k.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', style= "white-space:nowrap").text
    print('.')
    result2_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_2_2 = result2_2[0] + '.' + result2_2[1]
    prezzo_virgola_2_2 =result2_2[0] + ',' + result2_2[1]
    print('.')
    print (prezzo_virgola_2_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Intel-Core-i7-10700K-attacco-LGA1200/dp/B0883P8CNM/ref=sr_1_1?__mk_it_IT=ÅMÅŽÕÑ&crid=19V4V2PJ3FTQ&dchild=1&keywords=i7+10700k&qid=1610974971&sprefix=i7+%2Caps%2C389&sr=8-1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result2_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_2_3 = result2_3[0] + '.' + result2_3[1]
    prezzo_virgola_2_3 =result2_3[0] + ',' + result2_3[1]
    print('.')
    print (prezzo_virgola_2_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo2 = min (prezzo_finale_2_1, prezzo_finale_2_2, prezzo_finale_2_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo2 + ' €')
    print('Inviato!')
    
    database2 = open ("Minimi2.txt", "r").read()
    lista2 = re.findall(r'\b\d+\b', database2)
    risultato2 = lista2[-2] + '.' + lista2[-1]
    risultato_virgola2 = lista2[-2] + ',' + lista2[-1]
    
    if minimo2 == risultato2:
        andamento2 = '😴 (fermo)'
    elif minimo2 < risultato2:
        andamento2 = '📉 (sta calando da ' + risultato_virgola2 + ' €)'
    else:
        andamento2 = '📈 (sta salendo da ' + risultato_virgola2 + ' €)'
    
    testo_messaggio2_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_2_1 + ' €' + "*" + " su Idealo " + "\n" + andamento2
    testo_messaggio2_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_2_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento2
    testo_messaggio2_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_2_3 + ' €' + "*" + " su Amazon " + "\n" + andamento2
    
    if prezzo_finale_2_3 == minimo2:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio2_3}')
    elif prezzo_finale_2_1 == minimo2:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio2_1}')
    else:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio2_2}')
    
    database2 = open ("Minimi2.txt", "a")
    database2.write ("\n" + minimo2)
    database2.close ()
    
    time.sleep(3)

if __name__ == '__main__':
    main()

def main(event={}, context={}):
    name = 'Intel Core i9-10900K'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '200329896/intel-core-i9-10900k.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result3_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_3_1 = result3_1[0] + '.' + result3_1[1]
    prezzo_virgola_3_1 =result3_1[0] + ',' + result3_1[1]
    print('.')
    print (prezzo_virgola_3_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'prezzo_processori_i_9_10900k.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', style= "white-space:nowrap").text
    print('.')
    result3_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_3_2 = result3_2[0] + '.' + result3_2[1]
    prezzo_virgola_3_2 =result3_2[0] + ',' + result3_2[1]
    print('.')
    print (prezzo_virgola_3_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Intel-BX8070110900K-Core-i9-10900K-fase/dp/B0883NZC43'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result3_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_3_3 = result3_3[0] + '.' + result3_3[1]
    prezzo_virgola_3_3 =result3_3[0] + ',' + result3_3[1]
    print('.')
    print (prezzo_virgola_3_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo3 = min (prezzo_finale_3_1, prezzo_finale_3_2, prezzo_finale_3_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo3 + ' €')
    print('Inviato!')
    
    database3 = open ("Minimi3.txt", "r").read()
    lista3 = re.findall(r'\b\d+\b', database3)
    risultato3 = lista3[-2] + '.' + lista3[-1]
    risultato_virgola3 = lista3[-2] + ',' + lista3[-1]
    
    if minimo3 == risultato3:
        andamento3 = '😴 (fermo)'
    elif minimo3 < risultato3:
        andamento3 = '📉 (sta calando da ' + risultato_virgola3 + ' €)'
    else:
        andamento3 = '📈 (sta salendo da ' + risultato_virgola3 + ' €)'
    
    testo_messaggio3_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_3_1 + ' €' + "*" + " su Idealo " + "\n" + andamento3
    testo_messaggio3_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_3_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento3
    testo_messaggio3_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_3_3 + ' €' + "*" + " su Amazon " + "\n" + andamento3
    
    if prezzo_finale_3_3 == minimo3:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio3_3}')
    elif prezzo_finale_3_1 == minimo3:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio3_1}')
    else:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio3_2}')
    
    database3 = open ("Minimi3.txt", "a")
    database3.write ("\n" + minimo3)
    database3.close ()  
    
    time.sleep(3)

if __name__ == '__main__':
    main()

def main(event={}, context={}):
    name = 'MSI MPG Z490 Gaming Plus'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '200295282/msi-mpg-z490-gaming-plus.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result4_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_4_1 = result4_1[0] + '.' + result4_1[1]
    prezzo_virgola_4_1 =result4_1[0] + ',' + result4_1[1]
    print('.')
    print (prezzo_virgola_4_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'schede-madri/prezzi-scheda-prodotto/msi_mpg_z490_gaming_plus-v'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "price_range").text
    print('.')
    result4_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_4_2 = result4_2[0] + '.' + result4_2[1]
    prezzo_virgola_4_2 =result4_2[0] + ',' + result4_2[1]
    print('.')
    print (prezzo_virgola_4_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'MSI-Z490-GAMING-PLUS-S-1200/dp/B0886QSX7N/ref=sr_1_1?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=MSI+MPG+Z490+Gaming+Plus&qid=1611044080&sr=8-1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result4_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_4_3 = result4_3[0] + '.' + result4_3[1]
    prezzo_virgola_4_3 =result4_3[0] + ',' + result4_3[1]
    print('.')
    print (prezzo_virgola_4_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo4 = min (prezzo_finale_4_1, prezzo_finale_4_2, prezzo_finale_4_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo4 + ' €')
    print('Inviato!')
    
    database4 = open ("Minimi4.txt", "r").read()
    lista4 = re.findall(r'\b\d+\b', database4)
    risultato4 = lista4[-2] + '.' + lista4[-1]
    risultato_virgola4 = lista4[-2] + ',' + lista4[-1]
    
    if minimo4 == risultato4:
        andamento4 = '😴 (fermo)'
    elif minimo4 < risultato4:
        andamento4 = '📉 (sta calando da ' + risultato_virgola4 + ' €)'
    else:
        andamento4 = '📈 (sta salendo da ' + risultato_virgola4 + ' €)'
    
    testo_messaggio4_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_4_1 + ' €' + "*" + " su Idealo " + "\n" + andamento4
    testo_messaggio4_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_4_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento4
    testo_messaggio4_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_4_3 + ' €' + "*" + " su Amazon " + "\n" + andamento4
    
    if prezzo_finale_4_3 == minimo4:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio4_3}')
    elif prezzo_finale_4_1 == minimo4:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio4_1}')
    else:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio4_2}')
    
    database4 = open ("Minimi4.txt", "a")
    database4.write ("\n" + minimo4)
    database4.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()

def main(event={}, context={}):
    name = 'Corsair Vengeance RGB Pro 16 GB (2 x 8 GB) 3600 Mhz'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '6844731/corsair-vengeance-rgb-pro-16gb-kit-ddr4-3600-cl18-cmw16gx4m2d3600c18.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result5_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_5_1 = result5_1[0] + '.' + result5_1[1]
    prezzo_virgola_5_1 =result5_1[0] + ',' + result5_1[1]
    print('.')
    print (prezzo_virgola_5_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'prezzo_ram_ddr4_16gb_kit_2x8gb_pc_3600_corsair_vengeance_rgb_pro_cmw16gx4m2d3600c18.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', style= "white-space:nowrap").text
    print('.')
    result5_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_5_2 = result5_2[0] + '.' + result5_2[1]
    prezzo_virgola_5_2 =result5_2[0] + ',' + result5_2[1]
    print('.')
    print (prezzo_virgola_5_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Corsair-Vengeance-Black-DDR4-RAM-memoria/dp/B07TB3R9JB/ref=sr_1_3?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=Corsair+Vengeance+RGB+Pro+16GB+Kit+DDR4-3600&qid=1611045205&sr=8-3'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result5_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_5_3 = result5_3[0] + '.' + result5_3[1]
    prezzo_virgola_5_3 =result5_3[0] + ',' + result5_3[1]
    print('.')
    print (prezzo_virgola_5_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo5 = min (prezzo_finale_5_1, prezzo_finale_5_2, prezzo_finale_5_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo5 + ' €')
    print('Inviato!')
    
    database5 = open ("Minimi5.txt", "r").read()
    lista5 = re.findall(r'\b\d+\b', database5)
    risultato5 = lista5[-2] + '.' + lista5[-1]
    risultato_virgola5 = lista5[-2] + ',' + lista5[-1]
    
    if minimo5 == risultato5:
        andamento5 = '😴 (fermo)'
    elif minimo5 < risultato5:
        andamento5 = '📉 (sta calando da ' + risultato_virgola5 + ' €)'
    else:
        andamento5 = '📈 (sta salendo da ' + risultato_virgola5 + ' €)'
    
    testo_messaggio5_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_5_1 + ' €' + "*" + " su Idealo " + "\n" + andamento5
    testo_messaggio5_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_5_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento5
    testo_messaggio5_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_5_3 + ' €' + "*" + " su Amazon " + "\n" + andamento5
    
    if prezzo_finale_5_3 == minimo5:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio5_3}')
    elif prezzo_finale_5_1 == minimo5:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio5_1}')
    else:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio5_2}')
    
    database5 = open ("Minimi5.txt", "a")
    database5.write ("\n" + minimo5)
    database5.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()

def main(event={}, context={}):
    name = 'CoolerMaster MasterBox MB611 ARGB'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '7074513/coolermaster-masterbox-mb511-argb.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result6_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_6_1 = result6_1[0] + '.' + result6_1[1]
    prezzo_virgola_6_1 =result6_1[0] + ',' + result6_1[1]
    print('.')
    print (prezzo_virgola_6_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Cooler-Master-MasterBox-MB511-MCB-B511D-KGNN-RGA/dp/B0839XNV6H/ref=sr_1_1?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=CoolerMaster+MasterBox+MB511+ARGB&qid=1611046309&sr=8-1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result6_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_6_3 = result6_3[0] + '.' + result6_3[1]
    prezzo_virgola_6_3 =result6_3[0] + ',' + result6_3[1]
    print('.')
    print (prezzo_virgola_6_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo6 = min (prezzo_finale_6_1, prezzo_finale_6_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo6 + ' €')
    print('Inviato!')
    
    database6 = open ("Minimi6.txt", "r").read()
    lista6 = re.findall(r'\b\d+\b', database6)
    risultato6 = lista6[-2] + '.' + lista6[-1]
    risultato_virgola6 = lista6[-2] + ',' + lista6[-1]
    
    if minimo6 == risultato6:
        andamento6 = '😴 (fermo)'
    elif minimo6 < risultato6:
        andamento6 = '📉 (sta calando da ' + risultato_virgola6 + ' €)'
    else:
        andamento6 = '📈 (sta salendo da ' + risultato_virgola6 + ' €)'
    
    testo_messaggio6_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_6_1 + ' €' + "*" + " su Idealo " + "\n" + andamento6
    testo_messaggio6_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_6_3 + ' €' + "*" + " su Amazon " + "\n" + andamento6
    
    if prezzo_finale_6_3 == minimo6:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio6_3}')
    elif prezzo_finale_6_1 == minimo6:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio6_1}')
    
    database6 = open ("Minimi6.txt", "a")
    database6.write ("\n" + minimo6)
    database6.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()
    
def main(event={}, context={}):
    name = 'Corsair RM750X'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '6052663/corsair-rm750x-2018-750w-black.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result7_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_7_1 = result7_1[0] + '.' + result7_1[1]
    prezzo_virgola_7_1 =result7_1[0] + ',' + result7_1[1]
    print('.')
    print (prezzo_virgola_7_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'Fprezzo_case-alimentatori_corsair_rm750x.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "alert_price_tab").text
    print('.')
    result7_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_7_2 = result7_2[0] + '.' + result7_2[1]
    prezzo_virgola_7_2 =result7_2[0] + ',' + result7_2[1]
    print('.')
    print (prezzo_virgola_7_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Corsair-RM750x-Alimentatore-Completamente-Modulare/dp/B07GY3VFW8/ref=sr_1_fkmr0_1?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=Corsair+RM750X&qid=1611050396&sr=8-1-fkmr0'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result7_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_7_3 = result7_3[0] + '.' + result7_3[1]
    prezzo_virgola_7_3 =result7_3[0] + ',' + result7_3[1]
    print('.')
    print (prezzo_virgola_7_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo7 = min (prezzo_finale_7_1, prezzo_finale_7_2, prezzo_finale_7_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo7 + ' €')
    print('Inviato!')
    
    database7 = open ("Minimi7.txt", "r").read()
    lista7 = re.findall(r'\b\d+\b', database7)
    risultato7 = lista7[-2] + '.' + lista7[-1]
    risultato_virgola7 = lista7[-2] + ',' + lista7[-1]
    
    if minimo7 == risultato7:
        andamento7 = '😴 (fermo)'
    elif minimo7 < risultato7:
        andamento7 = '📉 (sta calando da ' + risultato_virgola7 + ' €)'
    else:
        andamento7 = '📈 (sta salendo da ' + risultato_virgola7 + ' €)'
    
    testo_messaggio7_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_7_1 + ' €' + "*" + " su Idealo " + "\n" + andamento7
    testo_messaggio7_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_7_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento7
    testo_messaggio7_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_7_3 + ' €' + "*" + " su Amazon " + "\n" + andamento7
    
    if prezzo_finale_7_3 == minimo7:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio7_3}')
    elif prezzo_finale_7_1 == minimo7:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio7_1}')
    else:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio7_2}')
    
    database7 = open ("Minimi7.txt", "a")
    database7.write ("\n" + minimo7)
    database7.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()

def main(event={}, context={}):
    name = 'Corsair RM850X'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '6317984/corsair-rm850x-2018-850w.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result8_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_8_1 = result8_1[0] + '.' + result8_1[1]
    prezzo_virgola_8_1 =result8_1[0] + ',' + result8_1[1]
    print('.')
    print (prezzo_virgola_8_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Corsair-RM850x-Alimentatore-Completamente-Modulare/dp/B07GY4ZCQT/ref=sr_1_1?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=RM850x&qid=1611053453&s=pc&sr=1-1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result8_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_8_3 = result8_3[0] + '.' + result8_3[1]
    prezzo_virgola_8_3 =result8_3[0] + ',' + result8_3[1]
    print('.')
    print (prezzo_virgola_8_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo8 = min (prezzo_finale_8_1, prezzo_finale_8_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo8 + ' €')
    print('Inviato!')
    
    database8 = open ("Minimi8.txt", "r").read()
    lista8 = re.findall(r'\b\d+\b', database8)
    risultato8 = lista8[-2] + '.' + lista8[-1]
    risultato_virgola8 = lista8[-2] + ',' + lista8[-1]
    
    if minimo8 == risultato8:
        andamento8 = '😴 (fermo)'
    elif minimo8 < risultato8:
        andamento8 = '📉 (sta calando da ' + risultato_virgola8 + ' €)'
    else:
        andamento8 = '📈 (sta salendo da ' + risultato_virgola8 + ' €)'
    
    testo_messaggio8_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_8_1 + ' €' + "*" + " su Idealo " + "\n" + andamento8
    testo_messaggio8_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_8_3 + ' €' + "*" + " su Amazon " + "\n" + andamento8
    
    if prezzo_finale_8_3 == minimo8:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio8_3}')
    elif prezzo_finale_8_1 == minimo8:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio8_1}')
    
    database8 = open ("Minimi8.txt", "a")
    database8.write ("\n" + minimo8)
    database8.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()
    
def main(event={}, context={}):
    name = 'Corsair RM850i'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '4830652/corsair-rm850i-850w.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result9_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_9_1 = result9_1[0] + '.' + result9_1[1]
    prezzo_virgola_9_1 =result9_1[0] + ',' + result9_1[1]
    print('.')
    print (prezzo_virgola_9_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'Fprezzo_case-alimentatori_corsair_rm850i.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "alert_price_tab").text
    print('.')
    result9_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_9_2 = result9_2[0] + '.' + result9_2[1]
    prezzo_virgola_9_2 =result9_2[0] + ',' + result9_2[1]
    print('.')
    print (prezzo_virgola_9_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Corsair-Alimentatore-Completamente-Modulare-Digital/dp/B00ZRL7LUE/ref=sr_1_1?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=RM850i&qid=1611053830&s=pc&sr=1-1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result9_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_9_3 = result9_3[0] + '.' + result9_3[1]
    prezzo_virgola_9_3 =result9_3[0] + ',' + result9_3[1]
    print('.')
    print (prezzo_virgola_9_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo9 = min (prezzo_finale_9_1, prezzo_finale_9_2, prezzo_finale_9_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo9 + ' €')
    print('Inviato!')
    
    database9 = open ("Minimi9.txt", "r").read()
    lista9 = re.findall(r'\b\d+\b', database9)
    risultato9 = lista9[-2] + '.' + lista9[-1]
    risultato_virgola9 = lista9[-2] + ',' + lista9[-1]
    
    if minimo9 == risultato9:
        andamento9 = '😴 (fermo)'
    elif minimo9 < risultato9:
        andamento9 = '📉 (sta calando da ' + risultato_virgola9 + ' €)'
    else:
        andamento9 = '📈 (sta salendo da ' + risultato_virgola9 + ' €)'
    
    testo_messaggio9_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_9_1 + ' €' + "*" + " su Idealo " + "\n" + andamento9
    testo_messaggio9_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_9_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento9
    testo_messaggio9_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_9_3 + ' €' + "*" + " su Amazon " + "\n" + andamento9
    
    if prezzo_finale_9_3 == minimo9:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio9_3}')
    elif prezzo_finale_9_1 == minimo9:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio9_1}')
    else:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio9_2}')
    
    database9 = open ("Minimi9.txt", "a")
    database9.write ("\n" + minimo9)
    database9.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()

def main(event={}, context={}):
    name = 'Corsair RM1000X'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '4867188/corsair-rm1000x-1000w.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result10_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_10_1 = result10_1[0] + '.' + result10_1[1]
    prezzo_virgola_10_1 =result10_1[0] + ',' + result10_1[1]
    print('.')
    print (prezzo_virgola_10_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'Fprezzo_case-alimentatori_corsair_rm1000x.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "alert_price_tab").text
    print('.')
    result10_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_10_2 = result10_2[0] + '.' + result10_2[1]
    prezzo_virgola_10_2 =result10_2[0] + ',' + result10_2[1]
    print('.')
    print (prezzo_virgola_10_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Corsair-RM1000x-Alimentatore-Completamente-Modulare/dp/B015Q7F5AQ/ref=sr_1_1?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=RM1000x&qid=1611054269&s=pc&sr=1-1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result10_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_10_3 = result10_3[0] + '.' + result10_3[1]
    prezzo_virgola_10_3 =result10_3[0] + ',' + result10_3[1]
    print('.')
    print (prezzo_virgola_10_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo10 = min (prezzo_finale_10_1, prezzo_finale_10_2, prezzo_finale_10_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo10 + ' €')
    print('Inviato!')
    
    database10 = open ("Minimi10.txt", "r").read()
    lista10 = re.findall(r'\b\d+\b', database10)
    risultato10 = lista10[-2] + '.' + lista10[-1]
    risultato_virgola10 = lista10[-2] + ',' + lista10[-1]
    
    if minimo10 == risultato10:
        andamento10 = '😴 (fermo)'
    elif minimo10 < risultato10:
        andamento10 = '📉 (sta calando da ' + risultato_virgola10 + ' €)'
    else:
        andamento10 = '📈 (sta salendo da ' + risultato_virgola10 + ' €)'
    
    testo_messaggio10_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_10_1 + ' €' + "*" + " su Idealo " + "\n" + andamento10
    testo_messaggio10_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_10_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento10
    testo_messaggio10_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_10_3 + ' €' + "*" + " su Amazon " + "\n" + andamento10
    
    if prezzo_finale_10_3 == minimo10:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio10_3}')
    elif prezzo_finale_10_1 == minimo10:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio10_1}')
    else:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio10_2}')
    
    database10 = open ("Minimi10.txt", "a")
    database10.write ("\n" + minimo10)
    database10.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()
    
def main(event={}, context={}):
    name = 'Corsair RM1000i'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '4794385/corsair-rm1000i-1000w.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result11_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_11_1 = result11_1[0] + '.' + result11_1[1]
    prezzo_virgola_11_1 =result11_1[0] + ',' + result11_1[1]
    print('.')
    print (prezzo_virgola_11_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Corsair-RM1000i-Alimentatore-Completamente-Modulare/dp/B00ZRL7WYY/ref=sr_1_1?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=Corsair+RM1000i&qid=1611054481&s=pc&sr=1-1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result11_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_11_3 = result11_3[0] + '.' + result11_3[1]
    prezzo_virgola_11_3 =result11_3[0] + ',' + result11_3[1]
    print('.')
    print (prezzo_virgola_11_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo11 = min (prezzo_finale_11_1, prezzo_finale_11_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo11 + ' €')
    print('Inviato!')
    
    database11 = open ("Minimi11.txt", "r").read()
    lista11 = re.findall(r'\b\d+\b', database11)
    risultato11 = lista11[-2] + '.' + lista11[-1]
    risultato_virgola11 = lista11[-2] + ',' + lista11[-1]
    
    if minimo11 == risultato11:
        andamento11 = '😴 (fermo)'
    elif minimo11 < risultato11:
        andamento11 = '📉 (sta calando da ' + risultato_virgola11 + ' €)'
    else:
        andamento11 = '📈 (sta salendo da ' + risultato_virgola11 + ' €)'
    
    testo_messaggio11_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_11_1 + ' €' + "*" + " su Idealo " + "\n" + andamento11
    testo_messaggio11_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_11_3 + ' €' + "*" + " su Amazon " + "\n" + andamento11
    
    if prezzo_finale_11_3 == minimo11:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio11_3}')
    elif prezzo_finale_11_1 == minimo11:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio11_1}')
    
    database11 = open ("Minimi11.txt", "a")
    database11.write ("\n" + minimo11)
    database11.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()
    
def main(event={}, context={}):
    name = 'Dissipatore cpu a liquido Msi Mag Core Liquid 240R'
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'prezzo_dissipatori-e-ventole_msi_mag_core_liquid_240r.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', style= "white-space:nowrap").text
    print('.')
    result12_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_12_2 = result12_2[0] + '.' + result12_2[1]
    prezzo_virgola_12_2 =result12_2[0] + ',' + result12_2[1]
    print('.')
    print (prezzo_virgola_12_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'MSI-CoreLiquid-Dissipatore-radiatore-Compatibile/dp/B089QZ9GX8/ref=sr_1_1?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=msi+mag+coreliquid+240r&qid=1611055106&s=pc&sr=1-1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result12_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_12_3 = result12_3[0] + '.' + result12_3[1]
    prezzo_virgola_12_3 =result12_3[0] + ',' + result12_3[1]
    print('.')
    print (prezzo_virgola_12_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo12 = min (prezzo_finale_12_2, prezzo_finale_12_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo12 + ' €')
    print('Inviato!')
    
    database12 = open ("Minimi12.txt", "r").read()
    lista12 = re.findall(r'\b\d+\b', database12)
    risultato12 = lista12[-2] + '.' + lista12[-1]
    risultato_virgola12 = lista12[-2] + ',' + lista12[-1]
    
    if minimo12 == risultato12:
        andamento12 = '😴 (fermo)'
    elif minimo12 < risultato12:
        andamento12 = '📉 (sta calando da ' + risultato_virgola12 + ' €)'
    else:
        andamento12 = '📈 (sta salendo da ' + risultato_virgola12 + ' €)'
    
    testo_messaggio12_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_12_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento12
    testo_messaggio12_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_12_3 + ' €' + "*" + " su Amazon " + "\n" + andamento12
    
    if prezzo_finale_12_3 == minimo12:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio12_3}')
    elif prezzo_finale_12_2 == minimo12:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio12_2}')
    
    database12 = open ("Minimi12.txt", "a")
    database12.write ("\n" + minimo12)
    database12.close ()
    
    time.sleep(3)

if __name__ == '__main__':
    main()
    
def main(event={}, context={}):
    name = 'Dissipatore cpu a liquido Msi Mag Core Liquid 360R'
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'prezzo_dissipatori-e-ventole_msi_mag_core_liquid_360r.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', style= "white-space:nowrap").text
    print('.')
    result13_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_13_2 = result13_2[0] + '.' + result13_2[1]
    prezzo_virgola_13_2 =result13_2[0] + ',' + result13_2[1]
    print('.')
    print (prezzo_virgola_13_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'MSI-CoreLiquid-360R-Dissipatore-Compatibile/dp/B089QYGNFK/ref=sr_1_1?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=msi+mag+coreliquid+360r&qid=1611055475&s=pc&sr=1-1'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result13_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_13_3 = result13_3[0] + '.' + result13_3[1]
    prezzo_virgola_13_3 =result13_3[0] + ',' + result13_3[1]
    print('.')
    print (prezzo_virgola_13_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo13 = min (prezzo_finale_13_2, prezzo_finale_13_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo13 + ' €')
    print('Inviato!')
    
    database13 = open ("Minimi13.txt", "r").read()
    lista13 = re.findall(r'\b\d+\b', database13)
    risultato13 = lista13[-2] + '.' + lista13[-1]
    risultato_virgola13 = lista13[-2] + ',' + lista13[-1]
    
    if minimo13 == risultato13:
        andamento13 = '😴 (fermo)'
    elif minimo13 < risultato13:
        andamento13 = '📉 (sta calando da ' + risultato_virgola13 + ' €)'
    else:
        andamento13 = '📈 (sta salendo da ' + risultato_virgola13 + ' €)'
    
    testo_messaggio13_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_13_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento13
    testo_messaggio13_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_13_3 + ' €' + "*" + " su Amazon " + "\n" + andamento13
    
    if prezzo_finale_13_3 == minimo13:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio13_3}')
    elif prezzo_finale_13_2 == minimo13:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio13_2}')
    
    database13 = open ("Minimi13.txt", "a")
    database13.write ("\n" + minimo13)
    database13.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()
    
def main(event={}, context={}):
    name = 'Ssd Crucial P2 M.2 Nvme 500 GB'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '200241235/crucial-p2-500gb-m-2.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result14_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_14_1 = result14_1[0] + '.' + result14_1[1]
    prezzo_virgola_14_1 =result14_1[0] + ',' + result14_1[1]
    print('.')
    print (prezzo_virgola_14_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'prezzo_hard-disk_ssd_crucial_p2_pcie_m.2_nvme_500gb.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', style= "white-space:nowrap").text
    print('.')
    result14_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_14_2 = result14_2[0] + '.' + result14_2[1]
    prezzo_virgola_14_2 =result14_2[0] + ',' + result14_2[1]
    print('.')
    print (prezzo_virgola_14_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo14 = min (prezzo_finale_14_1, prezzo_finale_14_2)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo14 + ' €')
    print('Inviato!')
    
    database14 = open ("Minimi14.txt", "r").read()
    lista14 = re.findall(r'\b\d+\b', database14)
    risultato14 = lista14[-2] + '.' + lista14[-1]
    risultato_virgola14 = lista14[-2] + ',' + lista14[-1]
    
    if minimo14 == risultato14:
        andamento14 = '😴 (fermo)'
    elif minimo14 < risultato14:
        andamento14 = '📉 (sta calando da ' + risultato_virgola14 + ' €)'
    else:
        andamento14 = '📈 (sta salendo da ' + risultato_virgola14 + ' €)'
    
    testo_messaggio14_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_14_1 + ' €' + "*" + " su Idealo " + "\n" + andamento14
    testo_messaggio14_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_14_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento14
    
    if prezzo_finale_14_1 == minimo14:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio14_1}')
    elif prezzo_finale_14_2 == minimo14:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio14_2}')
    
    database14 = open ("Minimi14.txt", "a")
    database14.write ("\n" + minimo14)
    database14.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()
    
def main(event={}, context={}):
    name = 'Ssd Samsung Evo M.2 Nvme 500 GB'
    
    print ('XXXXXXXXXXXXXXX')
    print ('IDEALO')
    print('Inviando')
    item = '6143328/samsung-970-evo-500gb-m-2.html'
    url = BASE_URL_1 + item
    r1 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r1.text, 'html.parser')
    print('.')
    price = soup.find('a', class_='productOffers-listItemOfferPrice').text
    print('.')
    result15_1 = re.findall(r'\b\d+\b', price)
    prezzo_finale_15_1 = result15_1[0] + '.' + result15_1[1]
    prezzo_virgola_15_1 =result15_1[0] + ',' + result15_1[1]
    print('.')
    print (prezzo_virgola_15_1 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('TROVAPREZZI')
    print('Inviando')
    item = 'prezzo_hard-disk_ssd_nvme_samsung_evo_500gb.aspx'
    url = BASE_URL_2 + item
    r2 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r2.text, 'html.parser')
    print('.')
    price = soup.find('span', style= "white-space:nowrap").text
    print('.')
    result15_2 = re.findall(r'\b\d+\b', price)
    prezzo_finale_15_2 = result15_2[0] + '.' + result15_2[1]
    prezzo_virgola_15_2 =result15_2[0] + ',' + result15_2[1]
    print('.')
    print (prezzo_virgola_15_2 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')
    
    print('AMAZON')
    print('Inviando')
    item = 'Samsung-MZ-V7E500BW-NVMe-Nero-Arancione/dp/B07CGGP7SV/ref=sr_1_2?__mk_it_IT=ÅMÅŽÕÑ&dchild=1&keywords=ssd+nvme+samsung+evo+500gb&qid=1611056278&s=pc&sr=1-2'
    url = BASE_URL_3 + item
    r3 = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(r3.text, 'html.parser')
    print('.')
    price = soup.find('span', class_= "a-size-medium a-color-price priceBlockBuyingPriceString").text
    print('.')
    result15_3 = re.findall(r'\b\d+\b', price)
    prezzo_finale_15_3 = result15_3[0] + '.' + result15_3[1]
    prezzo_virgola_15_3 =result15_3[0] + ',' + result15_3[1]
    print('.')
    print (prezzo_virgola_15_3 + ' €')
    print('Inviato!')
    print ('XXXXXXXXXXXXXXX')

    print('Inviando')
    print('.')
    minimo15 = min (prezzo_finale_15_1, prezzo_finale_15_2, prezzo_finale_15_3)
    print('.')
    print('.')
    print('Il prezzo più basso è: ' + minimo15 + ' €')
    print('Inviato!')
    
    database15 = open ("Minimi15.txt", "r").read()
    lista15 = re.findall(r'\b\d+\b', database15)
    risultato15 = lista15[-2] + '.' + lista15[-1]
    risultato_virgola15 = lista15[-2] + ',' + lista15[-1]
    
    if minimo15 == risultato15:
        andamento15 = '😴 (fermo)'
    elif minimo15 < risultato15:
        andamento15 = '📉 (sta calando da ' + risultato_virgola15 + ' €)'
    else:
        andamento15 = '📈 (sta salendo da ' + risultato_virgola15 + ' €)'
    
    testo_messaggio15_1 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_15_1 + ' €' + "*" + " su Idealo " + "\n" + andamento15
    testo_messaggio15_2 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_15_2 + ' €' + "*" + " su Trovaprezzi " + "\n" + andamento15
    testo_messaggio15_3 = "Vedi che " + name + " sta a " + "\n" + "*" + prezzo_virgola_15_3 + ' €' + "*" + " su Amazon " + "\n" + andamento15
    
    if prezzo_finale_15_3 == minimo15:
        r3 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio15_3}')
    elif prezzo_finale_15_1 == minimo15:
        r1 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio15_1}')
    else:
        r2 = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_messaggio15_2}')
    
    database15 = open ("Minimi15.txt", "a")
    database15.write ("\n" + minimo15)
    database15.close ()
    
    time.sleep(3)
    
if __name__ == '__main__':
    main()

print('Inviando')
print('.')
testo_finale = "⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️"
print('.')
f = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={testo_finale}')
print('.')
print('Inviato!')