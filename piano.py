from note import Note
from playsound import playsound
import random


class Piano:
    def __init__(self, settings):
        self.settings = settings
        Note(self.settings.reference_note, settings)  # Will raise ValueError if reference note is illegal.

    def random_note(self):
        letter = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        octave_num = random.randint(self.settings.first_used_octave, self.settings.last_used_octave)
        accidental = ''
        if octave_num == self.settings.first_used_octave and letter == 'C':
            accidental = random.choice(['#', ''])
        elif octave_num == self.settings.last_used_octave and letter == 'B':
            accidental = random.choice(['b', ''])
        else:
            accidental = random.choice(['b', '#', ''])
        return letter + accidental + str(octave_num)

    def simplify_note(self, note_str):
        return str(Note(note_str, self.settings).simplify())

    def play(self, note_str):
        simplified_note = self.simplify_note(note_str)
        note_recording_path = self.settings.audio_files_folder + '\\' + simplified_note + ".mp3"
        playsound(note_recording_path, True)
