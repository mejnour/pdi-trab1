import numpy as np
import yiq
from PIL import Image
import sys


def negative(image):
    # cria um array multidimensional(1x1x3) preenchido por zeros usando as
    # dimensões da
    neg = np.zeros((image.height, image.width, 3), 'uint8')
    # imagem e a quantidade de componentes que existe por cada pixel(RGB)
    for i in range(image.width):
        for j in range(image.height):  # percorre todos os pixels da imagem
            r, g, b = image.getpixel((i, j))  # retorna os valores de r ,g e b
            # do pixel(i,j)

            # subtrai de 255 o valor capturado em r, g e b do pixel
            neg[j, i, 0] = 255 - r
            neg[j, i, 1] = 255 - g
            neg[j, i, 2] = 255 - b

    return neg


def negativeR(image):
    neg = np.zeros((image.height, image.width, 3), 'uint8')
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j))

            # subtrai de 255 o valor capturado em r do pixel
            neg[j, i, 0] = 255 - r
            neg[j, i, 1] = g
            neg[j, i, 2] = b

    return neg


def negativeG(image):
    neg = np.zeros((image.height, image.width, 3), 'uint8')
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j))

            neg[j, i, 0] = r
            # subtrai de 255 o valor capturado em g do pixel
            neg[j, i, 1] = 255 - g
            neg[j, i, 2] = b

    return neg


def negativeB(image):
    neg = np.zeros((image.height, image.width, 3), 'uint8')
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j))

            neg[j, i, 0] = r
            neg[j, i, 1] = g
            # subtrai de 255 o valor capturado em b do pixel
            neg[j, i, 2] = 255 - b

    return neg


def negative_y(image, width, height):
    neg = np.zeros((height, width, 3), 'float32')
    # percorre todos os pixels da imagem
    for k in range(width):
        for j in range(height):
            y = image[j, k, 0]
            i = image[j, k, 1]
            q = image[j, k, 2]

            # realiza a subtração do valor máximo no
            # sistema YIQ e o próprio y capturado no pixel
            neg[j, k, 0] = 1-y
            neg[j, k, 1] = i
            neg[j, k, 2] = q

    return neg


def main(path):

    img = Image.open(path)  # abre a imagem passada como argumento

    while 1:
        print("\n\tMenu Negativo:\n")
        print("\t1 - Aplicar negativo em RGB")
        print("\t2 - Aplicar negativo em R")
        print("\t3 - Aplicar negativo em G")
        print("\t4 - Aplicar negativo em B")
        print("\t5 - Aplicar negativo em Y")
        print("\t0 - Voltar ao Menu Principal")

        option = int(input("Selecione uma opção: "))

        if option == 1:
            # retorna um array após deixar as cores negativas em RGB
            im = negative(img)
            im = Image.fromarray(im)  # constrói a imagem
            im.show()  # mostra a imagem construída

        elif option == 2:
            # retorna um array após deixar as cores negativas em R
            im = negativeR(img)
            im = Image.fromarray(im)
            im.show()

        elif option == 3:
            # retorna um array após deixar as cores negativas em G
            im = negativeG(img)
            im = Image.fromarray(im)
            im.show()

        elif option == 4:
            # retorna um array após deixar as cores negativas em B
            im = negativeB(img)
            im = Image.fromarray(im)
            im.show()

        elif option == 5:
            # converte a imagem de rgb para yiq
            im = yiq.rgb2yiq(img)
            # utiliza a nossa função para deixar deixar a imagem negativa
            im = negative_y(im, img.width, img.height)
            # converte de yiq para rgb
            im = yiq.yiq2rgb(im, img.width, img.height)
            im = Image.fromarray(im)
            im.show()

        else:
            return
