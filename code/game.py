import pygame
from pygame.examples.aliens import Player

from entity import Entity
from screen import Screen
from map import Map
class Game:

    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = Map(self.screen)
        self.entity = Entity()
        self.map.add_player(self.entity)

    def run(self):
        while self.running:
            self.map.update()
            self.screen.update()
