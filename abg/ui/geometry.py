import pygame

class Position(object):


    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def nw_anchor(self):
        return pygame.Rect(
            int(self.x - self.width / 2),
            int(self.y - self.height / 2),
            int(self.width),
            int(self.height)
            )
