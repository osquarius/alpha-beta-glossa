import pygame

from abg.ui import colors
from abg.ui.gui import GraphicalInterface

class Window(object):


    def __init__(self, width, height, caption):
        pygame.display.set_caption(*caption)
        self.gui = GraphicalInterface(width, height, fill_color=colors.WHITE)
        self.dimensions = None
        self.canvas = None
        self.resize(width, height)
    
    def add_components(self, *components):
        self.gui.add_components(*components)

    def resize(self, width, height):
        self.gui.set_mode(width, height)
        self.dimensions = (width, height)
        self.canvas = pygame.display.set_mode(self.dimensions, pygame.RESIZABLE)

    def refresh(self):
        self.gui.draw(self.canvas)
        pygame.display.update()
