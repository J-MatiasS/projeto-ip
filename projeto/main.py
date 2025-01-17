import pygame
from colorama import init, Fore #biblioteca de cores

#initialising pygame
pygame.init()

#defining size of game window
tela = pygame.display.set_mode((800,600))

#inicia o colorama
init(autoreset=True)

#cores
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Titulo e icon
pygame.display.set_caption("Jogo maneirasso")

def escrever(texto, cor, x, y, tamanho=40):
    fonte = pygame.font.Font(None, tamanho)  # Cria uma fonte com um tamanho específico (padrão: 30)
    texto_renderizado = fonte.render(texto, True, cor)  # Renderiza o texto com a fonte e a cor especificadas
    tela.blit(texto_renderizado, (x, y))  # Desenha o texto renderizado na tela nas coordenadas (x, y)

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    #printa os nomes na tela através da função
    escrever('Júlio', VERMELHO, 50, 50)
    escrever('Casé', VERDE, 50, 100)
    escrever('Vini', AZUL, 50, 150)
    escrever('Marcos', VERMELHO, 50, 200)
    escrever('Pimentel', VERDE, 50, 250)

    pygame.display.update()

pygame.quit()