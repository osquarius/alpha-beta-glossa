import abc

import pygame

import abg.ui.color as color
import abg.ui.attribute as attribute
from abg.ui.geometry import Position
from abg.ui.constraints import Constraints

class Component(abc.ABC):


    def __init__(self, *subcomponents, **attributes):
        self.subcomponents = list(subcomponents)
        self.position = Position()
        self.attributes = attributes
        if attribute.CONSTRAINTS in self.attributes:
            self.constraints = self.attributes[attribute.CONSTRAINTS]
        else:
            self.constraints = Constraints()
    
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


    def __init__(self, width, height, *subcomponents, **attributes):
        super().__init__(*subcomponents, **attributes)
        self.set_mode(width, height)
    
    def set_mode(self, width, height):
        self.reposition(Position(width // 2, height // 2, width, height))
    
    def render(self, canvas):
        if attribute.COLOR in self.attributes:
            canvas.fill(self.attributes[attribute.COLOR])



class Rectangle(Component):


    def __init__(self, *subcomponents, **attributes):
        super().__init__(*subcomponents, **attributes)
    
    def render(self, canvas):
        if attribute.COLOR in self.attributes:
            pygame.draw.rect(canvas, self.attributes[attribute.COLOR], self.position.nw_anchor)
