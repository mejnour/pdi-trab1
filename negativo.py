# -*- coding: utf-8 -*-
import numpy as np
import yiq
from PIL import Image
import sys

def negative(image):
    neg = np.zeros((image.height, image.width, 3), 'uint8') #cria um array multidimensional(1x1x3) preenchido por zeros usando as dimensões da
							    #imagem e a quantidade de componentes que existe por cada pixel(RGB)
    for i in range(image.width):
        for j in range(image.height):			    #percorre todos os pixels da imagem
            r, g, b = image.getpixel((i, j))		    #retorna os valores de r ,g e b do pixel(i,j)

            neg[j, i, 0] = 255 - r	#subtrai de 255 o valor capturado em r do pixel
            neg[j, i, 1] = 255 - g
            neg[j, i, 2] = 255 - b

    return neg

def negativeR(image):
    neg = np.zeros((image.height, image.width, 3), 'uint8') #cria um array multidimensional(1x1x3) preenchido por zeros usando as dimensões da
							    #imagem e a quantidade de componentes que existe por cada pixel(RGB)
    for i in range(image.width):
        for j in range(image.height):			    #percorre todos os pixels da imagem
            r, g, b = image.getpixel((i, j))		    #retorna os valores de r ,g e b do pixel(i,j)

            neg[j, i, 0] = 255 - r	#subtrai de 255 o valor capturado em r do pixel
            neg[j, i, 1] = g
            neg[j, i, 2] = b

    return neg

def negativeG(image):
    neg = np.zeros((image.height, image.width, 3), 'uint8') #cria um array multidimensional(1x1x3) preenchido por zeros usando as dimensões da
							    #imagem e a quantidade de componentes que existe por cada pixel(RGB)
    for i in range(image.width):
        for j in range(image.height):			    #percorre todos os pixels da imagem
            r, g, b = image.getpixel((i, j))		    #retorna os valores de r ,g e b do pixel(i,j)

            neg[j, i, 0] = r	
            neg[j, i, 1] = 255 - g      #subtrai de 255 o valor capturado em g do pixel
            neg[j, i, 2] = b

    return neg

def negativeB(image):
    neg = np.zeros((image.height, image.width, 3), 'uint8') #cria um array multidimensional(1x1x3) preenchido por zeros usando as dimensões da
							    #imagem e a quantidade de componentes que existe por cada pixel(RGB)
    for i in range(image.width):
        for j in range(image.height):			    #percorre todos os pixels da imagem
            r, g, b = image.getpixel((i, j))		    #retorna os valores de r ,g e b do pixel(i,j)

            neg[j, i, 0] = r	
            neg[j, i, 1] = g
            neg[j, i, 2] = 255 - b      #subtrai de 255 o valor capturado em b do pixel

    return neg

def negative_y(image, width, height):
    neg = np.zeros((height, width, 3), 'float32')

    for k in range(width):
        for j in range(height):
            y = image[j, k, 0]
            i = image[j, k, 1]
            q = image[j, k, 2]

            neg[j, k, 0] = 1-y
            neg[j, k, 1] = i
            neg[j, k, 2] = q

    return neg

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1]) #abre a imagem passada como argumento 
    
    print("1 - Aplicar negativo em RGB")
    print("2 - Aplicar negativo em R")
    print("3 - Aplicar negativo em G")
    print("4 - Aplicar negativo em B")
    print("5 - Aplicar negativo em Y")
    print("0 - Sair")
    
    option = int(input("Selecione uma opção: "))
    
    if option == 1:
        im = negative(img) #retorna um array após deixar as cores negativas em RGB
        im = Image.fromarray(im) #constrói a imagem 
        im.show() #mostra a imagem construída
    
    elif option == 2:
        im = negativeR(img) #retorna um array após deixar as cores negativas em R
        im = Image.fromarray(im) #constrói a imagem 
        im.show() #mostra a imagem construída
        
    elif option == 3:
        im = negativeG(img) #retorna um array após deixar as cores negativas em G
        im = Image.fromarray(im) #constrói a imagem 
        im.show() #mostra a imagem construída
        
    elif option == 4:
        im = negativeB(img) #retorna um array após deixar as cores negativas em B
        im = Image.fromarray(im) #constrói a imagem 
        im.show() #mostra a imagem construída
        
    elif option == 5:
        im = yiq.rgb2yiq(img) #converte a imagem de rgb para yiq
        im = negative_y(im, img.width, img.height) #utiliza a nossa função para deixar deixar a imagem negativa
        im = yiq.yiq2rgb(im, img.width, img.height) #converte de yiq para rgb
        im = Image.fromarray(im) #constrói a imagem 
        im.show()		#mostra a imagem construída 
        
    else:
        sys.exit(0)
        
if __name__ == "__main__":
    main()
