# -*- coding: utf-8 -*-
import noise
import numpy as np
from PIL import Image


octaves = 6
persistence = 1.6
lacunarity = 2.3
scale = 230.0
seed = 27
grau = 450
potencializar = 120
shap = 25
shape = ([shap,shap])


branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)

blue = (65,105,225)
darkblue = (85,125,245)
green = (34,139,34)
darkgreen = (0,100,0)
sandy = (238, 214, 175)
snow = (255, 250, 250)
mountain = (139, 137, 137)

blu = 20
darkblu = 60
sand = 90
gree = 120
darkgree = 200
mountai = 255
sno = 255


#filtro = Image.open("alpha25.png").convert("RGBA")

def render():
    shape[0] = shap
    shape[1] = shap
    world = np.zeros(shape)
    lista = np.zeros(shape)
    tela = Image.new ("RGBA", shape, (0, 0, 0))
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = (noise.pnoise2(i/scale, j/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=1024, repeaty=1024, base=seed) * grau) + potencializar
            tela.putpixel((i,j),(int(world[i][j]),int(world[i][j]),int(world[i][j]),255))

    tela.save("IMAGEMTESTE20.png")




    mesclagem = Image.new ("RGBA", (tela.size[0], tela.size[1]), (0, 0, 0))
    centro = [int(tela.size[0]/2),int(tela.size[1]/2)]

    pixel = mesclagem.load()

    for x in range(tela.size[0]):
        for y in range(tela.size[1]):
            n = tela.getpixel((x,y))
            #f = filtro.getpixel((x,y))
            #pixel[x,y] = (n[0]-int(f[3]/1.5),n[1]-int(f[3]/1.5),n[2]-int(f[3]/1.5),n[3])
            pixel[x,y] = tela.getpixel((x,y))

    mesclagem.save("mesclagem20.png")





    mapa = Image.new ("RGBA", (mesclagem.size[0], mesclagem.size[1]), (0, 0, 0))
    pixel = mapa.load()
    somay = 16
    somax = 0

    somax2 = 16 #COLUNA
    somay2 = 0  #LINHA

    correr = 0

    for x in range(mesclagem.size[0]):
        for y in range(mesclagem.size[1]):
            if x == somax and y == somay:
                pixel[x,y] = (255,0,255, 255)
                somay = somay + 1
            elif x == somax2 and y == somay2 and somay2 <= correr:
                pixel[x,y] = (255,0,255, 255)
                somay2 = somay2 + 1
            elif mesclagem.getpixel((x,y))[0] == 91 or mesclagem.getpixel((x,y))[0] == 100:
                pixel[x,y] = (255,0,0, 255)
            elif mesclagem.getpixel((x,y))[0] <  blu:
                pixel[x,y] = blue
            elif mesclagem.getpixel((x,y))[0] < darkblu:
                pixel[x,y] = darkblue
            elif mesclagem.getpixel((x,y))[0] < sand:
                pixel[x,y] = sandy
            elif mesclagem.getpixel((x,y))[0] < gree:
                pixel[x,y] = green
            elif mesclagem.getpixel((x,y))[0] < darkgree:
                pixel[x,y] = darkgreen
            elif mesclagem.getpixel((x,y))[0] == 208 or mesclagem.getpixel((x,y))[0] == 196:
                pixel[x,y] = (255,255,0,255)
            elif mesclagem.getpixel((x,y))[0] <= mountai:
                pixel[x,y] = mountain

        somay = 17 + x 
        somax = somax + 1 

        somay2 = 0 

        if x == somax2:
            somax2 = x + 1
            correr = correr + 1


    mapa.save("mapa20.png")

render()
