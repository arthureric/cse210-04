from game.casting.actor import Actor

class Artifact(Actor):
    """An object descendant of Actor
    It is an Actor that represents things (a rock or a gem) that participates in the game. 
    
    The responsibility of Artifact is to act as an Actor with a shape according to its type: rock or gem.

    Attributes:
        The same as Actor: Artifact uses set_text method to store the shape (a text, a letter)
    """

    def __init__(self, artifact_type):
        """Constructs a new Artifact with a specific type, artifact_type.
            This init method is an override of the corresponding Actor method.

        Args:
            artifact_type (str): The specified type of the artifact, as a text.
        """

        # this is the call to inherited __init__ method from the ancestor Actor        
        # all the actions done there will be executed before the specific actions of the Artifact itself
        super().__init__()

        # the lines below will be executed only for Artifact
        # if the artificat is a 'rock', its shape will be an 'O'; if not, it will be a '*' which means a gem
        if artifact_type == 'rock':
            self.set_text('O')
        else:
            self.set_text('*')
