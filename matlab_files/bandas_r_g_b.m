% Exibe bandas individuais R,G,B
img = imread('porta.jpg');

% Extrai os canais individuais de RGB
% Eles estão em escala monocromática de cinza
red_channel = img( :, :, 1);
green_channel = img( :, :, 2);
blue_channel = img( :, :, 3);

% ------- Cria uma imagem RGB -----------
z = zeros(size(red_channel)); %cria uma matriz de zeros.

red_image = cat(3, red_channel, z, z); %Cria uma Imagem de banda R, com G e B zerados
green_image = cat(3, z, green_channel, z); %Cria uma Imagem de banda G, com R e B zerados
blue_image = cat(3, z, z, blue_channel); %Cria uma Imagem de banda B, com R e G zerados

imshow(red_image); % Exibe a imagem na banda R
imshow(green_image); % Exibe a imagem na banda G
imshow(blue_image); % Exibe a Imagem na banda B
