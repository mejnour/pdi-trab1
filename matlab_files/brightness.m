% Controle de brilho em imagens RGB

img = imread('mulher.jpg'); %le a imagem


% --------- BRILHO ADITIVO ----------

% Para adicionar brilho aditivo em uma imagem,
% basta somar um valor a cada banda da imagem.
n = 100; % valor do brilho a ser somado.

% Extrai as bandas individuais
red_channel = img( :, :, 1);
green_channel = img( :, :, 2);
blue_channel = img( :, :, 3);

% Soma o valor N de brilho aos Canais
red_bright = red_channel + n;
green_bright = green_channel + n;
blue_bright = blue_channel + n;

image_final_1 = cat(3, red_bright, green_bright, blue_bright); %Soma as 3 bandas em uma imagem final

imshow(image_final_1); % Exibe o resultado do brilho aditivo


% --------- BRILHO MULTIPLICATIVO ----------
% Para adicionar brilho multiplicativo em uma imagem,
% basta multiplicar um valor real a cada banda da imagem.

m = 5.0; % valor real de brilho a ser multiplicado

% Extrai as bandas individuais
red_channel_2 = img( :, :, 1);
green_channel_2 = img( :, :, 2);
blue_channel_2 = img( :, :, 3);

% Multiplica o valor M de brilho aos Canais
red_bright_2 = red_channel * n;
green_bright_2 = green_channel * n;
blue_bright_2 = blue_channel * n;

image_final_2 = cat(3, red_bright_2, green_bright_2, blue_bright_2); %Soma as 3 bandas em uma imagem final

imshow(image_final_2); % Exibe a imagem final

