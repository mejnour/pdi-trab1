% Aplicação do Filtro da Mediana

img = imread('porta.jpg');
img = rgb2gray(img); %transforma a imagem em niveis de cinza

%img_noise = imnoise(img, 'salt & pepper', 0.02); %adiciona ruido salt and pepper a imagem
 
med_filt = medfilt2(img_noise, [5 5]); %aplica o filtro da mediana 3x3 na imagem

%imshow(img_noise); %exibe a imagem com ruidos
imshow(med_filt); % exibe o resultado