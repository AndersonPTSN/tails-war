
import pygame
from PIL import Image
import math
import numpy as np
import copy
from classes.objeto import Objeto
from classes.jogador import Jogador

import imports

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((35*32,25*32), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
dt = 0
pygame.font.init() 
font = pygame.font.SysFont('Comic Sans MS', 30)

#pygame.mixer.music.play(-1)

shap = 25
shape = ([shap,shap])
position = 0

shape[0] = shap
shape[1] = shap
tela = Image.new ("RGBA", shape, (0, 0, 0))
pix_val = list(imports.im.getdata())


pix = imports.im.load() 
mapa_com_personagens = np.empty((shap, shap), dtype=object)

mar_fundo          = Objeto(-2,-2,  7, 0, -10, -10)
mar_raso           = Objeto(-1,-1,  1, 0, -10, -10)
areia              = Objeto( 0, 0,  2, 0, -10, -10)
planice            = Objeto( 0, 0,  3, 0, -10, -10)
floresta           = Objeto(-1,+1,  4, 0, -10, -10)
montanha           = Objeto(-2,+2,  5, 0, -10, -10)
tijolo             = Objeto( 0,+3,  6, 0, -10, -10)

casa               = Objeto(-10,-10, 10, 0, -10, 0)
casa_azul          = Objeto(-10,-10, 11, 0, -10, 5)
casa_vermelha      = Objeto(-10,-10, 12, 0, -10, 5)

forte              = Objeto(-10,-10, 20, 0, -10, 0)
forte_azul         = Objeto(-10,-10, 21, 0,  1, 10)
forte_vermelho     = Objeto(-10,-10, 22, 0,  1, 10)


guerreiro_azul     = Objeto(-10,-10,-10, 11,  1,  10)
guerreiro_vermelho = Objeto(-10,-10,-10, 12,  1,  10)

arqueiro_azul      = Objeto(-10,-10,-10, 21,  1,  10)
arqueiro_vermelho  = Objeto(-10,-10,-10, 22,  1,  10)

mago_azul          = Objeto(-10,-10,-10, 31,  1,  10)
mago_vermelho      = Objeto(-10,-10,-10, 32,  1,  10)

jogador_azul = Jogador("azul",900)
jogador_vermelho = Jogador("vermelho",900)


def draw1():
    pixel = 32
    for i in range(25):
        for j in range(25):
            if(pix[i,j] == (65, 105, 225, 255)):
                mapa_com_personagens[i,j] = copy.deepcopy(mar_fundo)
            if(pix[i,j] == (85, 125, 245, 255)):
                mapa_com_personagens[i,j] = copy.deepcopy(mar_raso)
            if(pix[i,j] == (238, 214, 175, 255)):
                mapa_com_personagens[i,j] = copy.deepcopy(areia)
            if(pix[i,j] == (34, 139, 34, 255)):
                mapa_com_personagens[i,j] = copy.deepcopy(planice)
            if(pix[i,j] == (0, 100, 0, 255)):
                mapa_com_personagens[i,j] = copy.deepcopy(floresta)
            if(pix[i,j] == (139, 137, 137, 255)):
                mapa_com_personagens[i,j] = copy.deepcopy(montanha)

            if(pix[i,j] == (255,0,0, 255)):
                mapa_com_personagens[i,j] = copy.deepcopy(casa)
            if(pix[i,j] == (255,255,0,255)):
                mapa_com_personagens[i,j] = copy.deepcopy(forte)
            if(pix[i,j] == (255,0,255,255)):
                mapa_com_personagens[i,j] = copy.deepcopy(tijolo)

    mapa_com_personagens[1,19] = copy.deepcopy(casa_azul)
    mapa_com_personagens[5,23] = copy.deepcopy(casa_azul)
    mapa_com_personagens[1,23] = copy.deepcopy(forte_azul)

    mapa_com_personagens[13,13] = copy.deepcopy(forte_azul)

    mapa_com_personagens[19,1] = copy.deepcopy(casa_vermelha)
    mapa_com_personagens[23,5] = copy.deepcopy(casa_vermelha)
    mapa_com_personagens[23,1] = copy.deepcopy(forte_vermelho)

draw1()

def draw():

    for i in range(25):
        for j in range(25):
            if(mapa_com_personagens[i,j].tipo_bloco   == 7): #pix_mar_fundo
                screen.blit(imports.mar_fundo, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 1): #pix_mar_raso
                screen.blit(imports.mar_raso, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 2): #pix_areia
                screen.blit(imports.areia, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 3): #pix_planice
                screen.blit(imports.planice, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 4): #pix_floresta
                screen.blit(imports.floresta, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 5): #pix_montanha
                screen.blit(imports.montanha, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 6): #pix_tijolo
                screen.blit(imports.tijolo, (pixel*i,pixel*j))


            if(mapa_com_personagens[i,j].tipo_bloco   == 10): #pix_casa
                screen.blit(imports.casa_branca, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 11): #pix_casa_azul
                screen.blit(imports.casa_azul, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 12): #pix_casa_vermelha
                screen.blit(imports.casa_vermelha, (pixel*i,pixel*j))

            if(mapa_com_personagens[i,j].tipo_bloco   == 20): #pix_forte
                screen.blit(imports.forte, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 21): #pix_forte_azul
                screen.blit(imports.forte_azul, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_bloco   == 22): #pix_forte_vermelho
                screen.blit(imports.forte_vermelho, (pixel*i,pixel*j))

            if(mapa_com_personagens[i,j].tipo_personagem    == 11): #pix_guerreiro_azul
                screen.blit(imports.guerreiro_azul, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_personagem    == 12): #pix_arqueiro_azul
                screen.blit(imports.arqueiro_azul, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j].tipo_personagem    == 13): #pix_mago_azul
                screen.blit(imports.mago_azul, (pixel*i,pixel*j))

            if(mapa_com_personagens[i,j].ativo_inativo == 0): #pix_mago_azul
                screen.blit(imports.cinza_transparente, (pixel*i,pixel*j))

m = 1
person = 0
vector_onde_pode_andar = [(-1,-1)]
area_de_acao = [(-1,-1)]


def check(x,y,jogador_da_vez):
    global m 
    global person
    global vector_onde_pode_andar
    global area_de_acao
    if (x >= 0 and x <= 24) and (y >=0 and y <=24):
        if mapa_com_personagens[x,y].tipo_bloco   == 6 and mapa_com_personagens[x,y].tipo_personagem    == 0 and m == 1: # == pix_tijolo:
            screen.blit(imports.tijolo_big, (832,180))
            screen.blit(imports.tijolo_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y].tipo_bloco   == 5 and mapa_com_personagens[x,y].tipo_personagem    == 0 and m == 1: # == pix_montanha:
            screen.blit(imports.montanha_128, (832,180))
            screen.blit(imports.montanha_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y].tipo_bloco   == 4 and mapa_com_personagens[x,y].tipo_personagem    == 0 and m == 1:# == pix_floresta:
            screen.blit(imports.floresta_big, (832,180))
            screen.blit(imports.floresta_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y].tipo_bloco   == 3 and mapa_com_personagens[x,y].tipo_personagem    == 0 and m == 1: # == pix_planice:
            screen.blit(imports.planice_big, (832,180))
            screen.blit(imports.planice_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y].tipo_bloco   == 2 and mapa_com_personagens[x,y].tipo_personagem    == 0 and m == 1: # == pix_areia:
            screen.blit(imports.areia_big, (832,180))
            screen.blit(imports.areia_descricao, (832,480))
            return [0,0,0]
        elif mapa_com_personagens[x,y].tipo_bloco   == 1 and mapa_com_personagens[x,y].tipo_personagem    == 0 and m == 1: # == pix_mar_raso:
            screen.blit(imports.mar_raso_big, (832,180))
            screen.blit(imports.mar_raso_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y].tipo_bloco   == 7 and mapa_com_personagens[x,y].tipo_personagem    == 0 and m == 1: # == pix_mar_fundo:
            screen.blit(imports.mar_fundo_big, (832,180))
            screen.blit(imports.mar_fundo_descricao, (832,480))
            return [x,y,0]


        elif mapa_com_personagens[x,y].tipo_personagem  == 11 and m == 1 and jogador_da_vez.time == "azul":
            screen.blit(imports.arqueiro_azul_t, (832,180))
            screen.blit(imports.arqueiro_descricao, (832,480))
            vida = font.render(str(mapa_com_personagens[x,y].vida),font,(0,0,0))
            defesa = font.render(str(mapa_com_personagens[x,y].bonus_defesa),font,(0,0,0))
            ataque = font.render(str(math.ceil(mapa_com_personagens[x,y].vida/2)),font,(0,0,0))
            screen.blit(vida, (920,523))
            screen.blit(defesa, (920,558))
            screen.blit(ataque, (920,595))

            if mapa_com_personagens[x,y].ativo_inativo  == 1:
                andar_x = 4
                andar_y = 4
                tes = 0
                vector_casas = [1,1,2,1,1,2,3,2,1,1,2,3,4,3,2,1,1,2,3,4,5,4,3,2,1,1,2,3,4,3,2,1,1,2,3,2,1,1,2,1,1]
                for a in range(x - andar_x, x + andar_x + 1):
                    for b in range(y - andar_y, y + andar_y + 1):
                        if abs(x - a) + abs(y - b) <= andar_x:
                            if(a >= 0 and a <=24 and b >= 0 and b <=24 ): # DENTRO DA MATRIZ
                                if(a != x or b != y) and mapa_com_personagens[a,b].tipo_bloco   <= 7 and mapa_com_personagens[a,b].ativo_inativo     != 1 and mapa_com_personagens[a,b].tipo_personagem    == 0 : # EVITAR PIZAR ONDE N PODE
                                    if (vector_casas[tes] + mapa_com_personagens[a,b].bonus_distancia  > 0): # MOSTRA ONDE DEVE PISAR
                                        num = font.render(str(vector_casas[tes] + mapa_com_personagens[a,b].bonus_distancia ),font,(0,0,0))
                                        #screen.blit(num,(a*pixel, b*pixel))
                                        screen.blit(imports.cinza_transparente, (a*pixel, b*pixel))
                                        vector_onde_pode_andar.append((a,b))
                                    tes = tes + 1
                                else: 
                                    tes = tes + 1


        elif mapa_com_personagens[x,y].tipo_personagem  == 12 and m == 1 and jogador_da_vez.time == "azul":
            screen.blit(imports.arqueiro_azul_t, (832,180))
            screen.blit(imports.arqueiro_descricao, (832,480))
            vida = font.render(str(mapa_com_personagens[x,y].vida),font,(0,0,0))
            defesa = font.render(str(mapa_com_personagens[x,y].bonus_defesa),font,(0,0,0))
            ataque = font.render(str(math.ceil(mapa_com_personagens[x,y].vida/2)),font,(0,0,0))
            screen.blit(vida, (920,523))
            screen.blit(defesa, (920,558))
            screen.blit(ataque, (920,595))

            if mapa_com_personagens[x,y].ativo_inativo  == 1:
                andar_x = 4
                andar_y = 4
                tes = 0
                vector_casas = [1,1,2,1,1,2,3,2,1,1,2,3,4,3,2,1,1,2,3,4,5,4,3,2,1,1,2,3,4,3,2,1,1,2,3,2,1,1,2,1,1]
                for a in range(x - andar_x, x + andar_x + 1):
                    for b in range(y - andar_y, y + andar_y + 1):
                        if abs(x - a) + abs(y - b) <= andar_x:
                            if(a >= 0 and a <=24 and b >= 0 and b <=24 ): # DENTRO DA MATRIZ
                                if(a != x or b != y) and mapa_com_personagens[a,b].tipo_bloco   <= 7 and mapa_com_personagens[a,b].ativo_inativo     != 1 and mapa_com_personagens[a,b].tipo_personagem    == 0 : # EVITAR PIZAR ONDE N PODE
                                    if (vector_casas[tes] + mapa_com_personagens[a,b].bonus_distancia  > 0): # MOSTRA ONDE DEVE PISAR
                                        #num = font.render(str(vector_casas[tes] + mapa_com_personagens[a,b].bonus_distancia ),font,(0,0,0))
                                        #screen.blit(num,(a*pixel, b*pixel))
                                        screen.blit(imports.cinza_transparente, (a*pixel, b*pixel))
                                        vector_onde_pode_andar.append((a,b))
                                    tes = tes + 1
                                else:
                                    tes = tes + 1

        elif mapa_com_personagens[x,y].tipo_personagem    == 13 and m == 1 and jogador_da_vez.time == "azul":
            screen.blit(imports.mago_azul_t, (832,180))
            screen.blit(imports.mago_descricao, (832,480))
            vida = font.render(str(mapa_com_personagens[x,y].vida),font,(0,0,0))
            defesa = font.render(str(mapa_com_personagens[x,y].bonus_defesa),font,(0,0,0))
            ataque = font.render(str(math.ceil(mapa_com_personagens[x,y].vida/2)),font,(0,0,0))
            screen.blit(vida, (920,523))
            screen.blit(defesa, (920,558))
            screen.blit(ataque, (920,595))

            if mapa_com_personagens[x,y].ativo_inativo     == 1:
                andar_x = 4
                andar_y = 4
                tes = 0
                vector_casas = [1,1,2,1,1,2,3,2,1,1,2,3,4,3,2,1,1,2,3,4,5,4,3,2,1,1,2,3,4,3,2,1,1,2,3,2,1,1,2,1,1]
                for a in range(x - andar_x, x + andar_x + 1):
                    for b in range(y - andar_y, y + andar_y + 1):
                        if abs(x - a) + abs(y - b) <= andar_x:
                            if(a >= 0 and a <=24 and b >= 0 and b <=24 ): # DENTRO DA MATRIZ
                                if(a != x or b != y) and mapa_com_personagens[a,b].tipo_bloco   <= 7 and mapa_com_personagens[a,b].ativo_inativo     != 1 and mapa_com_personagens[a,b].tipo_personagem    == 0 : # EVITAR PIZAR ONDE N PODE
                                    if (vector_casas[tes] + mapa_com_personagens[a,b].bonus_distancia  > 0): # MOSTRA ONDE DEVE PISAR
                                        #num = font.render(str(vector_casas[tes] + mapa_com_personagens[a,b].bonus_distancia ),font,(0,0,0))
                                        #screen.blit(num,(a*pixel, b*pixel))
                                        screen.blit(imports.cinza_transparente, (a*pixel, b*pixel))
                                        vector_onde_pode_andar.append((a,b))
                                    tes = tes + 1
                                else:
                                    #if mapa_com_personagens[a,b].tipo_bloco == 10: # CASA BRANCA
                                    #    area_de_acao.append((a,b))
                                    #    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(a*pixel, b*pixel, pixel, pixel),  2)
                                    tes = tes + 1
                acao_personagem(x,y)

        elif mapa_com_personagens[x,y].tipo_bloco   == 21 and jogador_da_vez.time == "azul":
            screen.blit(imports.butão_cinza, (832*m,180))
            screen.blit(imports.menu_compra, (832*m,300))
            gold = font.render(str(jogador_da_vez.gold)+" ouro",font,(0,0,0))
            screen.blit(gold,(900*m,200))

            verde(mapa_com_personagens[x,y].tipo_bloco)
            mou_x, mou_y = pygame.mouse.get_pos()
            if (mou_x >= 865 and mou_x <= 1070) and (mou_y >=330 and mou_y <=395):
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(865*m, 327, 205, 70),  6)
                if pygame.mouse.get_pressed()[0]:
                    m = 50
                    person = 11
                    return [x,y,0]

            if (mou_x >= 865 and mou_x <= 1070) and (mou_y >=400 and mou_y <=470):
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(865*m, 404, 205, 70),  6)
                if pygame.mouse.get_pressed()[0]:
                    m = 50
                    person = 12
                    return [x,y,0]

            if (mou_x >= 865 and mou_x <= 1070) and (mou_y >=480 and mou_y <=550):
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(865*m, 480, 205, 70),  6)
                if pygame.mouse.get_pressed()[0]:
                    m = 50
                    person = 13
                    return [x,y,0]
            return [x,y,0]

    else:
        screen.blit(imports.passar_turno,(32*26*m,150))
        screen.blit(imports.renderse,(32*26*m,270))

    if m == 50:
        mou_x, mou_y = pygame.mouse.get_pos()
        m = 1

        return [mou_x, mou_y, person]

    return [x,y,0]
local_valido = []


def andar(x1,y1,x2,y2):
    global peca_x
    global peca_y
    global vector_onde_pode_andar
    if ((x2,y2) in vector_onde_pode_andar):
        mapa_com_personagens[math.floor(peca_x/pixel),math.floor(peca_y/pixel)].tipo_personagem    = mapa_com_personagens[x1,y1].tipo_personagem   
        mapa_com_personagens[math.floor(peca_x/pixel),math.floor(peca_y/pixel)].ativo_inativo     = 0
        mapa_com_personagens[math.floor(peca_x/pixel),math.floor(peca_y/pixel)].vida     = mapa_com_personagens[x1,y1].vida    

        mapa_com_personagens[x1,y1].tipo_personagem    = 0
        mapa_com_personagens[x1,y1].ativo_inativo     = -10
        mapa_com_personagens[x1,y1].vida     = -10

        vector_onde_pode_andar = [(-1,-1)]



def verde(p):
    global local_valido
    for i in range(25):
        for j in range(25):
            if(mapa_com_personagens[i,j].tipo_bloco == p):
                if(mapa_com_personagens[i-1,j].tipo_personagem    == 0 and mapa_com_personagens[i-1,j].tipo_bloco   <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((i-1)*pixel, j*pixel, pixel, pixel))
                    local_valido.append(((i-1), j))
                if(mapa_com_personagens[i+1,j].tipo_personagem    == 0 and mapa_com_personagens[i+1,j].tipo_bloco   <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((i+1)*pixel, j*pixel, pixel, pixel))
                    local_valido.append(((i+1), j))
                if(mapa_com_personagens[i,j-1].tipo_personagem    == 0 and mapa_com_personagens[i,j-1].tipo_bloco   <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j-1)*pixel, pixel, pixel))
                    local_valido.append((i, (j-1)))
                if(mapa_com_personagens[i,j+1].tipo_personagem    == 0 and mapa_com_personagens[i,j+1].tipo_bloco   <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j+1)*pixel, pixel, pixel))
                    local_valido.append((i, (j+1)))
'''
            if(mapa_com_personagens[i,j].tipo_personagem > 0):
                if(mapa_com_personagens[i-1,j].tipo_personagem    == 0 and mapa_com_personagens[i-1,j].tipo_bloco   <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((i-1)*pixel, j*pixel, pixel, pixel))
                    local_valido.append(((i-1), j))
                if(mapa_com_personagens[i+1,j].tipo_personagem    == 0 and mapa_com_personagens[i+1,j].tipo_bloco   <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((i+1)*pixel, j*pixel, pixel, pixel))
                    local_valido.append(((i+1), j))
                if(mapa_com_personagens[i,j-1].tipo_personagem    == 0 and mapa_com_personagens[i,j-1].tipo_bloco   <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j-1)*pixel, pixel, pixel))
                    local_valido.append((i, (j-1)))
                if(mapa_com_personagens[i,j+1].tipo_personagem    == 0 and mapa_com_personagens[i,j+1].tipo_bloco   <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j+1)*pixel, pixel, pixel))
                    local_valido.append((i, (j+1)))
'''

def add_personagem(x,y,a,b):
    if a == 1:
        global lista
        if(b == 11): #pix_guerreiro_azul
            mapa_com_personagens[x,y].tipo_personagem   = 11
            mapa_com_personagens[x,y].ativo_inativo     = 1
            mapa_com_personagens[x,y].vida              = 10
            lista = [x,y,0]
        if(b == 12): #pix_arqueiro_azul
            mapa_com_personagens[x,y].tipo_personagem   = 12
            mapa_com_personagens[x,y].ativo_inativo     = 1
            mapa_com_personagens[x,y].vida              = 10
            lista = [x,y,0]
        if(b == 13): #pix_arqueiro_azul
            mapa_com_personagens[x,y].tipo_personagem   = 13
            mapa_com_personagens[x,y].ativo_inativo     = 1
            mapa_com_personagens[x,y].vida              = 10
            #acao_personagem(x,y)
            lista = [x,y,0]

def acao_personagem(i,j):
    #if x1 == x2 and y1 - y2 == 1^2 or x1 - x2 == 1^2 and y1 == y2:
    if(mapa_com_personagens[i-1,j].tipo_bloco == 10):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((i-1)*pixel, j*pixel, pixel, pixel),2)

    if(mapa_com_personagens[i+1,j].tipo_bloco == 10):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((i+1)*pixel, j*pixel, pixel, pixel),2)

    if(mapa_com_personagens[i,j-1].tipo_bloco == 10):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j-1)*pixel, pixel, pixel),2)

    if(mapa_com_personagens[i,j+1].tipo_bloco == 10):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j+1)*pixel, pixel, pixel),2)



lop = 0
def loopi():
    if lop2 == 0:
        if(loop <= 200):
            screen.blit(imports.ouro_insuficiente,(300,loop+400))
        else:
            global lop
            lop = 0
            return
    else:
        if(loop <= 200):
            screen.blit(imports.local_invalido,(300,loop+400))
        else:
            lop = 0
            return

lop2 = 0
loop = 0

menu = 1


creditos = 2
jogador_da_vez = 1

pausa = 0
p = 0

peca_x = -32
peca_y = -32

pixel = 32



lista =[0,0,0]

old_x = 0
old_y = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #pygame.mixer.music.get_busy()

    loop = loop + 3
    if(loop >= 800):
        loop = 0

    screen.blit(imports.mar1, (0,loop))
    screen.blit(imports.mar2, (0,loop - 800))
    screen.blit(imports.logo, (327,80))

    screen.blit(imports.botao_jogar, (428 + creditos,400))
    screen.blit(imports.botao_creditos, (428 + creditos,500))
    screen.blit(imports.botao_sair, (428 + creditos,600))



    add_personagem(12,15,1,12)
    mapa_com_personagens[12,15].ativo_inativo     = 0



    if(menu == 0): # MENU GAME

        if pygame.mouse.get_pressed()[0]:
            mousex, mousey = pygame.mouse.get_pos()
            if(mousex >= 430 and mousex <= 689 and mousey >= 402 and mousey <= 485):
                menu = 1

        if pygame.mouse.get_pressed()[0]:
            mousex, mousey = pygame.mouse.get_pos()
            if(mousex >= 430 and mousex <= 689 and mousey >= 502 and mousey <= 585):
                menu = 2
                creditos = 1

        if pygame.mouse.get_pressed()[0]:
            mousex, mousey = pygame.mouse.get_pos()
            if(mousex >= 430 and mousex <= 689 and mousey >= 602 and mousey <= 685):
                running = False

    if(menu == 2): # CREDITOS
        menu = 2
        creditos = 10000
        screen.blit(imports.creditos_img, (428,400))
        screen.blit(imports.botao_voltar, (428,600))
        if pygame.mouse.get_pressed()[0]:
            mousex, mousey = pygame.mouse.get_pos()
            if(mousex >= 430 and mousex <= 689 and mousey >= 602 and mousey <= 685):
                menu = 0
                creditos = 2



    if(menu == 1): # JOGO

        draw()
        screen.blit(imports.wall, (800,0))
        pixel = 32
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(peca_x, peca_y, pixel, pixel),  2)

        if(lop != 0):
            loopi()



        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x <= 800 and mouse_y <= 800:
                peca_x = math.floor(mouse_x/pixel)*pixel
                peca_y = math.floor(mouse_y/pixel)*pixel
            '''
            elif lista.tipo_bloco   == 0:
                peca_x = math.floor(mouse_x/pixel)*pixel
                peca_y = math.floor(mouse_y/pixel)*pixel
                lista = check(math.floor(peca_x/pixel),math.floor(peca_y/pixel), jogador_da_vez, gold_azul,pygame.event.get())
                print("-------dsdsds---------",peca_x,peca_y)
            '''


        if jogador_da_vez == 1: # AZUL
            screen.blit(imports.vez_do_azul, (pixel*26,pixel*1))
            if(mapa_com_personagens[old_x,old_y].ativo_inativo     == 1):
                andar(old_x,old_y,math.floor(peca_x/pixel),math.floor(peca_y/pixel))



            if lista[2] == 0:
                lista = check(math.floor(peca_x/pixel),math.floor(peca_y/pixel), jogador_azul)




            if lista[2] == 11:
                if jogador_azul.gold  >= 100 and mapa_com_personagens[math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)].tipo_personagem  == 0 and (math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)) in local_valido:
                    add_personagem(math.floor(lista[0]/pixel),math.floor(lista[1]/pixel),1,lista[2])
                    jogador_azul.gold  = jogador_azul.gold  - 100
                    old_x = math.floor(peca_x/pixel)
                    old_y = math.floor(peca_y/pixel)
                    lista = [peca_x,peca_y,0]
                else:
                    if(jogador_azul.gold  < 200):
                        lop = 10
                        loop = 90
                        lista = [1000, 1000, 0]
                        lop2 = 0
                    else:
                        lop = 10
                        loop = 90
                        lista = [1000, 1000, 0]
                        lop2 = 1

            if lista[2] == 12:
                if jogador_azul.gold  >= 150 and mapa_com_personagens[math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)].tipo_personagem == 0 and (math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)) in local_valido:
                    add_personagem(math.floor(lista[0]/pixel),math.floor(lista[1]/pixel),1,lista[2])
                    jogador_azul.gold  = jogador_azul.gold  - 150
                    old_x = math.floor(peca_x/pixel)
                    old_y = math.floor(peca_y/pixel)
                    lista = [peca_x,peca_y,0]
                else:
                    if(jogador_azul.gold  < 200):
                        lop = 10
                        loop = 90
                        lista = [1000, 1000, 0]
                        lop2 = 0
                    else:
                        lop = 10
                        loop = 90
                        lista = [1000, 1000, 0]
                        lop2 = 1

            if lista[2] == 13:
                if jogador_azul.gold >= 200 and mapa_com_personagens[math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)].tipo_personagem == 0 and (math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)) in local_valido: 
                    add_personagem(math.floor(lista[0]/pixel),math.floor(lista[1]/pixel),1,lista[2])
                    jogador_azul.gold  = jogador_azul.gold  - 200
                    old_x = math.floor(peca_x/pixel)
                    old_y = math.floor(peca_y/pixel)
                    lista = [peca_x,peca_y,0]
                else:
                    if(jogador_azul.gold  < 200):
                        lop = 10
                        loop = 90
                        lista = [1000, 1000, 0]
                        lop2 = 0
                    else:
                        lop = 10
                        loop = 90
                        lista = [1000, 1000, 0]
                        lop2 = 1




            '''
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_ESCAPE]) != True and p == 0:
                pausa = 0


            if pausa:
                screen.blit(butão_cinza, (832,180))
                passar = font.render("Passar a vez",font,(0,0,0))
                screen.blit(passar,(900,200))

                screen.blit(butão_cinza, (832,300))
                rendicao = font.render("Render-se",font,(0,0,0))
                screen.blit(rendicao,(900,300))
                #print((keys[pygame.K_ESCAPE]) and pausa == 1)
                if (keys[pygame.K_ESCAPE]) and pausa == 1:
                    p = 1
            '''
        

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()