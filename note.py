import re
from settings import Settings


def is_legal_note_str(settings: Settings, note_str):
    first_used_full_octave = max(settings.first_used_octave, 1)
    last_used_full_octave = min(settings.last_used_octave, 7)
    if re.search(f'^[A-G](b|#|)[{first_used_full_octave}-{last_used_full_octave}]$', note_str) and \
            note_str != f'Cb{first_used_full_octave}' and note_str != f'B#{last_used_full_octave}':
        return True
    if note_str == f'B#{first_used_full_octave-1}' or note_str == f'Cb{last_used_full_octave+1}':
        return True
    if settings.first_used_octave == 0 and re.search('^[A-B](b|#|)0$', note_str) and note_str != 'Ab0':
        return True
    if settings.last_used_octave == 8 and re.search('^C(b|)8$', note_str):
        return True
    return False


class Note:
    def __init__(self, settings, note_str):
        if not is_legal_note_str(settings=settings, note_str=note_str):
            raise ValueError

        self.settings = settings
        if len(note_str) == 2:
            self.letter = note_str[0]
            self.accidental = ''
            self.octave_num = int(note_str[1])
        else:  # len = 3
            self.letter = note_str[0]
            self.accidental = note_str[1]
            self.octave_num = int(note_str[2])

    def simplify(self):
        simplified_note_str = self.letter + self.accidental + str(self.octave_num)
        if self.accidental == 'b':
            if self.letter == 'C':
                simplified_note_str = 'B' + str(self.octave_num-1)
            elif self.letter == 'F':
                simplified_note_str = 'E' + str(self.octave_num)
        elif self.accidental == '#':
            if self.letter == 'B':
                simplified_note_str = 'C' + str(self.octave_num+1)
            elif self.letter == 'E':
                simplified_note_str = 'F' + str(self.octave_num)
            else:
                simplified_note_str = chr(ord('A') + (ord(self.letter) - ord('A') + 1) %
                                          (self.settings.OctaveLength-1)) + 'b' + str(self.octave_num)
        return Note(self.settings, simplified_note_str)

    def move(self, half_steps, cyclic=None):
        # If cyclic is None then out of range raises ValueError. A number would get the number of octaves we should add
        # to the result.
        # Behavior at the and and beginning of the piano (0 and 8th octaves) is not well defined and may raise ValueError.
        simplified = self.simplify()
        current_note_index = self.settings.NotesInOctaves.index(simplified.letter + simplified.accidental)  # Letter and accidental.
        new_index = current_note_index + half_steps
        new_octave_num = simplified.octave_num
        if new_index >= len(self.settings.NotesInOctaves):
            new_octave_num += 1
            new_index %= len(self.settings.NotesInOctaves)
        elif new_index < 0:
            new_octave_num -= 1
            new_index %= len(self.settings.NotesInOctaves)
        try:
            return_value = str(Note(self.settings, self.settings.NotesInOctaves[new_index] + str(new_octave_num)))
            return return_value
        except ValueError:
            if cyclic is not None:
                return str(Note(self.settings, self.settings.NotesInOctaves[new_index] +
                                str(range(self.settings.first_used_octave, self.settings.last_used_octave + 1)[
                                        (new_octave_num - self.settings.last_used_octave - 1 + cyclic) %
                                        (self.settings.last_used_octave + 1 - self.settings.first_used_octave)])))
            raise

    def __str__(self):
        return self.letter + self.accidental + str(self.octave_num)
