% Conversão de imagem para Negativo

img = imread('IMG_0103.png');
% Extraimos as bandas da imagem
red_channel = img( :, :, 1);
green_channel = img( :, :, 2);
blue_channel = img( :, :, 3);

% Para tirar o negativo, temos q transformar os valores proximos
% de 0 em valores proximos de 255, e vice-versa
% Para isto subtraimos a imagem por 255 e multiplicamos por -1
% Fazemos isto banda a banda
neg_red = uint8(-1*(double(red_channel)-255)); % Negativo na banda R
neg_green = uint8(-1*(double(green_channel)-255)); % Negativo na banda G
neg_blue = uint8(-1*(double(blue_channel)-255)); % Negativo na banda B

image_final = cat(3, neg_red, neg_green, neg_blue); % Imagem final RGB, juntando todos os negativos.

imshow(image_final); % exibe a imagem