# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:55:08 2022

@author: vguid
"""

##Programa Principal

from selenium import webdriver
import numpy as np
import requests 
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import cv2


## capturar foto
usuario_github = input("Digite o usuario: ")
link = "https://github.com/"+usuario_github
requisição = requests.get (link)
soup=bs(requisição.content, "html.parser")
imagem_perfil = soup.find("img", {'alt': 'Avatar'})['src']
print(imagem_perfil)


## acesso a site
driver = webdriver.Chrome()

driver.get("https://www.youtube.com/channel/UCUN9lhwfMJRxMVuet7Shg0w")

## aplica filtro
array = np.array([150,150,150])
array1 = np.array([17, 0, 255])
image= cv2.imread('C:/TCC/imagem.jpg')
mascara= cv2.inRange(image,array,array1)
plt.imshow(mascara)
plt.show()

image = cv2.imread('C:/TCC/imagem10.jpg') 
B, G, R = cv2.split(image) 
  
cv2.imshow("original", image) 
cv2.waitKey(0) 
  
cv2.imshow("blue", B) 
cv2.waitKey(0) 
  
cv2.imshow("Green", G) 
cv2.waitKey(0) 
  
cv2.imshow("red", R) 
cv2.waitKey(0) 
  
cv2.destroyAllWindows()