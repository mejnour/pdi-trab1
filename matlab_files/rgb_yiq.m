% Conversão RGB para YIQ | YIQ para RGB

rgb = imread('mulher.jpg');

%Converte RGB para YIQ
yiq = rgb2ntsc(rgb); %converte rgb para yiq
imshow(yiq); %exibe a imagem após a conversão

%Converte YIQ para RGB
new_rgb = ntsc2rgb(yiq); %converte yiq para rgb
imshow(new_rgb);  %exibe a imagem após a conversão

