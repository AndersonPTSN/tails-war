# -*- coding: utf-8 -*-
import noise
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

octaves = 8
persistence = 0.6
lacunarity = 2.0
scale = 280.0
seed = 26
grau = 600
potencializar = 100
shap = 50
shape = ([shap,shap])
position = 0

largura = 600
altura = 400

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)

sair = True

tela = pygame.display.set_mode((largura,altura))

def render():
    shape[0] = shap
    shape[1] = shap
    world = np.zeros(shape)
    lista = np.zeros(shape)
    tela = Image.new ("RGBA", shape, (0, 0, 0))
    teste = Image.new ("RGBA", shape, (0, 0, 0))
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = (noise.pnoise2(i/scale, j/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=1024, repeaty=1024, base=seed) * grau) + potencializar
            if j == position:
                #teste.putpixel((i,j),vermelho)
                lista[i][j] = world[i][j]
            else:
                teste.putpixel((i,j),(int(world[i][j]),int(world[i][j]),int(world[i][j]),255))
            tela.putpixel((i,j),(int(world[i][j]),int(world[i][j]),int(world[i][j]),255))

    tela.save("IMAGEMTESTE2.png")
    teste.save("screenshot2.png")

    tela4 = Image.new ("RGBA", shape, (0, 0, 0))
    for i in range(shape[0]):
        for k in range(int(lista[i][position])):
            if k >= 0 and k < shap:
                tela4.putpixel((i,k),branco)


    """ 
    l = ""
    for i in range(shape[0]):
        for j in range(shape[1]):
            l = l + str(int(tela.getpixel((i,j))[0]))

    arquivo = open('superficie.txt', 'w')
    arquivo.write(l)
    arquivo.close()
    """

    tela4.save("tela44.png")

render()

posicao = 0
c1 = preto
c2 = preto
c3 = preto
c4 = preto
c5 = preto
c6 = preto
c7 = preto
c8 = preto
c9 = preto

modificador = 1.0

pygame.display.set_caption("Criador de Ruido de Perlin")

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rect = pygame.Rect(0, 0, largura, altura)
            sub = tela.subsurface(rect)
            pygame.image.save(sub, "screenshot2.png")
            sair = False

    imagem = pygame.image.load("screenshot2.png") #<type 'pygame.Surface'>
    tela.fill(branco)
    tela.blit(imagem, (0, 0))

    imagem = pygame.image.load("tela44.png")
    tela.blit(imagem, (200, 200))

    pygame.draw.rect(tela, preto, [400,0, 1,400])
    pygame.draw.rect(tela, preto, [400,235, 300,1])

    texto = fonte_teste.render("1_OCTAVES", 1, c1)
    tela.blit(texto, (410, 10))
    texto = fonte_teste.render(str(octaves), 1, c1)
    tela.blit(texto, (510, 10))

    texto = fonte_teste.render("2_PERSISTENCE", 1, c2)
    tela.blit(texto, (410, 35))
    texto = fonte_teste.render(str(persistence), 1, c2)
    tela.blit(texto, (510, 35))

    texto = fonte_teste.render("3_LACUNARITY", 1, c3)
    tela.blit(texto, (410, 60))
    texto = fonte_teste.render(str(lacunarity), 1, c3)
    tela.blit(texto, (510, 60))

    texto = fonte_teste.render("4_SCALE", 1, c4)
    tela.blit(texto, (410, 85))
    texto = fonte_teste.render(str(int(scale)), 1, c4)
    tela.blit(texto, (510, 85))

    texto = fonte_teste.render("5_SEED", 1, c5)
    tela.blit(texto, (410, 110))
    texto = fonte_teste.render(str(seed), 1, c5)
    tela.blit(texto, (510, 110))

    texto = fonte_teste.render("6_GRAU", 1, c6)
    tela.blit(texto, (410, 135))
    texto = fonte_teste.render(str(grau), 1, c6)
    tela.blit(texto, (510, 135))

    texto = fonte_teste.render("7_POTENCIA", 1, c7)
    tela.blit(texto, (410, 160))
    texto = fonte_teste.render(str(potencializar), 1, c7)
    tela.blit(texto, (510, 160))

    texto = fonte_teste.render("8_SHAPE", 1, c8)
    tela.blit(texto, (410, 185))
    texto = fonte_teste.render(str(shap), 1, c8)
    tela.blit(texto, (510, 185))

    texto = fonte_teste.render("9_POSIÇÃO", 1, c9)
    tela.blit(texto, (410, 210))
    texto = fonte_teste.render(str(position), 1, c9)
    tela.blit(texto, (510, 210))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = preto
        c1 = vermelho
        posicao = 1
    if keys[pygame.K_2]:
        c1 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = preto
        c2 = vermelho
        posicao = 2
    if keys[pygame.K_3]:
        c1 = c2 = c4 = c5 = c6 = c7 = c8 = c9 = preto
        c3 = vermelho
        posicao = 3
    if keys[pygame.K_4]:
        c1 = c2 = c3 = c5 = c6 = c7 = c8 = c9 = preto
        c4 = vermelho
        posicao = 4
    if keys[pygame.K_5]:
        c1 = c2 = c3 = c4 = c6 = c7 = c8 = c9 = preto
        c5 = vermelho
        posicao = 5
    if keys[pygame.K_6]:
        c1 = c2 = c3 = c4 = c5 = c7 = c8 = c9 = preto
        c6 = vermelho
        posicao = 6
    if keys[pygame.K_7]:
        c1 = c2 = c3 = c4 = c5 = c6 = c8 = c9 = preto
        c7 = vermelho
        posicao = 7
    if keys[pygame.K_8]:
        c1 = c2 = c3 = c4 = c5 = c6 = c7 = c9 = preto
        c8 = vermelho
        posicao = 8
    if keys[pygame.K_9]:
        c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = preto
        c9 = vermelho
        posicao = 9

    if posicao == 1:
        texto = fonte_teste.render("OCTAVES: significa o número", 1, preto)
        tela.blit(texto, (410, 245))
        texto = fonte_teste.render("de passes/camadas do", 1, preto)
        tela.blit(texto, (410, 260))
        texto = fonte_teste.render("algoritmo. Cada passe ", 1, preto)
        tela.blit(texto, (410, 275))
        texto = fonte_teste.render("adiciona mais detalhes", 1, preto)
        tela.blit(texto, (410, 290))
    if posicao == 2:
        texto = fonte_teste.render("PERSISTENCE: número que", 1, preto)
        tela.blit(texto, (410, 245))
        texto = fonte_teste.render("determina quanto cada", 1, preto)
        tela.blit(texto, (410, 260))
        texto = fonte_teste.render("oitava contribui para a", 1, preto)
        tela.blit(texto, (410, 275))
        texto = fonte_teste.render("forma geral (ajusta a amplitude)", 1, preto)
        tela.blit(texto, (410, 290))
    if posicao == 3:
        texto = fonte_teste.render("LACUNARITY: número que", 1, preto)
        tela.blit(texto, (410, 245))
        texto = fonte_teste.render("determina quantos detalhes são", 1, preto)
        tela.blit(texto, (410, 260))
        texto = fonte_teste.render("adicionados ou removidos a", 1, preto)
        tela.blit(texto, (410, 275))
        texto = fonte_teste.render("cada oitava (ajusta a frequência).", 1, preto)
        tela.blit(texto, (410, 290))
    if posicao == 4:
        texto = fonte_teste.render("SCALE: muda a escala do ruido", 1, preto)
        tela.blit(texto, (410, 245))
    if posicao == 5:
        texto = fonte_teste.render("SEED: id unico para imagem ", 1, preto)
        tela.blit(texto, (410, 245))
    if posicao == 6:
        texto = fonte_teste.render("GRAU: muda o valor do pixel", 1, preto)
        tela.blit(texto, (410, 245))
        texto = fonte_teste.render("atravez de um multiplicador", 1, preto)
        tela.blit(texto, (410, 260))
    if posicao == 7:
        texto = fonte_teste.render("POTENCIA: muda o valor do", 1, preto)
        tela.blit(texto, (410, 245))
        texto = fonte_teste.render("pixel atravez de uma adição", 1, preto)
        tela.blit(texto, (410, 260))
    if posicao == 8:
        texto = fonte_teste.render("SHAPE: muda a escala", 1, preto)
        tela.blit(texto, (410, 245))
        texto = fonte_teste.render("da imagem (25 a 400 px)", 1, preto)
        tela.blit(texto, (410, 260))
    if posicao == 9:
        texto = fonte_teste.render("POSIÇÃO: mostra a posicao", 1, preto)
        tela.blit(texto, (410, 245))
        texto = fonte_teste.render("lateral no eixo X", 1, preto)
        tela.blit(texto, (410, 260))


    if keys[pygame.K_LEFT]:
        if posicao == 1:
            if octaves > 1:
                octaves = octaves -  int(modificador)
                render()
        if posicao == 2:
            persistence = persistence - (modificador/10)
            render()
        if posicao == 3:
        	lacunarity =  lacunarity -  (modificador/10)
        	render()
        if posicao == 4:
            if scale > 10:
                scale = scale -  modificador*10
                render()
        if posicao == 5:
            seed = seed - int(modificador)
            render()
        if posicao == 6:
            grau = grau - int(modificador*50)
            render()
        if posicao == 7:
            potencializar = potencializar - int(modificador*10)
            render()
        if posicao == 8:
            if shap > 25:
                shap = shap - int(modificador*25)
                render()
        if posicao == 9:
            if position > 0:
                position = position - int(modificador)
                render()

    if keys[pygame.K_RIGHT]:
        if posicao == 1:
        	octaves = octaves + int(modificador)
        	render()
        if posicao == 2:
        	persistence = persistence + (modificador/10)
        	render()
        if posicao == 3:
        	lacunarity =  lacunarity +  (modificador/10)
        	render()
        if posicao == 4:
            scale = scale +  modificador*10
            render()
        if posicao == 5:
            seed = seed + int(modificador)
            render()
        if posicao == 6:
            grau = grau + int(modificador*50)
            render()
        if posicao == 7:
            potencializar = potencializar + int(modificador*10)
            render()
        if posicao == 8:
            if shap < 400:
                shap = shap + int(modificador*25)
                render()
        if posicao == 9:
            if position < shap - 1:
                position = position + int(modificador)
                render()

    pygame.display.update()
pygame.quit()