from piano import Piano
from settings import Settings


class BaseExercise:
    def __init__(self, settings: Settings, f_input, f_output):
        self.settings = settings
        self.f_input = f_input
        self.f_output = f_output

        try:
            self.piano = Piano(settings)
        except ValueError:
            self.f_output('Invalid reference note.')
            raise ValueError
