from playsound import playsound
import random
from multiprocessing import Process
from functools import cmp_to_key

from note import Note
from settings import Settings


def are_processes_dead(processes):
    for process in processes:
        if process.is_alive():
            return False
    return True


def move_note(settings, note_str, interval):
    return str(Note(settings, note_str).move(interval, cyclic=-1))


def compare_notes(note_str1, note_str2):
    empty_settings = Settings(audio_files_folder=None, audio_files_type=None, first_used_octave=0,
                              last_used_octave=8, reference_note=None)
    note1 = Note(empty_settings, note_str1).simplify()
    note2 = Note(empty_settings, note_str2).simplify()
    if note1.octave_num != note2.octave_num:
        return note1.octave_num - note2.octave_num
    else:
        return empty_settings.NotesInOctaves.index(str(note1)[:-1]) - empty_settings.NotesInOctaves.index(str(note2)[:-1])


class Piano:
    def __init__(self, settings: Settings):
        self.settings = settings
        Note(settings, self.settings.reference_note)  # Will raise ValueError if reference note is illegal.

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
        return str(Note(self.settings, note_str).simplify())

    def _play_single_note(self, note_str):  # Can't be __ type because multiprocessing needs access.
        simplified_note = self.simplify_note(note_str)
        note_recording_path = f"{self.settings.audio_files_folder}\\{simplified_note}.{self.settings.audio_files_type}"
        playsound(note_recording_path, True)

    def play(self, *notes_str, play_separately=False, play_by_order=True):
        if play_separately:
            modified_notes_str = list(notes_str).copy()
            if play_by_order:
                modified_notes_str = sorted(list(notes_str), key=cmp_to_key(compare_notes))
            for note in modified_notes_str:
                self._play_single_note(note)
            return

        processes = []
        for note in notes_str:
            processes.append(Process(target=self._play_single_note, args=[note]))
        for process in processes:
            process.start()

        while not are_processes_dead(processes):
            continue

    def play_chord_by_intervals(self, root, *intervals, play_separately=False):
        notes = [root]
        for interval in intervals:
            notes.append(move_note(self.settings, notes[-1], interval))
        self.play(*notes, play_separately=play_separately)
