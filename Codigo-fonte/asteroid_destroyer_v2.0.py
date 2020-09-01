"""
Asteroid destroyer para Micro:bit - Destrua todos os asteroides o mais rápido possível.
Inicialmente será exibido um rosto feliz, para iniciar precione ou o botão A ou B.
    Botão A - para iniciar o jogo com o asteroide piscando
    Botão B - para iniciar o jogo sem ter o asteroide piscando
Sempre destrua o asteroide que estiver na primeira linha. Para destruir os asteroides basta precionar:
    Botão A - Para destruir os asteroides na coluna esquerda
    Botão B - Para destruir os asteroides na coluna direita
    Botão A+B - Para destruir os asteroides no coluna central
No final será mostrado o tempo (em segundos) que o jogodor levou para destruir todos os asteroides.
Este tempo serve como pontuação/score a fim de disputar com outros jogadores.

Autor: Pedro Henrique Robadel (ph.robadel@gmail.com)
Versão: 2.0 @ 2020/09/1
Licença: MIT License (https://opensource.org/licenses/MIT)
Mais informações: https://github.com/ph-robadel/MicroBit-Game-AsteroidDestroyer.git
"""

from microbit import display, Image, button_a, button_b
from time import ticks_ms, sleep_ms
from random import randint

QTD_MAXIMA_ASTEROIDES = 100
qtd_asteroides_gerados = 0

def iniciar_asteroides_jogo() -> list:
    global qtd_asteroides_gerados
    qtd_asteroides_gerados = 5
    lista_asteroides = []
    for iteracao in range(5):
        lista_asteroides.append(randint(0, 2)*2)

    return lista_asteroides


def atualizar_lista_asteroides(lista_asteroides:list) -> None:
    global qtd_asteroides_gerados
    del(lista_asteroides[0])
    if qtd_asteroides_gerados < QTD_MAXIMA_ASTEROIDES:
        lista_asteroides.append(randint(0, 2)*2)
        qtd_asteroides_gerados += 1
    else:
        lista_asteroides.append(-1)


def imprimir_asteroides(lista_asteroides:list) -> None:
    display.clear()

    for y, x in enumerate(lista_asteroides):
        if(0<=x<5 and 0<=y<5):
            display.set_pixel(x, y, 9-int(y*1.5))


def piscar_asteroide_atual(x_posicao:int) -> None:
    display.set_pixel(x_posicao, 0, 8)
    sleep_ms(50)
    display.set_pixel(x_posicao, 0, 4)
    sleep_ms(10)


def jogar(piscar:bool=False) -> None:
    lista_asteroides = iniciar_asteroides_jogo()
    imprimir_asteroides(lista_asteroides)
    t_ini = ticks_ms()
    if piscar:
        tempo_espera = 50
    else:
        tempo_espera = 140

    while lista_asteroides[0] != -1:
        if piscar:
            piscar_asteroide_atual(lista_asteroides[0])

        if(button_a.is_pressed() and not button_b.is_pressed() and lista_asteroides[0] == 0) or\
          (button_a.is_pressed() and button_b.is_pressed() and lista_asteroides[0] == 2) or\
          (not button_a.is_pressed() and button_b.is_pressed() and lista_asteroides[0] == 4):
            atualizar_lista_asteroides(lista_asteroides)
            imprimir_asteroides(lista_asteroides)
            sleep_ms(tempo_espera)

    display.scroll("{:.2f}".format((ticks_ms() - t_ini)/1000))
    display.show(Image.HAPPY)



display.show(Image.HAPPY)
while True:
    # Botão A - Inicia jogo com asteroide piscando
    # Botão B - Inicia jogo sem ter asteroide piscando
    if button_a.is_pressed():
        jogar(piscar=True)
    elif button_b.is_pressed():
        jogar(piscar=False)