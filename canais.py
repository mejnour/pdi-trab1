# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import sys

def image_split_monochromatic(image):
    r = np.zeros((image.height, image.width, 3), 'uint8') #cria um array multidimensional(1x1x3) preenchido por zeros usando as dimensões da
    g = np.zeros((image.height, image.width, 3), 'uint8') #imagem e a quantidade de componentes que existe por cada pixel(RGB) 
    b = np.zeros((image.height, image.width, 3), 'uint8')
							
    for i in range(image.width):
        for j in range(image.height):			  #percorre todos os pixels da imagem
            rc, gc, bc = image.getpixel((i, j)) 	  #retorna os valores de r ,g e b do pixel(i,j)
            r[j, i, 0] = r[j, i, 1] = r[j, i, 2] = rc	  #iguala os "níveis" de vermelho aos capturados no pixel para produzir "cinza" 
            g[j, i, 0] = g[j, i, 1] = g[j, i, 2] = gc	
            b[j, i, 0] = b[j, i, 1] = b[j, i, 2] = bc

    return r, g, b

def image_split_color(image):
    r = np.zeros((image.height, image.width, 3), 'uint8')
    g = np.zeros((image.height, image.width, 3), 'uint8')
    b = np.zeros((image.height, image.width, 3), 'uint8')

    for i in range(image.width):
        for j in range(image.height):
            rc, gc, bc = image.getpixel((i, j))
            r[j, i, 0] = rc #captura os níveis de vermelho do pixel
            g[j, i, 1] = gc
            b[j, i, 2] = bc

    return r, g, b

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1]) #abre a imagem passada como argumento 
    
    print("1 - Exibir bandas individuais como imagens monocromáticas")
    print("2 - Exibir bandas individuais como imagens coloridas")
    
    option = int(input("Selecione uma opção: "))
    
    if option == 1:
        r, g, b = image_split_monochromatic(img) #extrai as bandas monocromáticas 
        
        while True:
            print("\n1 - Exibir banda R")
            print("2 - Exibir banda G")
            print("3 - Exibir banda B")
            print("0 - Sair")
            
            option = int(input("Selecione uma opção: "))
            
            if option == 0:
                break
            
            elif option == 1:
                im = Image.fromarray(r)	#constrói a imagem usando a banda monocromática r
                im.show()		#mostra a imagem construída
                
            elif option == 2:
                im = Image.fromarray(g)
                im.show()
                
            elif option == 3:
                im = Image.fromarray(b)
                im.show()
                
    else:
        r, g, b = image_split_color(img) #extrai bandas coloridas
        
        while True:
            print("\n1 - Exibir banda R")
            print("2 - Exibir banda G")
            print("3 - Exibir banda B")
            print("0 - Sair")
            
            option = int(input("Selecione uma opção: "))
            
            if option == 0:
                break
            
            elif option == 1:
                im = Image.fromarray(r) #constrói a imagem usando a banda colorida r
                im.show()		#mostra a imagem construída
                
            elif option == 2:
                im = Image.fromarray(g)
                im.show()
                
            elif option == 3:
                im = Image.fromarray(b)
                im.show()
                
if __name__ == "__main__":
    main()
