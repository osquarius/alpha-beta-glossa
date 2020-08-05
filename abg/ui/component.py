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
    
    def set_constraints(self, horizontal, vertical, width, height):
        self.constraints = Constraints(horizontal, vertical, width, height)

    @abc.abstractmethod
    def render(self, canvas):
        pass
    
    def draw(self, canvas):
        if canvas:
            self.render(canvas)
        for component in self.subcomponents:
            component.draw(canvas)
    
    def apply_constraints(self, parent_position):
        self.position.x = parent_position.x * self.constraints.horizontal
        self.position.y = parent_position.y * self.constraints.vertical
        self.position.width = parent_position.width * self.constraints.width
        self.position.height = parent_position.height * self.constraints.height

    def reposition(self, parent_position):
        if parent_position:
            self.apply_constraints(parent_position)
        for component in self.subcomponents:
            component.reposition()



class GraphicalInterface(Component):


    def __init__(self, width, height, background_color=color.WHITE):
        super().__init__(Constraints(0.5, 0.5, 1.0, 1.0))
        self.set_mode(width, height)
        self.background_color = background_color
    
    def set_mode(self, width, height):
        self.reposition(Position(width // 2, height // 2, width, height))
    
    def render(self, canvas):
        canvas.fill(self.background_color)
