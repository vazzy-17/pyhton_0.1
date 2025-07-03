# instalasi pygame dan hello window
# fokkus menyiapkan pyame dan menampilkan jendela game pertama

import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("game pertama ku")

running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

pygame.quit()

# latihan 
# ubah ukuran layar
# tambahkan warna background dengan scree.fill((r,g,b))