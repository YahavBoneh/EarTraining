
class Settings:
    def __init__(self, audio_files_folder, audio_files_type, first_used_octave, last_used_octave, reference_note):
        self.audio_files_folder = audio_files_folder
        self.audio_files_type = audio_files_type

        self.first_used_octave = first_used_octave
        self.last_used_octave = last_used_octave
        self.reference_note = reference_note
        self.octave_length = 8

        self.quit_messages = ["quit", "exit", "bye"]
