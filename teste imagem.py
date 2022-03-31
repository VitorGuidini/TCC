# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:53:10 2022

@author: vguid
"""
import numpy as np
import PIL
import matplotlib.pyplot as plt
import cv2
## print ('Pillow Version:',PIL.__version__)
from PIL import Image


'''# Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem.jpg")

# Visualizando a imagem:
image.show()

# Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem2.jpg")

# Visualizando a imagem:
image.show()


# Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem3.jpg")

# Visualizando a imagem:
image.show()


# Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem4.jpg")

# Visualizando a imagem:
image.show()


# Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem5.jpg")

# Visualizando a imagem:
image.show()


# Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem6.jpg")

# Visualizando a imagem:
image.show()


# Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem7.jpg")

# Visualizando a imagem:
image.show()


# Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem8.jpg")

# Visualizando a imagem:
image.show()

# Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem9.jpg")
'''
#Visualizando a imagem:
#image.show()


#Carregar um imagem a partir do disco:
image = Image.open("C:\TCC/imagem10.jpg")

# Visualizando a imagem:
image.show()
print (image, 'M2(1)')



'''
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
  
#cv2.destroyAllWindows()
'''












'''
# Import required image modules
#from PIL import Image, ImageFilter
  
# Import all the enhancement filter from pillow
#from PIL.ImageFilter import (
#   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
#   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
#)
  
# Create image object
#img = Image.open("C:\TesteTCC/Lampada-Poste.jpg")
  
# Applying the sharpen filter
# You can change the value in filter function
# to see the deifferences
#img1 = img.filter(SHARPEN)
#img1.show()
'''