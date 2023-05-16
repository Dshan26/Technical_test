import pygame
from Enemy import Enemy
from Bala import Missil
from Spacecraft import SpaceCraft

width = 800
height = 600

black = (0, 0, 0)
white = (255, 255, 255)


def main(vidas=4):
    pygame.init()
    pantalla = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PyGame")
    reloj = pygame.time.Clock()

    jugador = SpaceCraft()
    jugadores = pygame.sprite.Group()
    jugadores.add(jugador)

    enemigos = pygame.sprite.Group()
    for _ in range(10):
        enemigo = Enemy()
        enemigos.add(enemigo)

    proyectiles = pygame.sprite.Group()

    jugando = True
    game_over = False  # Bandera para finalizar el juego
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador.mover_izquierda()
                elif evento.key == pygame.K_RIGHT:
                    jugador.mover_derecha()
                elif evento.key == pygame.K_SPACE:
                    if jugador.vidas > 0:
                        proyectil = Missil(jugador.rect.centerx, jugador.rect.top)
                        proyectiles.add(proyectil)
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and jugador.velocidad_x < 0:
                    jugador.detener()
                elif evento.key == pygame.K_RIGHT and jugador.velocidad_x > 0:
                    jugador.detener()

        jugadores.update()
        enemigos.update()
        proyectiles.update()

        # Colisión entre proyectiles y enemigos
        for proyectil in proyectiles:
            enemigos_alcanzados = pygame.sprite.spritecollide(proyectil, enemigos, True)
            for _ in enemigos_alcanzados:
                proyectil.kill()

        if pygame.sprite.spritecollide(jugador, enemigos, True):
            vidas -= 1
            if vidas == 0:
                jugador.explotar()
                pantalla.fill(black)
                pygame.display.flip()
                jugador.update()
                pygame.time.wait(3)
                jugando = False

        pantalla.fill(black)
        jugadores.draw(pantalla)
        enemigos.draw(pantalla)
        proyectiles.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
