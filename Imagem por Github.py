# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:33:01 2022

@author: vguid
"""

import requests 
from bs4 import BeautifulSoup as bs

usuario_github = input("Digite o usuario: ")
link = "https://github.com/"+usuario_github
requisição = requests.get (link)
soup=bs(requisição.content, "html.parser")
imagem_perfil =soup.find("img", {'alt': 'Avatar'})['src']
print(imagem_perfil)
