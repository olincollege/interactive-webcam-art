# interactive-webcam-art
This project uses body tracking through the computer webcam to generate art that is controlled through body movement. 

A few libraries are needed to run this code:

Install [Mediapipe](https://google.github.io/mediapipe/) using: `pip install mediapipe`

Install [OpenCV](https://pypi.org/project/opencv-python/) using: `pip install opencv-python`

Install [pygame](https://www.pygame.org/wiki/GettingStarted) using: `pip install pygame`


Running main.py will generate the tree using data from the webcam. Currently the code is set up so that the number of brances on the tree is determined by the position of a nose on the x-axis. There can be 0-9 branches based on that position. 

![Head Upright](HeadUpright.png "Head Upright")
![Head Turned](HeadTurned.png "Head Turned")

artwork.py is the code for the Art class which is used to generate the tree in main.py. artwork.py uses pygame to make the fractal tree.
bodytracking.py is the code that uses opencv and mediapipe to estimate body position with the webcam. converter.py takes the information from bodytracking.py and formats it in a way which is more useable when interacting with the Art class.