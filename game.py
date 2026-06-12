from pygame import *
import sys

init()
screen = display.set_mode((1280,720))
display.set_caption("Fuga da Masmorra")
clock = time.Clock()

mapa = image.load("fundos_masmorra/piso1.png")



while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    clock.tick(60)
    dt = clock.get_time()

    screen.fill((255,255,255)) # Fundo Branco

    screen.blit(mapa,(600,675),(0,0,32,45))
    screen.blit(mapa,(500,675),(45,0,32,45))
    screen.blit(mapa,(400,675),(90,0,32,45))
    screen.blit(mapa,(300,675),(135,0,32,45))
    screen.blit(mapa,(200,675),(180,0,32,45))
    screen.blit(mapa,(100,675),(250,0,32,45))

    display.update()