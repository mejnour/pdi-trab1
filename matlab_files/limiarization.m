% Exemplos de Limiarização

img = imread('iMG_0103.png');
img = rgb2gray(img);

%histogram(img);
n = input('Digite o valor de Limiarização desejado:');
% Foi escolhido o nivel 128 como base.
case_one = img < n; %temos niveis menores que N
case_two = img > n; %temos niveis maiores que N

%imshow(case_one); %exibe baseado no caso 1
imshow(case_two); %exibe baseado no caso 2
