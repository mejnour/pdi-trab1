import numpy as np
from PIL import Image
from math import ceil, sqrt
import convolucao as conv


# Instancia a função filtro de laplace, o filtro é colocado em uma matriz e
# adicionado a variável kernel e depois usa a função conv para alterar a imagem
# usando o filtro que foi passado para variável
def laplacian_filter(image):
    kernel = np.array([[0,  1,  0],
                       [1, -4,  1],
                       [0,  1,  0]])

    return conv.conv_image(image, kernel)


# Instancia a função filtro de sobel, cria as máscaras para detecção de bordas
# em x e y, depois usa a função conv para alterar a imagem usando essas
# máscaras,no fim é feito o módulo das máscaras e salvo o resultado.
def sobel_filter(image):
    out = np.zeros((image.height, image.width, 3), 'uint8')

    kernel_x = np.array([[1,  0,  -1],
                         [2,  0,  -2],
                         [1,  0,  -1]])
    kernel_y = np.array([[1,   2,  1],
                         [0,   0,  0],
                         [-1, -2, -1]])

    out_x = conv.conv_image(image, kernel_x)
    out_y = conv.conv_image(image, kernel_y)

    for y in range(image.height):
        for x in range(image.width):
            out[y, x, 0] = ceil(sqrt(out_x[y, x, 0]**2 + out_y[y, x, 0]**2))
            out[y, x, 1] = ceil(sqrt(out_x[y, x, 1]**2 + out_y[y, x, 1]**2))
            out[y, x, 2] = ceil(sqrt(out_x[y, x, 2]**2 + out_y[y, x, 2]**2))

    return out


def main(path):

    img = Image.open(path)

    while 1:
        print("\n\tMenu Sobel/Laplace:\n")
        print("\t1 - Aplicar filtro laplaciano")
        print("\t2 - Aplicar filtro de Sobel")
        print("\t0 - Voltar ao Menu Principal")

        option = int(input("\t> "))

        if option == 1:
            im = laplacian_filter(img)
            im = Image.fromarray(im)
            im.show()

        elif option == 2:
            im = sobel_filter(img)
            im = Image.fromarray(im)
            im.show()

        else:
            return
