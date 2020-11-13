import argparse
import sys

from settings import Settings
from relative_pitch_exercise import RelativePitchExercise
from chord_kind_exercise import ChordKindExercise
import exercise_properties


def parse_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('exercise', choices=exercise_properties.EXERCISES_LIST,
                        help=f'Select an exercise from the following list: {exercise_properties.EXERCISES_LIST}')
    parser.add_argument('--from', metavar='first_octave', dest='first_octave', type=int, choices=range(0, 9), required=True,
                        help='Select first octave; must satisfy 0 <= first_octave <= 8.')
    parser.add_argument('--to', metavar='last_octave', dest='last_octave', type=int, choices=range(0, 9), required=True,
                        help='Select last octave; must satisfy first_octave <= last_octave <= 8.')

    args = parser.parse_args()
    exe_properties = exercise_properties.ExerciseProperties(args.exercise, args.first_octave, args.last_octave)
    return exe_properties


def main():
    exe_properties = parse_cmd_args()
    try:
        settings = Settings(audio_files_folder='piano-mp3', audio_files_type='mp3',
                            first_used_octave=exe_properties.first_used_octave,
                            last_used_octave=exe_properties.last_used_octave, reference_note='C4')
    except ValueError:
        print('Please make sure 0 <= first_octave <= last_octave <= 8')
        sys.exit()

    if exe_properties.exercise == exercise_properties.EXERCISE.RELATIVE_PITCH.value:
        RPE = RelativePitchExercise(settings, input, print)
        RPE.run_exercise()
    elif exe_properties.exercise == exercise_properties.EXERCISE.CHORD_KIND.value:
        CKE = ChordKindExercise(settings, input, print)
        CKE.run_exercise()


if __name__ == '__main__':
    main()
