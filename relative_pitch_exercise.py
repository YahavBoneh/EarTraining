from piano import Piano


class RelativePitchExercise:
    def __init__(self, settings, f_input, f_output):
        self.settings = settings
        self.f_input = f_input
        self.f_output = f_output

        try:
            self.piano = Piano(settings)
        except ValueError:
            self.f_output("Invalid reference note.")

    def __play_reference_note(self):
        self.f_output("Reference note: " + self.settings.reference_note)
        self.piano.play(self.settings.reference_note)

    def run_exercise(self):
        help_message = "Enter \"ref\" to hear the reference note. Enter \"again\" to hear the new note again. \n\
        Answer format is [A-G](b|#|)(octave_number)"
        self.f_output(help_message)
        self.__play_reference_note()

        new_random_note_flag = True
        random_note = self.piano.simplify_note(self.piano.random_note())

        while True:
            if new_random_note_flag:
                random_note = self.piano.simplify_note(self.piano.random_note())
            else:
                new_random_note_flag = True
            self.piano.play(random_note)
            input_message = self.f_input()

            if input_message.lower() in self.settings.quit_messages:
                break
            elif input_message.lower() == "ref":
                self.__play_reference_note()
                new_random_note_flag = False
                continue
            elif input_message.lower() == "again":
                new_random_note_flag = False
                continue
            else:
                try:
                    guessed_note = self.piano.simplify_note(input_message)
                    if guessed_note == random_note:
                        self.f_output("Correct.")
                        continue
                    else:
                        self.f_output("Incorrect. Try again.")
                        new_random_note_flag = False
                        continue
                except ValueError:
                    self.f_output(help_message)
                    new_random_note_flag = False
                    continue
