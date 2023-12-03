# -*- coding: utf-8 -*-
import math
from PIL import Image

'''
Cria uma imagem com um degrade racial em degrade com camada alpha tendo 5 variaveis:
altura, largura e raio
degrade: valor inicial
taixa_de_variacao: a taixa q varia o degrade

voce pode alterar o raio e a densidade do degrade mudando e mesclando 
os valores de raio, degrade e taixa_de_variacao

salvando sempre como "alpha.png"
'''

altura = 25
largura = 25
raio = 135
degrade = 10
taixa_de_variacao =  8

tela = Image.new ("RGBA", (altura, largura), (0, 0, 0))
centro = [int(altura/2),int(largura/2)]

for r in range(raio):
	for x in range(altura):
		for y in range(largura):
			if r == int(math.sqrt(((centro[0]-x)*(centro[0]-x)) + ((centro[1]-y)*(centro[1]-y)))):
				tela.putpixel((x,y),(0,0,0,degrade))
	degrade = degrade + taixa_de_variacao

tela.save("alpha.png")
