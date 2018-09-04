import numpy as np
import yiq
from PIL import Image
import sys

def aditive_brightness(image, plus): #BRILHO ADITIVO
    img = np.zeros((image.height, image.width, 3), 'uint8') #Matriz de inteiros com a quantidade de linhas e colunas da imagem para os 3 canais rgb

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j)) #func getpixel retorna uma tupla RGB

            img[j, i, 0] = min(255, r + plus) #se a soma do canal R ficar maior que 255, R fica em 255, se menor que 255, R é o valor obtido na soma
            img[j, i, 1] = min(255, g + plus) #se a soma do canal G ficar maior que 255, G fica em 255, se menor que 255, G é o valor obtido na soma
            img[j, i, 2] = min(255, b + plus) #se a soma do canal B ficar maior que 255, B fica em 255, se menor que 255, B é o valor obtido na soma

    print("Done")

    return img

def multiplicative_brightness(image, mult): #BRILHO MULTIPLICATIVO
    img = np.zeros((image.height, image.width, 3), 'uint8')

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j))

            img[j, i, 0] = min(255, r * mult)
            img[j, i, 1] = min(255, g * mult)
            img[j, i, 2] = min(255, b * mult)

    print("Done")

    return img

def aditive_brightness_y(image, width, height, plus): #BRILHO ADITIVO EM Y
    img = np.zeros((height, width, 3), 'float32') #Matriz de float 32bits com a quantidade de linhas e colunas da imagem para os 3 canais yiq

    for i in range(width):
        for j in range(height):
            y = image[j, i, 0]  #canal y
            ii = image[j, i, 1]	#canal i
            q = image[j, i, 2]	#canal q

            img[j, i, 0] = min(1.0, y + plus) #exibe o menor valor entre os dois numeros. se a soma for maior que 1 o resultado irá para 1
            img[j, i, 1] = ii	#canal i continua igual
            img[j, i, 2] = q	#canal q continua igual

    print("Done")

    return img

def multiplicative_brightness_y(image, width, height, mult): #BRILHO MULTIPLICATIVO EM Y
    img = np.zeros((height, width, 3), 'float32')

    for i in range(width):
        for j in range(height):
            y = image[j, i, 0]
            ii = image[j, i, 1]
            q = image[j, i, 2]

            img[j, i, 0] = min(1.0, y * mult)
            img[j, i, 1] = ii
            img[j, i, 2] = q

    print("Done")

    return img

def main():
    if len(sys.argv) < 2: #se o usuario não digitar todos os parametros, sai
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)

    img = Image.open(sys.argv[1]) # img = imagem do parametro

    print("1 - Brilho aditivo em RGB")
    print("2 - Brilho multiplicativo em RGB")
    print("3 - Brilho aditivo em Y")
    print("4 - Brilho multiplicativo em Y")
    print("0 - Sair")

    option = int(input("Escolha um opção: ")) #lê inteiro

    if option == 1:
        plus = float(input("Digite o valor a ser adicionado: ")) #lê valor que o usuario deseja para brilho
        im = aditive_brightness(img, plus) #im recebe a imagem retornada pela função
        im = Image.fromarray(im) #salva imagem
        img.show() #exibe imagem antes da aplicação da função
        im.show()  #exibe imagem depois da aplicação da função

    elif option == 2:
        mult = float(input("Digite o valor a ser multiplicado: ")) 
        im = multiplicative_brightness(img, mult)
        im = Image.fromarray(im)
        img.show()
        im.show()

    elif option == 3:
        plus = float(input("Digite o valor a ser adicionado: "))
        im = yiq.rgb2yiq(img) #converte a imagem rgb para yiq
        im = aditive_brightness_y(im, img.width, img.height, plus) #im recebe imagem retornada pela função
        im = yiq.yiq2rgb(im, img.width, img.height) #converte imagem yiq em rgb
        im = Image.fromarray(im) #salva imagem
        img.show() #exibe imagem antes do processamento
        im.show() #exibe imagem depois do processamento

    elif option == 4:
        mult = float(input("Digite o valor a ser multiplicado: "))
        im = yiq.rgb2yiq(img)
        im = multiplicative_brightness_y(im, img.width, img.height, mult)
        im = yiq.yiq2rgb(im, img.width, img.height)
        im = Image.fromarray(im)
        img.show()
        im.show()

    else:
        print("Bye")
        sys.exit(0)

if __name__ == "__main__":
    main()
