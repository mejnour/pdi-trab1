import convolution as conv
from PIL import Image
import numpy as np
import sys

#Essa função usa a função conv image para convolucionar a imagem usando os filtro desejado
def apply_filter(image, kernel):
    return conv.conv_image(image, kernel)

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1])
    
    #Nesse filtro os pixels com maiores frequências são realçados, deixando a imagem com bordas e detalhes mais marcantes,
    #mas em compensação é aumentado o número de ruidos
    kernel1 = np.array([[0,-1,0],
                        [-1,5,-1],
                        [0,-1,0]])
    
    #Nesse filtro de realce de bordas, onde a imagem é deslocada e subtraída da imagem original
    kernel2 = np.array([[0,0,0],
                        [0,1,0],
                        [0,0,-1]])
    
    print("1 - Aplicar filtro ", kernel1[0], "\n\t\t   ", kernel1[1], "\n\t\t   ", kernel1[2])
    print("\n2 - Aplicar filtro ", kernel2[0], "\n\t\t   ", kernel2[1], "\n\t\t   ", kernel2[2])
    print("0 - Sair")
    
    option = int(input("\nSelecione uma opção: "))
    
    if option == 1:
        im = apply_filter(img, kernel1)
        im = Image.fromarray(im)
        im.show()
        
    elif option == 2:
        im = apply_filter(img, kernel2)
        im = Image.fromarray(im)
        im.show()
        
    else:
        sys.exit()
    
if __name__ == "__main__":
    main()
    
