
class Settings:
    def __init__(self, audio_files_folder, audio_files_type, first_used_octave, last_used_octave, reference_note):
        self.audio_files_folder = audio_files_folder
        self.audio_files_type = audio_files_type

        if not (0 <= first_used_octave <= last_used_octave <= 8):
            raise ValueError

        self.first_used_octave = first_used_octave
        self.last_used_octave = last_used_octave
        self.reference_note = reference_note
        self.OctaveLength = 8

        self.QuitMessages = ['quit', 'exit', 'bye']

        self.NotesInOctaves = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

