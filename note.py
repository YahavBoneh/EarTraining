import re


def is_legal_note_str(note_str, settings):
    first_used_full_octave = max(settings.first_used_octave, 1)
    last_used_full_octave = min(settings.last_used_octave, 7)
    if re.search(f"^[A-G](b|#|)[{first_used_full_octave}-{last_used_full_octave}]$", note_str) and \
            note_str != f"Cb{first_used_full_octave}" and note_str != f"B#{last_used_full_octave}":
        return True
    if settings.first_used_octave == 0 and re.search("^[A-B](b|#|)0$", note_str) and note_str != "Ab0":
        return True
    if settings.last_used_octave == 8 and re.search("^C(b|)8$", note_str):
        return True
    return False


class Note:
    def __init__(self, note_str, settings):
        if not is_legal_note_str(note_str=note_str, settings=settings):
            raise ValueError

        self.settings = settings
        if len(note_str) == 2:
            self.letter = note_str[0]
            self.accidental = ''
            self.octave_num = note_str[1]
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
                                          (self.settings.octave_length-1)) + 'b' + str(self.octave_num)
        return Note(simplified_note_str, self.settings)

    def __str__(self):
        return self.letter + self.accidental + str(self.octave_num)
