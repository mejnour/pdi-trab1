%Convolução SOBEL / MEDIA

img = imread('porta.jpg');
img = rgb2gray(img); %transforma a imagem em niveis de cinza

% ------- DETECÇÃO DE BORDAS DE SOBEL ------- 

img_sobel = edge(img); % Detecta bordas com filtro de Sobel
%imshow(img_sobel); % exibe a imagem 


% -------- FILTRO DA MEDIA -------- 

img_media = conv2(double(img), ones(3)/9); % Aplica convolução com matriz 3x3 de filtro da media
img_media = conv2(double(img), ones(5)/25); % 5x5

imshow(uint8(img_media));%exibe o resultado


