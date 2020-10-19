from piano import Piano
from settings import Settings
from relative_pitch_exercise import RelativePitchExercise

if __name__ == '__main__':
    settings = Settings(audio_files_folder="piano-mp3", audio_files_type="mp3", first_used_octave=4, last_used_octave=4,
                        reference_note="C4")
    RPE = RelativePitchExercise(settings, input, print)
    RPE.run_exercise()
