import abc

import pygame

from abg.ui import colors
from abg.ui import font
from abg.ui.geometry import Position
from abg.ui.constraints import Constraints

class Component(abc.ABC):


    def __init__(self, constraints=None, *subcomponents):
        if constraints:
            self.constraints = constraints
        else:
            self.constraints = Constraints()
        self.subcomponents = list(subcomponents)
        self.position = Position()
    
    def add_components(self, *components):
        self.subcomponents.extend(components)
    
    def set_constraints(self, constraints):
        self.constraints = constraints
    
    def set_constraints(self, x, y, width, height):
        self.constraints = Constraints(x, y, width, height)

    @abc.abstractmethod
    def render(self, canvas):
        pass
    
    def draw(self, canvas):
        if canvas:
            self.render(canvas)
        for component in self.subcomponents:
            component.draw(canvas)
    
    def apply_constraints(self, parent):
        x = parent.x + (self.constraints.x - 0.5) * parent.width
        y = parent.y + (self.constraints.y - 0.5) * parent.height
        width = parent.width * self.constraints.width
        height = parent.height * self.constraints.height
        self.position = Position(x, y, width, height)

    def reposition(self, parent):
        if parent:
            self.apply_constraints(parent)
        for component in self.subcomponents:
            component.reposition(self.position)



class GraphicalInterface(Component):


    def __init__(self, width, height, fill_color=None, *subcomponents):
        super().__init__(*subcomponents)
        self.set_mode(width, height)
        self.fill_color = fill_color
    
    def set_mode(self, width, height):
        self.reposition(Position(width // 2, height // 2, width, height))
    
    def render(self, canvas):
        if self.fill_color:
            canvas.fill(self.fill_color)



class Rectangle(Component):


    def __init__(self, fill_color=None, constraints=None, *subcomponents):
        super().__init__(constraints, *subcomponents)
        self.fill_color = fill_color
    
    def render(self, canvas):
        if self.fill_color:
            pygame.draw.rect(canvas, self.fill_color, self.position.rect)



class Text(Component):


    def __init__(
            self,
            text,
            font_color=colors.BLACK,
            max_font_size=None,
            constraints=None,
            *subcomponents
    ):
        super().__init__(constraints, *subcomponents)
        self.__text = text
        self.__color = font_color
        self.max_font_size = max_font_size
        self.surface = None
        self.create_surface()
    
    def create_surface(self):
        self.surface = font.best_fit_text_surface(
            self.text,
            self.position.width,
            self.position.height
        )
    
    def reposition(self, parent):
        super().reposition(parent)
        self.create_surface()
    
    def render(self, canvas):
        canvas.blit(
            self.surface,
            self.position.center_alignment(
                self.surface.get_width(),
                self.surface.get_height()
            )
        )
    
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, new_text):
        if new_text != self.__text:
            self.__text = new_text
            self.create_surface()
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        if new_color != self.__color:
            self.__color = new_color
            self.create_surface()
