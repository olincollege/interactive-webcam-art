'''
Run this file to generate the interactive art.
Main uses functions and classes from bodytracking, artwork, and converter
files.
'''
from bodytracking import Body
from artwork import Art
from converter import Convert

#constantly loop as to keep updating
while True:
    #landmarks is a list of all of the current landmarks
    landmarks = Body.tracking()
    nose = Convert(landmarks,0)
    wrist = Convert(landmarks,16)
    #set paramaters for the drawing
    frame = Art(-90, 5, 10, 20, 300, 550)
    #draw the tree with depth determined by the nose position
    frame.sketch(frame.x1, frame.y1, frame.angle, nose.depth())
