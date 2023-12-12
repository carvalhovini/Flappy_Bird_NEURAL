import pygame

from attrib import Bird, Color, Game, Pipe

def principal():
    atributos = Game.initialize()
    Game.loop(*(atributos))

if __name__ == '__main__':
    principal()
    pygame.quit()
