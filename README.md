# Asteroid Destroyer

Asteroid Destroyer is a game made to be played on a [BBC Micro:bit](https://microbit.org/) and was written in the programming language [MicroPython](https://micropython.org/).

## Game Instructions

#### objective

Destroy all 100 asteroids as fast as you can. The score is based on the time (in seconds) it took the player to destroy all asteroids.

#### Standby mode / Menu

The game starts by loading the standby mode (or menu) which displays a happy face. To start playing, press either button A or button B.

- **Button A** - to start the game with the asteroid to be destroyed blinking

- **Button B** - to start the game without having a flashing asteroid

After any button is pressed, the game and the timer will start. At the end of the game, the time (in seconds) that the player took to destroy all asteroids will be shown, and will return to standby mode (happy face).

#### How to play

Each line has only one asteroid, and it can be on the left (1st Column) in the center (3rd Column) or on the right (5th Column), as you can see in the image below.

![MicroBit](imagens/MicroBit.png)

**Always destroy the asteroid on the first line**, the lines below are a preview of the next asteroids to come.

To destroy the asteroids that are in the first line, just press:
 - **Button A** - To destroy the asteroids in the left column
 - **Button B** - To destroy the asteroids in the right column
 - **Button A + B** - To destroy asteroids in the central column