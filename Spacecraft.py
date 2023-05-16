import pygame

# screen dimensions
width = 800
height = 600


# Class to represent the spaceship
class SpaceCraft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('nave.png').convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height - 10
        self.velocidad_x = 0
        self.vidas = 4
        self.explotado = False
        self.explotado_tiempo = 0

    def update(self):
        if not self.explotado:
            self.rect.x += self.velocidad_x
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > width:
                self.rect.right = width
        else:
            # Lógica para mostrar una animación de explosión cuando la nave está explotada
            self.image = pygame.image.load('explosion.png').convert()
            self.rect = self.image.get_rect()
            self.rect.centerx = width // 2
            self.rect.bottom = height - 10

    def mover_izquierda(self):
        self.velocidad_x = -5

    def mover_derecha(self):
        self.velocidad_x = 5

    def detener(self):
        self.velocidad_x = 0

    def explotar(self):
        if not self.explotado:
            self.explotado = True
            self.vidas -= 1

