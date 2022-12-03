import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 20      # The original value was 40
# This new constant is to define the speed at which Artifacts fall 
DOWN_SPEED = int(CELL_SIZE / 3)  # I decided to use some number relative to the cell size, but any integer value greater than 0 can be used.  

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot

    # The robot is positioned in the center of the lower part of the screen
    x = int(COLS / 2) * CELL_SIZE           
    y = MAX_Y - CELL_SIZE
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts

    for n in range(DEFAULT_ARTIFACTS):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        # There are only two types of artifact: gems and rocks.        
        artifact_type = random.randint(0, 1)    # this randomization will generate only 0 and 1
        if artifact_type == 0:
            artifact = Artifact('rock')         # the Artifact is created as a 'rock'
        else:
            artifact = Artifact('gem')          # the Artifact is created as a 'gem'

        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)

        # the velocity of an Artifact is the speed of the fall
        speed = random.randint(1, DOWN_SPEED)       # the DOWN_SPEED is a new constant here
        artifact.set_velocity(Point(0, speed))      # speed will enable varying speeds by random

        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()