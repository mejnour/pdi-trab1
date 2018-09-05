import convolucao as conv
from PIL import Image
import numpy as np


# Essa função usa a função conv image para convolucionar a imagem usando os
# filtros desejado
def apply_filter(image, kernel):
    return conv.conv_image(image, kernel)


def main(path):

    img = Image.open(path)

    # Nesse filtro os pixels com maiores frequências são realçados, deixando a
    # imagem com bordas e detalhes mais marcantes, mas em compensação é aumen-
    # tado o número de ruidos
    kernel1 = np.array([[0,  -1,  0],
                        [-1,  5, -1],
                        [0,  -1,  0]])

    # Nesse filtro de realce de bordas, onde a imagem é deslocada e subtraída
    # da imagem original
    kernel2 = np.array([[0,   0,  0],
                        [0,   1,  0],
                        [0,   0, -1]])

    print("\n\tMenu Filtros:\n")
    print("\t1 - Aplicar filtro ", kernel1[0],
                    "\n\t\t\t   ", kernel1[1],
                    "\n\t\t\t   ", kernel1[2])

    print("\t2 - Aplicar filtro ", kernel2[0],
                    "\n\t\t\t   ", kernel2[1],
                    "\n\t\t\t   ", kernel2[2])
    print("\t0 - Voltar ao Menu Principal")

    option = int(input("\t> "))

    if option == 1:
        im = apply_filter(img, kernel1)
        im = Image.fromarray(im)
        im.show()

    elif option == 2:
        im = apply_filter(img, kernel2)
        im = Image.fromarray(im)
        im.show()

    else:
        return
