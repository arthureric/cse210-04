class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play and shows the score of the game

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
        _score (int): The value corresponding to the total score of the player.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services, and the game score.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service

        # the player does not start with an amount of points, so he starts with 0
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        # accepts only moviment to left or right

        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        
        # all the artifacts are verifyed if they collides with the robot
        for artifact in artifacts:
            # instead of using equals() method from Point class, it is used touches() (see Point class)
            # when the robot touches the artifact, some actions will happen according to artifact type
            if robot.get_position().touches(artifact.get_position(), self._video_service.get_cell_size()):
                # the "text" attribute indicates the artifact type, because the shape is stored there
                text = artifact.get_text()

                if text == '*':     # it is a gem
                    self._score += 1                    # if the player touches a gem they earn a point
                else:
                    self._score -= 1                    # if the player touches a gem they lose a point
                
                # gems and rocks are removed when the player touches them
                cast.remove_actor("artifacts", artifact)
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()

        self._video_service.clear_buffer()

        # the line below shows the grid; the line is commented
        #self._video_service._draw_grid()

        # the following lines are responsible for showing the score in the banner
        message = 'Score ' + str(self._score)
        banner = cast.get_first_actor("banners")
        banner.set_text(message)
        
        # all the actors have a movement, according to their velocity, including the robot, 
        # and are shown in the screen in their new position
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next(max_x, max_y)
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()