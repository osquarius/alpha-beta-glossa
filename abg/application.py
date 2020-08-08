import pygame

from abg.ui import gui
from abg.ui import colors
from abg.ui.window import Window
from abg.ui.constraints import Constraints

class AlphaBetaGlossa(object):


    def __init__(self, caption, fps=20):
        pygame.init()
        self.window = Window(640, 480, caption)
        self.running = False
        self.fps = fps
        self.build_gui()
    
    def __del__(self):
        self.deactivate()
        pygame.quit()
    
    def build_gui(self):
        rectangle = gui.Rectangle(
            constraints=Constraints(0.5, 0.5, 0.9, 0.33),
            )
        text = gui.Text("Μιλάτε ελληνικά;")
        rectangle.add_components(text)
        self.window.add_components(rectangle)
    
    def run(self):
        self.activate()
        clock = pygame.time.Clock()
        while self.running:
            self.window.refresh()
            self.update()
            clock.tick(self.fps)
    
    def update(self):
        self.handle_events()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.deactivate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.deactivate()
            elif event.type == pygame.VIDEORESIZE:
                self.window.resize(event.w, event.h)
    
    def activate(self):
        self.running = True

    def deactivate(self):
        self.running = False
