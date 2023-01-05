import pygame
import random
import math
from pygame import mixer

# inicializar
pygame.init()

# pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo e icono

pygame.display.set_caption("Invacion chavista")
icono = pygame.image.load("chavez.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")


# sonido

mixer.music.load("16.3 MusicaFondo.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# variables jugador

img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_cambio = 0

# variables enemigo

img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for a in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("chavez2.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(2)
    enemigo_y_cambio.append(50)


# variable bala

img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 10
bala_visible = False

# puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# funcion fin

fuente_final = pygame.font.Font("freesansbold.ttf", 40)


def texto_final():
    mi_fuente_final = fuente_final.render(
        "MAMATE UN GUEVO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (220, 200))

# funcion puntaje


def mostrar_puntaje(x, y):
    texto = fuente.render(f"puntaje:{puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))
# funcion enemigo


def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# funcion jugador


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# funcion bala


def bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x+16, y+10))

# funcion colision


def hay_colision(x1, y1, x2, y2):

    distancia = math.sqrt(math.pow(y2 - y1, 2)+math.pow(x2 - x1, 2))
    if distancia < 27:
        return True
    else:
        return False


# ejecucion
ejecucion = True

while ejecucion:
    # rgb pantalla
    pantalla.blit(fondo, (0, 0))
    for evento in pygame.event.get():
        # cerrar
        if evento.type == pygame.QUIT:
            ejecucion = False
        # mover
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_cambio = -4
            if evento.key == pygame.K_RIGHT:
                jugador_cambio = 4
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("16.1 disparo.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    bala(bala_x, bala_y)
        # soltar tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_cambio = 0
    # actualizar pocision del jugador
    jugador_x += jugador_cambio

    # limites del jugardor
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # actualizar pocision del enemigo
    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[e] > 470:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # limites del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -3
            enemigo_y[e] += enemigo_y_cambio[e]
        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("16.2 Golpe.mp3")
            sonido_colision.play
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # mostrar bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # pocision jugar
    jugador(jugador_x, jugador_y)

    # mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)

    # actualizar
    pygame.display.update()
    # actualizar
    pygame.display.update()
