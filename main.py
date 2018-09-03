import brilho
import convolucao as convo
import filtros
import canais
import media
import negativo
import sobel
import thresholding as thres
import yiq
import sys

def main():
    print("- - - - - - - - - - - - - - - - - - - - - - - -")
    print("Universidade Federal da Paraíba - U.F.P.B.")
    print("Introdução ao Processamento Digital de Imagens\n")
    print("\t\tTrabalho Primeiro\n")
    print("Choose Your Destiny:\n")
    print("1 - Brilho")
    print("2 - Canais")
    print("3 - Convolucao")
    print("4 - Filtros")
    print("5 - Media e Mediana")
    print("6 - Negativo")
    print("7 - Sobel/Laplace")
    print("8 - Thresholding")
    print("0 - Sair")
    print("- - - - - - - - - - - - - - - - - - - - - - - -")
    destiny = int(input("> "))

    if destiny == 1:
        brilho.main()
    # elif destiny == 2:
    # elif destiny == 3:
    # elif destiny == 4:
    # elif destiny == 5:
    # elif destiny == 6:
    # elif destiny == 7:
    # elif destiny == 8:
    # elif destiny == 9:
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
