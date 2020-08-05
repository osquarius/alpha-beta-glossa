import pygame

import abg.ui.component as ui
from abg.ui.window import Window
from abg.ui.constraints import Constraints

class AlphaBetaGlossa(object):


    def __init__(self, caption, fps=30):
        pygame.init()
        self.window = Window(640, 480, caption)
        self.running = False
        self.fps = fps
    
    def __del__(self):
        pygame.quit()
    
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