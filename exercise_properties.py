from enum import Enum


class EXERCISE(Enum):
    RELATIVE_PITCH = 'relative-pitch'
    CHORD_KIND = 'chord-kind'


EXERCISES_LIST = [EXERCISE.RELATIVE_PITCH.value, EXERCISE.CHORD_KIND.value]


class ExerciseProperties:
    def __init__(self, exercise: EXERCISE, first_used_octave: int, last_used_octave: int):
        self.exercise = exercise
        self.first_used_octave = first_used_octave
        self.last_used_octave = last_used_octave
