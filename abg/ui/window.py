import pygame

import abg.ui.color as color
from abg.ui.component import GraphicalInterface

class Window(object):


    def __init__(self, width, height, caption):
        pygame.display.set_caption(*caption)
        self.gui = GraphicalInterface(width, height)
        self.dimensions = None
        self.canvas = None
        self.resize(width, height)
    
    def add_component(self, component):
        self.gui.add_component(component)

    def resize(self, width, height):
        self.gui.set_mode(width, height)
        self.dimensions = (width, height)
        self.canvas = pygame.display.set_mode(self.dimensions, pygame.RESIZABLE)

    def refresh(self):
        self.gui.draw(self.canvas)
        pygame.display.update()
