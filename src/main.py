# -*- coding: utf-8 -*-
# File main.py

from classes.tiled import TiledRenderer
from classes.hero import Hero
from classes.cursor import Cursor
from classes.menu import Menu
from classes.inventory import Item, Bag
from classes.settings import *
import sys
import pygame
from pygame.locals import *
import math

pygame.init()
screen = pygame.display.set_mode((640, 640))
screen_buf = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()
angus = Hero()
hawk = Hero(name="Hawk")
hello = Hero(name="Hello")
world = Hero(name="World")
team = [angus, hawk, hello, world]
bag = Bag()
randobject = Item(name="Random !", quantity=2, effect="None")
bag.useable.append(randobject)

#for item in bag.useable:
#    print("Name : %s\nQuantity : %s\nEffect : %s" % (item.name, item.quantity, item.effect))

hawk.stats.hp -= 10
hawk.stats.level = 15

hello.stats.hp = 1
hello.stats.level = 2

world.stats.hp = 10
world.stats.maxhp = 2000
world.stats.level = 32

class Game(object):
    """ The main Game Class """
    def __init__(self):
        pygame.font.init()
        pygame.display.set_caption('Yet Another SNES RPG')
        pygame.mouse.set_visible(0)
        pygame.key.set_repeat(1, 5)

    def game(self, filename):
        formosa = TiledRenderer(filename)

        run = True
        while run:
            try:
                event = pygame.event.wait()
                if event.type == KEYDOWN:
                    arrow_pressed = False
                    if (event.key == K_LEFT):
                        angus.update(DIR_LEFT)
                        arrow_pressed = True

                    # KEY RIGHT
                    if (event.key == K_RIGHT):
                        angus.update(DIR_RIGHT)
                        arrow_pressed = True

                    # KEY UP
                    if (event.key == K_UP):
                        angus.update(DIR_UP)
                        arrow_pressed = True

                    # KEY DOWN        
                    if (event.key == K_DOWN):
                        angus.update(DIR_DOWN)
                        arrow_pressed = True

                    if arrow_pressed and angus.collidelist(formosa.boxcollider) == -1:
                        angus.move()

                    if (event.key == K_ESCAPE):
                        menu = Menu(screen, team, bag)
                        run = menu.open_menu()

                if event.type == QUIT: run = False

            except KeyboardInterrupt:
                run = False

            formosa.terrain_render(screen_buf)
            formosa.over_terrain_render(screen_buf)
            formosa.under_char_render(screen_buf)
            screen_buf.blit(angus.image,angus.position)
            formosa.over_char_render(screen_buf)
            pygame.transform.scale(screen_buf, screen.get_size(), screen)
            pygame.display.flip()
            clock.tick(60)

    def quit(self):
        pygame.quit()

game = Game()
game.game(MAPS_DIR + "map.tmx")
game.quit()