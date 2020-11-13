from base_exercise import BaseExercise


class RelativePitchExercise(BaseExercise):
    def __play_reference_note(self):
        self.f_output('Reference note: ' + self.settings.reference_note)
        self.piano.play(self.settings.reference_note)

    def run_exercise(self):
        help_message = f'Enter "ref" to hear the reference note. Press Enter to hear the new note again. Enter "ans" for the answer.\n\
Answer format is [A-G](b|#|)[{self.settings.first_used_octave}-{self.settings.last_used_octave}]. Type "exit", \
"quit" or "bye" to get out.'
        self.f_output(help_message)
        self.__play_reference_note()

        new_random_note_flag = True
        random_note = None

        while True:
            if new_random_note_flag:
                random_note = self.piano.simplify_note(self.piano.random_note())
            else:
                new_random_note_flag = True
            self.piano.play(random_note)
            input_message = self.f_input()

            if input_message.lower() in self.settings.QuitMessages:
                break
            elif input_message.lower() == 'ref':
                self.__play_reference_note()
                new_random_note_flag = False
            elif input_message == '':
                new_random_note_flag = False
            elif input_message.lower() == 'ans':
                self.f_output(random_note)
            else:
                try:
                    guessed_note = self.piano.simplify_note(input_message)
                    if guessed_note == random_note:
                        self.f_output('Correct.')
                    else:
                        self.f_output('Incorrect. Try again.')
                        new_random_note_flag = False
                except ValueError:
                    self.f_output(help_message)
                    new_random_note_flag = False
