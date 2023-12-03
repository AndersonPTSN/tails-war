import pygame
from PIL import Image
pygame.mixer.init()
#--------------------------------------------------------------- BLOCOS

mar_fundo = pygame.image.load("imagens/tiles/tile_agua_f.png")
mar_fundo_big = pygame.image.load("imagens/tiles/imagem/tile_agua_f_big.png")
mar_fundo_descricao = pygame.image.load("imagens/tiles/descrição/mar_fundo_descricao.png")

mar_raso = pygame.image.load("imagens/tiles/tile_agua.png")
mar_raso_big = pygame.image.load("imagens/tiles/imagem/tile_agua_big.png")
mar_raso_descricao = pygame.image.load("imagens/tiles/descrição/mar_raso_descricao.png")

areia = pygame.image.load("imagens/tiles/areia.png")
areia_big = pygame.image.load("imagens/tiles/imagem/areia_big.png")
areia_descricao = pygame.image.load("imagens/tiles/descrição/praia_descricao.png")

planice = pygame.image.load("imagens/tiles/grama_baixa.png")
planice_big = pygame.image.load("imagens/tiles/imagem/grama_baixa_big.png")
planice_descricao = pygame.image.load("imagens/tiles/descrição/planicie_descricao.png")

floresta = pygame.image.load("imagens/tiles/grama_alta.png")
floresta_big = pygame.image.load("imagens/tiles/imagem/grama_alta_big.png")
floresta_descricao = pygame.image.load("imagens/tiles/descrição/floresta_descricao.png")

montanha = pygame.image.load("imagens/tiles/montanha.png")
montanha_128 = pygame.image.load("imagens/tiles/imagem/montanha_128.png")
montanha_descricao = pygame.image.load("imagens/tiles/descrição/montanha_descricao.png")

tijolo = pygame.image.load("imagens/tiles/tijolo.png")
tijolo_big = pygame.image.load("imagens/tiles/imagem/tijolo_big.png")
tijolo_descricao = pygame.image.load("imagens/tiles/descrição/tijolo_descricao.png")

#--------------------------------------------------------------- NOISE
im = Image.open("imagens/mapa20.png", 'r')
#--------------------------------------------------------------- ESTRUTURAS
forte = pygame.image.load("imagens/tiles/forte.png")
forte_big = pygame.image.load("imagens/tiles/imagem/forte_big.png")
casa_branca = pygame.image.load("imagens/tiles/casa.png")
casa_big = pygame.image.load("imagens/tiles/imagem/casa_big.png")
#--------------------------------------------------------------- DESCRIÇÃO 
guerreiro_descricao = pygame.image.load("imagens/tiles/descrição/guerreiro_descricao.png")
arqueiro_descricao = pygame.image.load("imagens/tiles/descrição/arqueiro_descricao.png")
mago_descricao = pygame.image.load("imagens/tiles/descrição/mago_descricao.png")
forte_descricao = pygame.image.load("imagens/tiles/descrição/forte_descricao.png")
casa_descricao = pygame.image.load("imagens/tiles/descrição/casa_descricao.png")
#--------------------------------------------------------------- AZUL
vez_do_azul = pygame.image.load("imagens/botões/vez_do_azul.png")

forte_azul = pygame.image.load("imagens/tiles/forte_azul.png")
forte_azul_big = pygame.image.load("imagens/tiles/imagem/forte_azul_big.png")
casa_azul = pygame.image.load("imagens/tiles/casa_azul.png")
casa_azul_big = pygame.image.load("imagens/tiles/imagem/casa_azul_big.png")

arqueiro_azul = pygame.image.load("imagens/tiles/arqueiro_azul.png")
arqueiro_azul_t = pygame.image.load("imagens/tiles/imagem/arqueiro_azul_t.png")
mago_azul = pygame.image.load("imagens/tiles/mago_azul.png")
mago_azul_t = pygame.image.load("imagens/tiles/imagem/mago_azul_t.png")
guerreiro_azul = pygame.image.load("imagens/tiles/guerreiro_azul.png")
#--------------------------------------------------------------- VERMELHO
vez_do_vermelho = pygame.image.load("imagens/botões/vez_do_vermelho.png")

forte_vermelho = pygame.image.load("imagens/tiles/forte_vermelho.png")
forte_vermelho_big = pygame.image.load("imagens/tiles/imagem/forte_vermelho_big.png")
casa_vermelha = pygame.image.load("imagens/tiles/casa_vermelha.png")
casa_vermelha_big = pygame.image.load("imagens/tiles/imagem/casa_vermelha_big.png")

arqueiro_vermelho = pygame.image.load("imagens/tiles/arqueiro_vermelho.png")
arqueiro_vermelho_t = pygame.image.load("imagens/tiles/imagem/arqueiro_vermelho_t.png")
mago_vermelho = pygame.image.load("imagens/tiles/mago_vermelho.png")
mago_vermelho_t = pygame.image.load("imagens/tiles/imagem/mago_vermelho_t.png")
guerreiro_vermelho = pygame.image.load("imagens/tiles/guerreiro_vermelho.png")
#--------------------------------------------------------------- MENU COMPRA
butão_cinza = pygame.image.load("imagens/botões/butão_cinza.png")
menu_compra = pygame.image.load("imagens/botões/menu_compra.png")
#--------------------------------------------------------------- MENU PAUSA
passar_turno = pygame.image.load("imagens/botões/passar_turno.png")
renderse = pygame.image.load("imagens/botões/renderse.png")
#--------------------------------------------------------------- AVISOS
ouro_insuficiente = pygame.image.load("imagens/botões/ouro_insuficiente.png")
local_invalido = pygame.image.load("imagens/botões/local_invalido.png")
#--------------------------------------------------------------- BACKGROUND MAR - FUNDO MENU PRINCIPAL
mar1 = pygame.image.load("imagens/a1.png")
mar2 = pygame.image.load("imagens/a1.png")

#--------------------------------------------------------------- MENU PRINCIPAL
logo = pygame.image.load("imagens/logo.png")

botao_jogar = pygame.image.load("imagens/botões/butão_jogar.png")
botao_creditos = pygame.image.load("imagens/botões/butão_creditos.png")
creditos_img = pygame.image.load("imagens/creditos_img.png")
botao_sair = pygame.image.load("imagens/botões/butão_sair.png")
botao_voltar = pygame.image.load("imagens/botões/butão_voltar.png")

#--------------------------------------------------------------- OUTROS
cinza_transparente = pygame.image.load("imagens/tiles/cinza_transparente.png")
wall = pygame.image.load("imagens/wall.png")



#=============================================================== MUSICAS
pygame.mixer.music.load("musicas/Musica_2.wav")