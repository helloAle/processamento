import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem colorida
imagem = cv2.imread('HD-wallpaper-black-horse-cavalo-preto-cavalo-horse.jpg')

# Separar os canais de cores
(B, G, R) = cv2.split(imagem)

# Criar uma imagem em preto com o mesmo tamanho da imagem original
zeros = np.zeros(imagem.shape[:2], dtype="uint8")

# Exibir os canais separadamente
plt.figure(figsize=(10,7))

# Canal Vermelho
plt.subplot(1, 3, 1)
plt.imshow(cv2.merge([zeros, zeros, R]))
plt.title('Canal Vermelho')

# Canal Verde
plt.subplot(1, 3, 2)
plt.imshow(cv2.merge([zeros, G, zeros]))
plt.title('Canal Verde')

# Canal Azul
plt.subplot(1, 3, 3)
plt.imshow(cv2.merge([B, zeros, zeros]))
plt.title('Canal Azul')

plt.show()