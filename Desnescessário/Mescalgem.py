# -*- coding: utf-8 -*-
import math
from PIL import Image

'''
Mesclagem faz a mescla entre duas imagens a noise_teste.png
e alpha.png e salva uma nova imagem, mesclagem.png

lembrando que tanto a noise_teste.png quanto a alpha.png
precisam estar junto ao programa
'''

noise = Image.open("noise_teste.png").convert("RGBA")
filtro = Image.open("alpha.png").convert("RGBA")
mesclagem = Image.new ("RGBA", (noise.size[0], noise.size[1]), (0, 0, 0))
centro = [int(noise.size[0]/2),int(noise.size[1]/2)]
#print(tela.mode,tela.size,tela.format)
pixel = mesclagem.load()

for x in range(noise.size[0]):
	for y in range(noise.size[1]):
		n = noise.getpixel((x,y))
		f = filtro.getpixel((x,y))
		pixel[x,y] = (n[0]-int(f[3]/1.5),n[1]-int(f[3]/1.5),n[2]-int(f[3]/1.5),n[3])

mesclagem.save("mesclagem.png")