import numpy as np
from PIL import Image
import yiq
import sys


# Limiarização pré definida, aqui se faz um limiar usando o valor enviado pelo
# usuário, após dividido por 255 o valor é então usado como comparador para
# se alterar o valor de Y entre 1 e 0
def threshold_user(image, thresh):
    thresh /= 255

    img = np.zeros((image.height, image.width, 3), 'float32')
    im = yiq.rgb2yiq(image)

    for j in range(image.height):
        for i in range(image.width):
            # img[j, i, 0] = im[j, i, 0]

            if im[j, i, 0] <= thresh:
                img[j, i, 0] = 0
            else:
                img[j, i, 0] = 1

    return img


# Nessa limiarização, é feito o cálculo da média de Y em todos os pixels,
# dividido por sua quantidade, e então é usado como comparativo para alterar
# o valor de y entre 1 e 0
def threshold_mean(image):
    img = np.zeros((image.height, image.width, 3), 'float32')
    im = yiq.rgb2yiq(image)

    thresh = 0
    for j in range(image.height):
        for i in range(image.width):
            img[j, i, 0] = im[j, i, 0]
            thresh += img[j, i, 0]

    thresh /= (image.width * image.height)

    for j in range(image.height):
        for i in range(image.width):
            if img[j, i, 0] <= thresh:
                img[j, i, 0] = 0
            else:
                img[j, i, 0] = 1

    return img


def main(path):

    img = Image.open(path)

    while 1:
        print("\n\tMenu Limiarizacao:\n")
        print("\t1 - Limiar definido pelo usuário")
        print("\t2 - Limiar por média de valores em Y")
        print("\t0 - Voltar ao Menu Principal")

        option = int(input("\t> "))

        if option == 1:
            thresh = int(input("\t\tDigite o limiar: "))
            im = threshold_user(img, thresh)
            im = yiq.yiq2rgb(im, img.width, img.height)
            im = Image.fromarray(im)
            im.show()

        if option == 2:
            im = threshold_mean(img)
            im = yiq.yiq2rgb(im, img.width, img.height)
            im = Image.fromarray(im)
            im.show()

        else:
            return
