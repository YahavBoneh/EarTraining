from base_exercise import BaseExercise
import random


class ChordKindExercise(BaseExercise):
    # def __play_random_major_triad(self, root):
    #     self.piano.play_chord_by_intervals(root, 4, 3)
    #
    # def __play_random_minor_triad(self, root):
    #     self.piano.play_chord_by_intervals(root, 3, 4)
    #
    # def __play_random_diminished_triad(self, root):
    #     self.piano.play_chord_by_intervals(root, 3, 3)
    #
    # def __play_random_augmented_triad(self, root):
    #     self.piano.play_chord_by_intervals(root, 4, 4)
    #
    # def __play_random_major_seven(self, root):
    #     self.piano.play_chord_by_intervals(root, 4, 3, 4)
    #
    # def __play_random_minor_seven(self, root):
    #     self.piano.play_chord_by_intervals(root, 3, 4, 3)
    #
    # def __play_random_dominant_seven(self, root):
    #     self.piano.play_chord_by_intervals(root, 4, 3, 3)
    #
    # def __play_random_diminished_seven(self, root):
    #     self.piano.play_chord_by_intervals(root, 3, 3, 3)
    #
    # def __play_random_minor_major_seven(self, root):
    #     self.piano.play_chord_by_intervals(root, 3, 4, 4)
    #
    # def __play_random_diminished_major_seven(self, root):
    #     self.piano.play_chord_by_intervals(root, 3, 3, 5)
    #
    # def __play_random_major_seven_sharp_five(self, root):
    #     self.piano.play_chord_by_intervals(root, 4, 4, 3)
    #
    # def __play_random_minor_seven_flat_five(self, root):
    #     self.piano.play_chord_by_intervals(root, 3, 3, 4)

    chord_kinds_intervals = {
        "M": (4, 3),  # Major triad.
        "m": (3, 4),  # Minor triad.
        "dim": (3, 3),  # Diminished triad.
        "aug": (4, 4),  # Augmented triad.
        "M7": (4, 3, 4),  # Major seven.
        "m7": (3, 4, 3),  # Minor seven.
        "dom7": (4, 3, 3),  # Dominant seven.
        "dim7": (3, 3, 3),  # Diminished seven.
        "mM7": (3, 4, 4),  # Minor major seven.
        "dimM7": (3, 3, 5),  # Diminished major seven.
        "M7#5": (4, 4, 3),  # Major seven sharp five.
        "m7b5": (3, 3, 4)  # Minor seven flat five.
    }

    def run_exercise(self):
        help_message = """Enter "sep" to hear each note of the chord separately. Press Enter to hear the chord again. Enter "ans" for the answer. Answer format is:
        M: Major triad.
        m: Minor triad.
        dim: Diminished triad.
        aug: Augmented triad.
        M7: Major seven.
        m7: Minor seven.
        dom7: Dominant seven.
        dim7: Diminished seven.
        mM7: Minor major seven.
        dimM7: Diminished major seven.
        M7#5: Major seven sharp five.
        m7b5: Minor seven flat five."""
        self.f_output(help_message)

        new_random_chord_flag = True
        random_chord_kind = None
        random_root = None
        play_separately = False

        while True:
            if new_random_chord_flag:
                random_chord_kind = random.choice(list(self.chord_kinds_intervals.keys()))
                random_root = self.piano.random_note()
            else:
                new_random_chord_flag = True
            self.piano.play_chord_by_intervals(random_root, *self.chord_kinds_intervals[random_chord_kind], play_separately=play_separately)
            play_separately = False

            input_message = self.f_input()
            if input_message.lower() in self.settings.QuitMessages:
                break
            elif input_message.lower() == 'sep':
                play_separately = True
                new_random_chord_flag = False
            elif input_message in self.chord_kinds_intervals.keys():
                if input_message == random_chord_kind:
                    self.f_output('Correct.')
                else:
                    self.f_output('Incorrect. Try again.')
                    new_random_chord_flag = False
            elif input_message == '':
                new_random_chord_flag = False
            elif input_message == 'ans':
                self.f_output(random_chord_kind)
                self.piano.play_chord_by_intervals(random_root, *self.chord_kinds_intervals[random_chord_kind])
            else:
                self.f_output(help_message)
                new_random_chord_flag = False

