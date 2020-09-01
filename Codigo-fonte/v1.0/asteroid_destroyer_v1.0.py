"""
Asteroid destroyer para Micro:bit - Destrua todos os asteroides o mais rápido possível.
Inicialmente será exibido um rosto feliz, para iniciar precione ou o botão A ou B.
    Botão A - para iniciar no modo fácil (toda tela será usada para mostrar os próximos asteroides)
    Botão B - para iniciar no modo Difícil (apenas o próximo asteroide é mostrado)
Sempre destrua o asteroide que estiver na primeira linha. Para destruir os asteroides basta precionar:
    Botão A - Para destruir os asteroides na coluna esquerda
    Botão B - Para destruir os asteroides na coluna direita
    Botão A+B - Para destruir os asteroides no coluna central
No final será mostrado o tempo (em segundos) que o jogodor levou para destruir todos os asteroides.
Este tempo serve como pontuação/score a fim de disputar com outros jogadores.

Autor: Pedro Henrique Robadel (ph.robadel@gmail.com)
Versão: 1.0 @ 2020/08/31
Licença: MIT License (https://opensource.org/licenses/MIT)
Mais informações: https://github.com/ph-robadel/MicroBit-Game-AsteroidDestroyer.git
"""

from microbit import display, Image, button_a, button_b
from time import ticks_ms, sleep_ms
from random import randint

QTD_MAXIMA_ASTEROIDES = 100
qtd_asteroides_gerados = 0

def iniciar_lista(tamanho_lista:int) -> list:
    global qtd_asteroides_gerados
    qtd_asteroides_gerados = tamanho_lista
    lista = []
    for iteracao in range(tamanho_lista):
        lista.append(randint(0, 2)*2)

    return lista

def atualizar_lista(lista:list) -> None:
    global qtd_asteroides_gerados
    del(lista[0])
    if qtd_asteroides_gerados < QTD_MAXIMA_ASTEROIDES:
        lista.append(randint(0, 2)*2)
        qtd_asteroides_gerados += 1
    else:
        lista.append(-1)

def imp_lista(lista:list, isDificil:bool) -> None:
    display.clear()

    if isDificil:
        fator = 6
    else:
        fator = 1.5

    for y, x in enumerate(lista):
        if(0<=x<5 and 0<=y<5):
            display.set_pixel(x, y, 9-int(y*fator))

def jogar(qtd_asteroides_tela:int) -> None:
    lista_jogo = iniciar_lista(qtd_asteroides_tela)
    isDificil = qtd_asteroides_tela < 3
    imp_lista(lista_jogo, isDificil)
    t_ini = ticks_ms()
    while lista_jogo[0] != -1:
        if(button_a.is_pressed() and not button_b.is_pressed() and lista_jogo[0] == 0) or\
          (button_a.is_pressed() and button_b.is_pressed() and lista_jogo[0] == 2) or\
          (not button_a.is_pressed() and button_b.is_pressed() and lista_jogo[0] == 4):
            atualizar_lista(lista_jogo)
            imp_lista(lista_jogo, isDificil)
            sleep_ms(170)

    display.scroll("{:.2f}".format((ticks_ms() - t_ini)/1000))
    display.show(Image.HAPPY)


display.show(Image.HAPPY)
while True:
    # Botão A - Inicia jogo no modo fácil
    # Botão B - Inicia jogo no modo difícil
    if button_a.is_pressed():
        jogar(qtd_asteroides_tela=5)
    elif button_b.is_pressed():
        jogar(qtd_asteroides_tela=2)