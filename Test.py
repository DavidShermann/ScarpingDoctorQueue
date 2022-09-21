


from bs4 import BeautifulSoup
import requests 


payload = {
 'identifyWithPasswordCitizenId' : '208733360',
 'password' : 'HGTarMH3UKgeR8b'
 }

with requests.Session() as s:
    p = s.post('https://online.maccabi4u.co.il/', data=payload).text
    print(p)


