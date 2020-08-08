import pygame

class Position(object):


    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def rect(self):
        return pygame.Rect(
            int(self.x - self.width / 2),
            int(self.y - self.height / 2),
            int(self.width),
            int(self.height)
        )
    
    def center_alignment(self, object_width=0, object_height=0):
        return (
            int(self.x - object_width / 2),
            int(self.y - object_height / 2)
        )
    
    def north_west_alignment(self, object_width=0, object_height=0):
        return (
            int(self.x - self.width / 2),
            int(self.x - self.height / 2)
        )
    
    def north_alignment(self, object_width=0, object_height=0):
        return (
            int(self.x - object_width / 2),
            int(self.y - self.height / 2)
        )
    
    def north_east_alignment(self, object_width=0, object_height=0):
        return (
            int(self.x + self.width / 2 - object_width),
            int(self.y - self.height / 2)
        )
    
    def east_alignment(self, object_width=0, object_height=0):
        return (
            int(self.x + self.width / 2 - object_width),
            int(self.y - object_height / 2)
        )
    
    def south_east_alignment(self, object_width=0, object_height=0):
        return (
            int(self.x + self.width / 2 - object_width),
            int(self.y + self.height / 2 - object_height)
        )
    
    def south_alignment(self, object_width=0, object_height=0):
        return (
            int(self.x - object_width / 2),
            int(self.y + self.height / 2 - object_height)
        )
    
    def south_west_alignment(self, object_width=0, object_height=0):
        return (
            int(self.x - self.width / 2),
            int(self.y + self.height / 2 - object_height)
        )
    
    def west_alignment(self, object_width=0, object_height=0):
        return (
            int(self.x - self.width / 2),
            int(self.y - object_height / 2)
        )
    
    def __str__(self):
        return f"positioned at ({self.x}, {self.y}), dimensions are {self.width} by {self.height}"
    
    def __contains__(self, point):
        return (point[0] >= self.x - (self.width // 2)
            and point[0] <= self.x + (self.width // 2)
            and point[1] >= self.y - (self.height // 2)
            and point[1] <= self.y + (self.height // 2)
        )
