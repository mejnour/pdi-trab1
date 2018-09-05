import brilho
import convolucao as convo
import filtros
import canais
import media
import negativo
import sobel_laplace as sobel
import limiarizacao as thres
import sys


def main():
    print("- - - - - - - - - - - - - - - - - - - - - - - -")
    print("Universidade Federal da Paraíba - U.F.P.B.")
    print("Introdução ao Processamento Digital de Imagens\n")

    print("\t\tTrabalho Primeiro\n")

    print("Entre o caminho do arquivo a ser trabalhado:\n")
    path = str(input("> "))

    while 1:
        print("\nMenu Principal:\n")
        print("1 - Brilho")
        print("2 - Canais")
        print("3 - Convolucao")
        print("4 - Filtros")
        print("5 - Media e Mediana")
        print("6 - Negativo")
        print("7 - Sobel/Laplace")
        print("8 - Limiarizacao")
        print("9 - Arquivo")
        print("0 - Sair")
        destiny = int(input("> "))

        if destiny == 1:
            brilho.main(path)

        elif destiny == 2:
            canais.main(path)

        elif destiny == 3:
            convo.main(path)

        elif destiny == 4:
            filtros.main(path)

        elif destiny == 5:
            media.main(path)

        elif destiny == 6:
            negativo.main(path)

        elif destiny == 7:
            sobel.main(path)

        elif destiny == 8:
            thres.main(path)

        elif destiny == 9:
            print("\nChoose Your File:\n")
            path = str(input("> "))

        else:
            print("- - - - - - - - - - - - - - - - - - - - - - - -")
            sys.exit(0)


if __name__ == '__main__':
    main()
