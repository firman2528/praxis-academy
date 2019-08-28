import requests
from bs4 import BeautifulSoup
import sys


class ambilwebsite :
    ling = ""

    def __main__(self):
        pass
        # self.ambil()

    @classmethod
    def ambil(cls) :
        for a in sys.argv :
            cls.ling = a 
        return cls.ling  

web_r = requests.get(ambilwebsite.ambil())

web_soup = BeautifulSoup(web_r.text, 'html.parser')

print(web_soup.findAll())