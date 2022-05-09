'''
Artwork contains the class Art, and will be used to generate frames
of the tree.
'''
import pygame
import math

class Art:
    '''
    Store information about the art tree and function to draw the tree.
    '''
    def __init__(self, angle, depth, base_length, fork_angle, x1, y1):

        pygame.init()
        pygame.display.set_caption("Fractal Tree")

        #These parameters will later be values from the body position
        self.angle = angle
        self.depth = depth
        self.base_length = base_length
        self.fork_angle = fork_angle
        self.x1 = x1
        self.y1 = y1
        self.window = pygame.display.set_mode((600, 600))
        self.screen = pygame.display.get_surface()

    def sketch(self, x1, y1, angle, depth):
        '''
        Generate the tree artwork. This takes inputs for x1, y1, angle
        and depth so that the sketch can easily be updated and redrawn
         every frame.
        '''
        if depth > 0:
            x2 = x1 + int(math.cos(math.radians(angle)) * depth * self.base_length)
            y2 = y1 + int(math.sin(math.radians(angle)) * depth * self.base_length)
            pygame.draw.line(self.screen, (255,255,255), (x1, y1), (x2, y2), 2)
            self.sketch(x2, y2, angle - self.fork_angle, depth - 1)
            self.sketch(x2, y2, angle + self.fork_angle, depth - 1)
            pygame.display.flip()



