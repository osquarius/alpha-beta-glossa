class Constraints(object):


    def __init__(self, x=0.5, y=0.5, width=1.0, height=1.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"anchor at {self.x} parent width, {self.y} parent height, dimensions are {self.width} parent width by {self.height} parent height"