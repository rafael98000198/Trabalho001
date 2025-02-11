#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.menu import Menu


class Game:
    def __init__(self):
        pygame.get_init()
        self.window = pygame.display.set_mode(size=(800, 600))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #        pygame.quit()  # Close window
            #        quit()  # End pygame
