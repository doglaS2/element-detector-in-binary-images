import os
import cv2
import numpy as np
from skimage import measure
import matplotlib.pyplot as plt

# definir o caminho para o arquivo de imagem na pasta data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, '..', 'data')
image_path = os.path.join(data_dir, 'imagem_meteoro.png')

# carregar a imagem
image_color = cv2.imread(image_path)

# verificar se a imagem foi carregada corretamente
if image_color is None:
    print("Erro ao carregar a imagem.")
else:
    print("Imagem carregada com sucesso.")

    # converte a imagem de BGR para RGB
    image_rgb = cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB)

    # cria uma máscara para pixels brancos
    white_mask = np.all(image_rgb >= 240, axis=-1)
    white_pixels = np.uint8(white_mask) * 255  # Binário: 255 para branco, 0 para não-branco

    # identificar estrelas na imagem binária
    labels = measure.label(white_pixels, connectivity=2, background=0)
    star_count = np.max(labels)  # contar as estrelas

    print(f'número de estrelas encontradas: {star_count}')

    # exibir ambas as imagens
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Imagem Original')
    plt.imshow(image_rgb)

    plt.subplot(1, 2, 2)
    plt.title('Estrelas Detectadas')
    plt.imshow(white_pixels, cmap='gray')

    plt.show()
