# -*- coding: utf-8 -*-
import pygame
import numpy as np
from PIL import Image
#  pyinstaller Criador_de_ruido_3.py --onefile --noconsole     <- TRANSFORMA ARQUIVOS .PY EM .EXE

try:
    pygame.init()
except:
    print("O modulo não foi inicializado com sucesso")

pygame.font.init()

fonte_teste = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",12)

largura = 600
altura = 400

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)

lightblue = (0,191,255)
blue = (65,105,225)
darkblue = (85,125,245)
green = (34,139,34)
darkgreen = (0,100,0)
sandy = (238, 214, 175)
snow = (255, 250, 250)
mountain = (139, 137, 137)

blu = 50
darkblu = 90
sand = 108
gree = 144
darkgree = 180
mountai = 216
sno = 255

sair = True

tela = pygame.display.set_mode((largura,altura))

def render():

    noise = Image.open("IMAGEMTESTE.png")
    mapa = Image.new ("RGBA", (noise.size[0], noise.size[1]), (0, 0, 0))
    pixel = mapa.load()

    for x in range(noise.size[0]):
        for y in range(noise.size[1]):
            if noise.getpixel((x,y))[0] <  blu:
                pixel[x,y] = blue
            elif noise.getpixel((x,y))[0] < darkblu:
                pixel[x,y] = darkblue
            elif noise.getpixel((x,y))[0] < sand:
                pixel[x,y] = sandy
            elif noise.getpixel((x,y))[0] < gree:
                pixel[x,y] = green
            elif noise.getpixel((x,y))[0] < darkgree:
                pixel[x,y] = darkgreen
            elif noise.getpixel((x,y))[0] < mountai:
                pixel[x,y] = mountain
            elif noise.getpixel((x,y))[0] <= sno:
                pixel[x,y] = snow
    mapa.save("mapa.png")

render()

posicao = 0
c1 = preto
c2 = preto
c3 = preto
c4 = preto
c5 = preto
c6 = preto

modificador = 1.0

pygame.display.set_caption("Criador de Ruido de Perlin")

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rect = pygame.Rect(0, 0, largura, altura)
            sub = tela.subsurface(rect)
            pygame.image.save(sub, "screenshot_map.png")
            sair = False

    imagem = pygame.image.load("mapa.png") #<type 'pygame.Surface'>
    tela.fill(branco)
    tela.blit(imagem, (0, 0))

    pygame.draw.rect(tela, preto, [400,0, 1,400])
    pygame.draw.rect(tela, preto, [400,210, 300,1])

    texto = fonte_teste.render("1_BLUE", 1, c1)
    tela.blit(texto, (410, 10))
    texto = fonte_teste.render(str(blu), 1, c1)
    tela.blit(texto, (510, 10))

    texto = fonte_teste.render("2_DARKBLUE", 1, c2)
    tela.blit(texto, (410, 35))
    texto = fonte_teste.render(str(darkblu), 1, c2)
    tela.blit(texto, (510, 35))

    texto = fonte_teste.render("3_SANDY", 1, c3)
    tela.blit(texto, (410, 60))
    texto = fonte_teste.render(str(sand), 1, c3)
    tela.blit(texto, (510, 60))

    texto = fonte_teste.render("4_GREEN", 1, c4)
    tela.blit(texto, (410, 85))
    texto = fonte_teste.render(str(int(gree)), 1, c4)
    tela.blit(texto, (510, 85))

    texto = fonte_teste.render("5_DRAKGREEN", 1, c5)
    tela.blit(texto, (410, 110))
    texto = fonte_teste.render(str(darkgree), 1, c5)
    tela.blit(texto, (510, 110))

    texto = fonte_teste.render("6_MOUNTAIN", 1, c6)
    tela.blit(texto, (410, 135))
    texto = fonte_teste.render(str(mountai), 1, c6)
    tela.blit(texto, (510, 135))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        c2 = c3 = c4 = c5 = c6 = preto
        c1 = vermelho
        posicao = 1
    if keys[pygame.K_2]:
        c1 = c3 = c4 = c5 = c6 = preto
        c2 = vermelho
        posicao = 2
    if keys[pygame.K_3]:
        c1 = c2 = c4 = c5 = c6 = preto
        c3 = vermelho
        posicao = 3
    if keys[pygame.K_4]:
        c1 = c2 = c3 = c5 = c6 = preto
        c4 = vermelho
        posicao = 4
    if keys[pygame.K_5]:
        c1 = c2 = c3 = c4 = c6 = preto
        c5 = vermelho
        posicao = 5
    if keys[pygame.K_6]:
        c1 = c2 = c3 = c4 = c5 = preto
        c6 = vermelho
        posicao = 6


    if keys[pygame.K_LEFT]:
        if posicao == 1:
            blu = blu - int(modificador)
            render()
        if posicao == 2:
            darkblu = darkblu - int(modificador)
            render()
        if posicao == 3:
            sand = sand - int(modificador)
            render()
        if posicao == 4:
            gree = gree - int(modificador)
            render()
        if posicao == 5:
            darkgree = darkgree - int(modificador)
            render()
        if posicao == 6:
            mountai = mountai - int(modificador)
            render()


    if keys[pygame.K_RIGHT]:
        if posicao == 1:
            blu = blu + int(modificador)
            render()
        if posicao == 2:
            darkblu = darkblu + int(modificador)
            render()
        if posicao == 3:
            sand = sand + int(modificador)
            render()
        if posicao == 4:
            gree = gree + int(modificador)
            render()
        if posicao == 5:
            darkgree = darkgree + int(modificador)
            render()
        if posicao == 6:
            mountai = mountai + int(modificador)
            render()

    pygame.display.update()
pygame.quit()