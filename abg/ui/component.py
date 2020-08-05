import abc

import pygame

import abg.ui.color as color
from abg.ui.geometry import Position
from abg.ui.constraints import Constraints

class Component(abc.ABC):


    def __init__(self, constraints=Constraints()):
        self.subcomponents = []
        self.position = Position()
        self.constraints = constraints
    
    def add_component(self, component):
        self.subcomponents.append(component)
    
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
        print(id(self), type(self))
        x = parent.x + (self.constraints.x - 0.5) * parent.width
        y = parent.y + (self.constraints.y - 0.5) * parent.height
        width = parent.width * self.constraints.width
        height = parent.height * self.constraints.height
        self.position = Position(x, y, width, height)

    def reposition(self, parent):
        if parent and self.constraints:
            self.apply_constraints(parent)
        for component in self.subcomponents:
            component.reposition(self.position)



class GraphicalInterface(Component):


    def __init__(self, width, height, background_color=color.WHITE):
        super().__init__(Constraints(0.5, 0.5, 1.0, 1.0))
        self.set_mode(width, height)
        self.background_color = background_color
    
    def set_mode(self, width, height):
        self.reposition(Position(width // 2, height // 2, width, height))
    
    def render(self, canvas):
        canvas.fill(self.background_color)



class Rectangle(Component):


    def __init__(self, constraints=Constraints(), fill_color=color.RED):
        super().__init__(constraints)
        self.fill_color = fill_color
    
    def render(self, canvas):
        pygame.draw.rect(canvas, self.fill_color, self.position.nw_anchor)
