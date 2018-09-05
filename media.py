import numpy as np
from PIL import Image
from math import ceil
import sys


# Calculasse a média, somando todos os valores e dividindo pelo tamanho do
# array recebido
def mean(arr):
    m = 0
    for k in arr:
        m += k

    return int(m/len(arr))


# Calculasse a mediana, dividindo o tamanho do array por 2 e acessando dire-
# tamente o valor no array depois de ordenado
# Caso seja par os dois centrais são somados e dividido por dois, caso impar
# o elemento central é retornado
def median(arr):
    size = len(arr)
    arr = list(np.sort(arr))

    if size % 2 == 0:
        return int((arr[int(size/2)] + arr[int(size/2+1)])/2)
    else:
        return arr[int(size/2) + 1]


# Nessa função é acessado os pixels desejados, e retorna o valores de RGB do
# pixels. Os calculos sao um pouco mais complexos que o normal, pois tem-se que
# retornar o numero de pixels correspondente ao tamanho do kernel escolhido.
def get_pixels(img, x, y, size):
    # im = np.zeros((img.height, img.width, 3), 'uint8')
    r = []
    g = []
    b = []
    limit = range(-size + ceil(size/2), size - int(size/2)+1)
    L = abs(min(limit))
    U = max(limit)

    for j in range(y-L, y+U):
        for i in range(x-L, x+U):
            for band in range(3):
                if band == 0:
                    try:
                        r.append(img.getpixel((i, j))[0])
                    except:
                        r.append(0)
                elif band == 1:
                    try:
                        g.append(img.getpixel((i, j))[1])
                    except:
                        g.append(0)
                else:
                    try:
                        b.append(img.getpixel((i, j))[2])
                    except:
                        b.append(0)

    return (r, g, b)


# Filtro de média, ao receber a imagem e o tamanho do kernel, são acessados
# os pixels e calculado a média de valores de acordo com o tamanho do kernel
# escolhido
def mean_filter(img, size):
    copy = img.copy()

    for j in range(img.height):
        for i in range(img.width):
            r, g, b = get_pixels(img, i, j, size)
            r = mean(r)
            g = mean(g)
            b = mean(b)

            copy.putpixel((i, j), (r, g, b))

    return copy


# Filtro de mediana, ao receber a imagem e o tamanho do kernel, são acessados
# os pixels e calculado o valor da mediana de acordo com o tamanho do kernel
# escolhido
def median_filter(img, size):
    copy = img.copy()

    for j in range(img.height):
        for i in range(img.width):
            r, g, b = get_pixels(img, i, j, size)
            r = median(r)
            g = median(g)
            b = median(b)

            copy.putpixel((i, j), (r, g, b))

    return copy


def main(path):

    img = Image.open(path)

    while 1:
        print("\n\tMenu Media:\n")
        print("\t1 - Aplicar filtro de média")
        print("\t2 - Aplicar filtro de mediana")
        print("\t0 - Sair")

        option = int(input("\t> "))

        if option == 1:
            size = int(input("\n\t\tDigite o tamanho do kernel: "))
            im = mean_filter(img, size)
            im.show()

        elif option == 2:
            size = int(input("\n\t\tDigite o tamanho do kernel: "))
            im = median_filter(img, size)
            im.show()

        else:
            return
