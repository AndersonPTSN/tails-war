
import pygame
from PIL import Image
import math
import numpy as np

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((35*32,25*32), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
dt = 0
pygame.font.init() 
font = pygame.font.SysFont('Comic Sans MS', 30)




mar_fundo = pygame.image.load("tile_agua_f.png")
mar_fundo_big = pygame.image.load("tile_agua_f_big.png")
mar_fundo_descricao = pygame.image.load("mar_fundo_descricao.png")

mar_raso = pygame.image.load("tile_agua.png")
mar_raso_big = pygame.image.load("tile_agua_big.png")
mar_raso_descricao = pygame.image.load("mar_raso_descricao.png")

areia = pygame.image.load("areia.png")
areia_big = pygame.image.load("areia_big.png")
areia_descricao = pygame.image.load("praia_descricao.png")

planice = pygame.image.load("grama_baixa.png")
planice_big = pygame.image.load("grama_baixa_big.png")
planice_descricao = pygame.image.load("planicie_descricao.png")

floresta = pygame.image.load("grama_alta.png")
floresta_big = pygame.image.load("grama_alta_big.png")
floresta_descricao = pygame.image.load("floresta_descricao.png")

montanha = pygame.image.load("montanha.png")
montanha_descricao = pygame.image.load("montanha_descricao.png")
montanha_128 = pygame.image.load("montanha_128.png")

tijolo = pygame.image.load("tijolo.png")
tijolo_big = pygame.image.load("tijolo_big.png")
tijolo_descricao = pygame.image.load("tijolo_descricao.png")

im = Image.open("mapa20.png", 'r')


#casa = pygame.image.load("casa.png")
forte = pygame.image.load("forte.png")
casa_branca = pygame.image.load("casa.png")

guerreiro_descricao = pygame.image.load("guerreiro_descricao.png")
arqueiro_descricao = pygame.image.load("arqueiro_descricao.png")
mago_descricao = pygame.image.load("mago_descricao.png")
#--------------------------------------------------------------- AZUL
vez_do_azul = pygame.image.load("vez_do_azul.png")

forte_azul = pygame.image.load("forte_azul.png")
casa_azul = pygame.image.load("casa_azul.png")

arqueiro_azul = pygame.image.load("arqueiro_azul.png")
arqueiro_azul_t = pygame.image.load("arqueiro_azul_t.png")
mago_azul = pygame.image.load("mago_azul.png")
mago_azul_t = pygame.image.load("mago_azul_t.png")
guerreiro_azul = pygame.image.load("guerreiro_azul.png")
#--------------------------------------------------------------- VERMELHO
vez_do_vermelho = pygame.image.load("vez_do_vermelho.png")

forte_vermelho = pygame.image.load("forte_vermelho.png")
casa_vermelha = pygame.image.load("casa_vermelha.png")

arqueiro_vermelho = pygame.image.load("arqueiro_vermelho.png")
arqueiro_vermelho_t = pygame.image.load("arqueiro_vermelho_t.png")
mago_vermelho = pygame.image.load("mago_vermelho.png")
mago_vermelho_t = pygame.image.load("mago_vermelho_t.png")
guerreiro_vermelho = pygame.image.load("guerreiro_vermelho.png")
#--------------------------------------------------------------- 

butão_cinza = pygame.image.load("butão_cinza.png")
menu_compra = pygame.image.load("menu_compra.png")

passar_turno = pygame.image.load("passar_turno.png")
renderse = pygame.image.load("renderse.png")

ouro_insuficiente = pygame.image.load("ouro_insuficiente.png")
local_invalido = pygame.image.load("local_invalido.png")

mar1 = pygame.image.load("a1.png")
mar2 = pygame.image.load("a1.png")

logo = pygame.image.load("logo.png")

botao_jogar = pygame.image.load("butão_jogar.png")
botao_creditos = pygame.image.load("butão_creditos.png")
botao_sair = pygame.image.load("butão_sair.png")
botao_voltar = pygame.image.load("butão_voltar.png")

creditos_img = pygame.image.load("creditos_img.png")

cinza_transparente = pygame.image.load("cinza_transparente.png")

wall = pygame.image.load("wall.png")


pygame.mixer.music.load("Musica_2.wav")
#pygame.mixer.music.play(-1)

shap = 25
shape = ([shap,shap])
position = 0

shape[0] = shap
shape[1] = shap
tela = Image.new ("RGBA", shape, (0, 0, 0))
pix_val = list(im.getdata())


pix = im.load() 
mapa_com_personagens = np.empty((shap, shap), dtype=object)

#(BONUS DE DISTANCIA, BONUS DE DEFESA, TIPO DE BLOCO, TIPO DE PERSONAGEM, ATIVO/INATIVO, VIDA)

pix_mar_fundo          = [-2,-2,  7, 0, -10, -10]
pix_mar_raso           = [-1,-1,  1, 0, -10, -10]
pix_areia              = [ 0, 0,  2, 0, -10, -10]
pix_planice            = [ 0, 0,  3, 0, -10, -10]
pix_floresta           = [-1,+1,  4, 0, -10, -10]
pix_montanha           = [-2,+2,  5, 0, -10, -10]
pix_tijolo             = [ 0,+3,  6, 0, -10, -10]

pix_casa               = [-10,-10, 10, 0, -10, 0]
pix_casa_azul          = [-10,-10, 11, 0, -10, 5]
pix_casa_vermelha      = [-10,-10, 12, 0, -10, 5]

pix_forte              = [-10,-10, 20, 0, -10, 0]
pix_forte_azul         = [-10,-10, 21, 0,  1, 10]
pix_forte_vermelho     = [-10,-10, 22, 0,  1, 10]


pix_guerreiro_azul     = [-10,-10,-10, 11,  1,  10]
pix_guerreiro_vermelho = [-10,-10,-10, 12,  1,  10]

pix_arqueiro_azul      = [-10,-10,-10, 21,  1,  10]
pix_arqueiro_vermelho  = [-10,-10,-10, 22,  1,  10]

pix_mago_azul          = [-10,-10,-10, 31,  1,  10]
pix_mago_vermelho      = [-10,-10,-10, 32,  1,  10]


def draw1():
    pixel = 32
    for i in range(25):
        for j in range(25):
            if(pix[i,j] == (65, 105, 225, 255)):
                mapa_com_personagens[i,j] = pix_mar_fundo.copy()
            if(pix[i,j] == (85, 125, 245, 255)):
                mapa_com_personagens[i,j] = pix_mar_raso.copy()
            if(pix[i,j] == (238, 214, 175, 255)):
                mapa_com_personagens[i,j] = pix_areia.copy()
            if(pix[i,j] == (34, 139, 34, 255)):
                mapa_com_personagens[i,j] = pix_planice.copy()
            if(pix[i,j] == (0, 100, 0, 255)):
                mapa_com_personagens[i,j] = pix_floresta.copy()
            if(pix[i,j] == (139, 137, 137, 255)):
                mapa_com_personagens[i,j] = pix_montanha.copy()

            if(pix[i,j] == (255,0,0, 255)):
                mapa_com_personagens[i,j] = pix_casa.copy()
            if(pix[i,j] == (255,255,0,255)):
                mapa_com_personagens[i,j] = pix_forte.copy()
            if(pix[i,j] == (255,0,255,255)):
                mapa_com_personagens[i,j] = pix_tijolo.copy()

    mapa_com_personagens[1,19] = pix_casa_azul.copy()
    mapa_com_personagens[5,23] = pix_casa_azul.copy()
    mapa_com_personagens[1,23] = pix_forte_azul.copy()

    mapa_com_personagens[13,13] = pix_forte_azul.copy()

    mapa_com_personagens[19,1] = pix_casa_vermelha.copy()
    mapa_com_personagens[23,5] = pix_casa_vermelha.copy()
    mapa_com_personagens[23,1] = pix_forte_vermelho.copy()

draw1()

def draw():

    for i in range(25):
        for j in range(25):
            if(mapa_com_personagens[i,j][2] == 7): #pix_mar_fundo
                screen.blit(mar_fundo, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 1): #pix_mar_raso
                screen.blit(mar_raso, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 2): #pix_areia
                screen.blit(areia, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 3): #pix_planice
                screen.blit(planice, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 4): #pix_floresta
                screen.blit(floresta, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 5): #pix_montanha
                screen.blit(montanha, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 6): #pix_tijolo
                screen.blit(tijolo, (pixel*i,pixel*j))


            if(mapa_com_personagens[i,j][2] == 10): #pix_casa
                screen.blit(casa_branca, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 11): #pix_casa_azul
                screen.blit(casa_azul, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 12): #pix_casa_vermelha
                screen.blit(casa_vermelha, (pixel*i,pixel*j))

            if(mapa_com_personagens[i,j][2] == 20): #pix_forte
                screen.blit(forte, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 21): #pix_forte_azul
                screen.blit(forte_azul, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][2] == 22): #pix_forte_vermelho
                screen.blit(forte_vermelho, (pixel*i,pixel*j))

            if(mapa_com_personagens[i,j][3] == 11): #pix_guerreiro_azul
                screen.blit(guerreiro_azul, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][3] == 12): #pix_arqueiro_azul
                screen.blit(arqueiro_azul, (pixel*i,pixel*j))
            if(mapa_com_personagens[i,j][3] == 13): #pix_mago_azul
                screen.blit(mago_azul, (pixel*i,pixel*j))

            if(mapa_com_personagens[i,j][4] == 0): #pix_mago_azul
                screen.blit(cinza_transparente, (pixel*i,pixel*j))

m = 1
person = 0
vector_onde_pode_andar = [(-1,-1)]
def check(x,y,jogador_da_vez,gold_azul, event_list):
    global m 
    global person
    global vector_onde_pode_andar
    if (x >= 0 and x <= 24) and (y >=0 and y <=24):
        if mapa_com_personagens[x,y][2] == 6 and mapa_com_personagens[x,y][3] == 0 and m == 1: # == pix_tijolo:
            screen.blit(tijolo_big, (832,180))
            screen.blit(tijolo_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y][2] == 5 and mapa_com_personagens[x,y][3] == 0 and m == 1: # == pix_montanha:
            screen.blit(montanha_128, (832,180))
            screen.blit(montanha_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y][2] == 4 and mapa_com_personagens[x,y][3] == 0 and m == 1:# == pix_floresta:
            screen.blit(floresta_big, (832,180))
            screen.blit(floresta_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y][2] == 3 and mapa_com_personagens[x,y][3] == 0 and m == 1: # == pix_planice:
            screen.blit(planice_big, (832,180))
            screen.blit(planice_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y][2] == 2 and mapa_com_personagens[x,y][3] == 0 and m == 1: # == pix_areia:
            screen.blit(areia_big, (832,180))
            screen.blit(areia_descricao, (832,480))
            return [0,0,0]
        elif mapa_com_personagens[x,y][2] == 1 and mapa_com_personagens[x,y][3] == 0 and m == 1: # == pix_mar_raso:
            screen.blit(mar_raso_big, (832,180))
            screen.blit(mar_raso_descricao, (832,480))
            return [x,y,0]
        elif mapa_com_personagens[x,y][2] == 7 and mapa_com_personagens[x,y][3] == 0 and m == 1: # == pix_mar_fundo:
            screen.blit(mar_fundo_big, (832,180))
            screen.blit(mar_fundo_descricao, (832,480))
            return [x,y,0]

        elif mapa_com_personagens[x,y][3] == 12 and m == 1 and jogador_da_vez == 1:
            screen.blit(arqueiro_azul_t, (832,180))
            screen.blit(arqueiro_descricao, (832,480))

            if mapa_com_personagens[x,y][4] == 1:
                andar_x = 4
                andar_y = 4
                tes = 0
                vector_casas = [1,1,2,1,1,2,3,2,1,1,2,3,4,3,2,1,1,2,3,4,5,4,3,2,1,1,2,3,4,3,2,1,1,2,3,2,1,1,2,1,1]
                for a in range(x - andar_x, x + andar_x + 1):
                    for b in range(y - andar_y, y + andar_y + 1):
                        if abs(x - a) + abs(y - b) <= andar_x:
                            if(a >= 0 and a <=24 and b >= 0 and b <=24 ): # DENTRO DA MATRIZ
                                if(a != x or b != y) and mapa_com_personagens[a,b][2] <= 7 and mapa_com_personagens[a,b][4] != 1 and mapa_com_personagens[a,b][3] == 0 : # EVITAR PIZAR ONDE N PODE
                                    if (vector_casas[tes] + mapa_com_personagens[a,b][0] > 0): # MOSTRA ONDE DEVE PISAR
                                        num = font.render(str(vector_casas[tes] + mapa_com_personagens[a,b][0]),font,(0,0,0))
                                        #screen.blit(num,(a*pixel, b*pixel))
                                        screen.blit(cinza_transparente, (a*pixel, b*pixel))
                                        vector_onde_pode_andar.append((a,b))
                                    tes = tes + 1
                                else:
                                    tes = tes + 1

                '''
                if mapa_com_personagens[x,y][4] == 1:
                    if pygame.mouse.get_pressed()[0]:
                        mou_x, mou_y = pygame.mouse.get_pos()
                        if ((mou_x,mou_y) in vector_onde_pode_andar):
                            print("pode")
                        else:
                            lop = 10
                            loop = 90
                            lista = [1000, 1000, 0]
                            lop2 = 1
                '''
        elif mapa_com_personagens[x,y][3] == 13 and m == 1 and jogador_da_vez == 1:
            screen.blit(mago_azul_t, (832,180))
            screen.blit(mago_descricao, (832,480))

            if mapa_com_personagens[x,y][4] == 1:
                andar_x = 4
                andar_y = 4
                tes = 0
                vector_casas = [1,1,2,1,1,2,3,2,1,1,2,3,4,3,2,1,1,2,3,4,5,4,3,2,1,1,2,3,4,3,2,1,1,2,3,2,1,1,2,1,1]
                for a in range(x - andar_x, x + andar_x + 1):
                    for b in range(y - andar_y, y + andar_y + 1):
                        if abs(x - a) + abs(y - b) <= andar_x:
                            if(a >= 0 and a <=24 and b >= 0 and b <=24 ): # DENTRO DA MATRIZ
                                if(a != x or b != y) and mapa_com_personagens[a,b][2] <= 7 and mapa_com_personagens[a,b][4] != 1 and mapa_com_personagens[a,b][3] == 0 : # EVITAR PIZAR ONDE N PODE
                                    if (vector_casas[tes] + mapa_com_personagens[a,b][0] > 0): # MOSTRA ONDE DEVE PISAR
                                        num = font.render(str(vector_casas[tes] + mapa_com_personagens[a,b][0]),font,(0,0,0))
                                        #screen.blit(num,(a*pixel, b*pixel))
                                        screen.blit(cinza_transparente, (a*pixel, b*pixel))
                                        vector_onde_pode_andar.append((a,b))
                                    tes = tes + 1
                                else:
                                    tes = tes + 1

        elif mapa_com_personagens[x,y][2] == 21 and jogador_da_vez == 1:
            screen.blit(butão_cinza, (832*m,180))
            screen.blit(menu_compra, (832*m,300))
            gold = font.render(str(gold_azul)+" ouro",font,(0,0,0))
            screen.blit(gold,(900*m,200))

            verde(pix_forte_azul)
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
        screen.blit(passar_turno,(32*26*m,150))
        screen.blit(renderse,(32*26*m,270))

    if m == 50:
        mou_x, mou_y = pygame.mouse.get_pos()
        m = 1

        return [mou_x, mou_y, person]

    return [x,y,0]
local_valido = []


def andar(x1,y1,x2,y2):
    global peca_x
    global old_x
    global peca_y
    global old_y
    global walk_x
    global walk_y
    global vector_onde_pode_andar
    if ((x2,y2) in vector_onde_pode_andar):

        mapa_com_personagens[math.floor(peca_x/pixel),math.floor(peca_y/pixel)][3] = mapa_com_personagens[old_x,old_y][3]
        mapa_com_personagens[math.floor(peca_x/pixel),math.floor(peca_y/pixel)][4] = 0
        mapa_com_personagens[math.floor(peca_x/pixel),math.floor(peca_y/pixel)][5] = mapa_com_personagens[old_x,old_y][5]

        mapa_com_personagens[old_x,old_y][3] = 0
        mapa_com_personagens[old_x,old_y][4] = -10
        mapa_com_personagens[old_x,old_y][5] = -10

        vector_onde_pode_andar = [(-1,-1)]

    else:
        lop = 10
        loop = 90
        lista = [1000, 1000, 0]
        lop2 = 1



def verde(p):
    global local_valido
    for i in range(25):
        for j in range(25):
            if(mapa_com_personagens[i,j] == p):
                if(mapa_com_personagens[i-1,j][3] == 0 and mapa_com_personagens[i-1,j][2] <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((i-1)*pixel, j*pixel, pixel, pixel))
                    local_valido.append(((i-1), j))
                if(mapa_com_personagens[i+1,j][3] == 0 and mapa_com_personagens[i+1,j][2] <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((i+1)*pixel, j*pixel, pixel, pixel))
                    local_valido.append(((i+1), j))
                if(mapa_com_personagens[i,j-1][3] == 0 and mapa_com_personagens[i,j-1][2] <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j-1)*pixel, pixel, pixel))
                    local_valido.append((i, (j-1)))
                if(mapa_com_personagens[i,j+1][3] == 0 and mapa_com_personagens[i,j+1][2] <= 7 ):
                    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j+1)*pixel, pixel, pixel))
                    local_valido.append((i, (j+1)))


def cinza(i,j):
    #global local_valido
    if(mapa_com_personagens[i-1,j][3] == 0 and mapa_com_personagens[i-1,j][2] <= 7):
        pygame.draw.rect(screen, (150, 150, 150, 150), pygame.Rect((i-1)*pixel, j*pixel, pixel, pixel))
        screen.blit(cinza_transparente, ((i-1)*pixel, j*pixel)) 
        local_valido.append(((i-1), j))
    if(mapa_com_personagens[i+1,j][3] == 0 and mapa_com_personagens[i+1,j][2] <= 7 ):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((i+1)*pixel, j*pixel, pixel, pixel))
        local_valido.append(((i+1), j))
    if(mapa_com_personagens[i,j-1][3] == 0 and mapa_com_personagens[i,j-1][2] <= 7 ):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j-1)*pixel, pixel, pixel))
        local_valido.append((i, (j-1)))
    if(mapa_com_personagens[i,j+1][3] == 0 and mapa_com_personagens[i,j+1][2] <= 7 ):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i*pixel, (j+1)*pixel, pixel, pixel))
        local_valido.append((i, (j+1)))

def add_and_remove_person(x,y,a,b):
    if a == 1:
        global lista
        if(b == 11): #pix_guerreiro_azul
            mapa_com_personagens[x,y][3] = 11
            mapa_com_personagens[x,y][4] = 1
            mapa_com_personagens[x,y][5] = 10
            lista = [x,y,0]
        if(b == 12): #pix_arqueiro_azul
            mapa_com_personagens[x,y][3] = 12
            mapa_com_personagens[x,y][4] = 1
            mapa_com_personagens[x,y][5] = 10
            lista = [x,y,0]
        if(b == 13): #pix_arqueiro_azul
            mapa_com_personagens[x,y][3] = 13
            mapa_com_personagens[x,y][4] = 1
            mapa_com_personagens[x,y][5] = 10
            lista = [x,y,0]

lop = 0
def loopi():
    if lop2 == 0:
        if(loop <= 200):
            screen.blit(ouro_insuficiente,(300,loop+400))
        else:
            global lop
            lop = 0
            return
    else:
        if(loop <= 200):
            screen.blit(local_invalido,(300,loop+400))
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

gold_azul = 900
gold_vermelho = 100

pixel = 32


soldado = 0

lista =[0,0,0]

old_x = 0
old_y = 0

walk_x = 0
walk_y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #pygame.mixer.music.get_busy()

    loop = loop + 3
    if(loop >= 800):
        loop = 0

    screen.blit(mar1, (0,loop))
    screen.blit(mar2, (0,loop - 800))
    screen.blit(logo, (327,80))

    screen.blit(botao_jogar, (428 + creditos,400))
    screen.blit(botao_creditos, (428 + creditos,500))
    screen.blit(botao_sair, (428 + creditos,600))



    add_and_remove_person(12,15,1,12)
    mapa_com_personagens[12,15][4] = 0



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
        creditos = 1000
        screen.blit(creditos_img, (428,400))
        screen.blit(botao_voltar, (428,600))
        if pygame.mouse.get_pressed()[0]:
            mousex, mousey = pygame.mouse.get_pos()
            if(mousex >= 430 and mousex <= 689 and mousey >= 602 and mousey <= 685):
                menu = 0
                creditos = 2



    if(menu == 1): # JOGO

        draw()
        screen.blit(wall, (800,0))
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
            elif lista[2] == 0:
                peca_x = math.floor(mouse_x/pixel)*pixel
                peca_y = math.floor(mouse_y/pixel)*pixel
                lista = check(math.floor(peca_x/pixel),math.floor(peca_y/pixel), jogador_da_vez, gold_azul,pygame.event.get())
                print("-------dsdsds---------",peca_x,peca_y)
            '''


        if jogador_da_vez == 1: # AZUL
            screen.blit(vez_do_azul, (pixel*26,pixel*1))

            if(mapa_com_personagens[old_x,old_y][3] > 0 and mapa_com_personagens[old_x,old_y][4] == 1):
                andar(old_x,old_y,math.floor(peca_x/pixel),math.floor(peca_y/pixel))



            if lista[2] == 0:
                lista = check(math.floor(peca_x/pixel),math.floor(peca_y/pixel), jogador_da_vez, gold_azul,pygame.event.get())


            if lista[2] == 11:
                if gold_azul >= 100 and mapa_com_personagens[math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)][3] == 0 and (math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)) in local_valido:
                    add_and_remove_person(math.floor(lista[0]/pixel),math.floor(lista[1]/pixel),1,lista[2])
                    gold_azul = gold_azul - 100
                    lista = [peca_x,peca_y,0]
                else:
                    if(gold_azul < 200):
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
                if gold_azul >= 150 and mapa_com_personagens[math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)][3] == 0 and (math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)) in local_valido:
                    add_and_remove_person(math.floor(lista[0]/pixel),math.floor(lista[1]/pixel),1,lista[2])
                    gold_azul = gold_azul - 150
                    old_x = math.floor(peca_x/pixel)
                    old_y = math.floor(peca_y/pixel)
                    walk_x = old_x
                    walk_y = old_y
                    lista = [peca_x,peca_y,0]
                else:
                    if(gold_azul < 200):
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
                if gold_azul >= 200 and mapa_com_personagens[math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)][3] == 0 and (math.floor(lista[0]/pixel),math.floor(lista[1]/pixel)) in local_valido: 
                    add_and_remove_person(math.floor(lista[0]/pixel),math.floor(lista[1]/pixel),1,lista[2])
                    gold_azul = gold_azul - 200
                    old_x = math.floor(peca_x/pixel)
                    old_y = math.floor(peca_y/pixel)
                    walk_x = old_x
                    walk_y = old_y
                    lista = [peca_x,peca_y,0]
                else:
                    if(gold_azul < 200):
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