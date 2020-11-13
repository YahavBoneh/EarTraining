import unittest
import sys

sys.path.insert(0, '..')
import note
from settings import Settings


class MyTestCase(unittest.TestCase):
    def test_legal_note(self):

        """======================================First settings case======================================"""

        settings1 = Settings(audio_files_folder='piano-mp3', audio_files_type='mp3', first_used_octave=4,
                             last_used_octave=4, reference_note='C4')

        self.assertTrue(note.is_legal_note_str(settings=settings1, note_str='C4'))
        self.assertTrue(note.is_legal_note_str(settings=settings1, note_str='C#4'))
        self.assertTrue(note.is_legal_note_str(settings=settings1, note_str='Bb4'))
        self.assertTrue(note.is_legal_note_str(settings=settings1, note_str='B4'))
        self.assertTrue(note.is_legal_note_str(settings=settings1, note_str='B#3'))
        self.assertTrue(note.is_legal_note_str(settings=settings1, note_str='Cb5'))

        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str=''))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='Cb4'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='B#4'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='F7'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='A0'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='C##4'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='R'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='C#'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='C#9'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='2'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='Db4.2'))
        self.assertFalse(note.is_legal_note_str(settings=settings1, note_str='D$4'))

        """======================================Second settings case======================================"""

        settings2 = Settings(audio_files_folder='piano-mp3', audio_files_type='mp3', first_used_octave=0,
                             last_used_octave=8, reference_note='C4')

        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='C4'))
        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='C#4'))
        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='Bb4'))
        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='B4'))
        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='B#3'))
        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='Cb5'))
        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='Cb4'))
        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='B#4'))
        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='F7'))
        self.assertTrue(note.is_legal_note_str(settings=settings2, note_str='A0'))

        self.assertFalse(note.is_legal_note_str(settings=settings2, note_str=''))
        self.assertFalse(note.is_legal_note_str(settings=settings2, note_str='Ab0'))
        self.assertFalse(note.is_legal_note_str(settings=settings2, note_str='C##4'))
        self.assertFalse(note.is_legal_note_str(settings=settings2, note_str='R'))
        self.assertFalse(note.is_legal_note_str(settings=settings2, note_str='C#'))
        self.assertFalse(note.is_legal_note_str(settings=settings2, note_str='C#9'))
        self.assertFalse(note.is_legal_note_str(settings=settings2, note_str='2'))
        self.assertFalse(note.is_legal_note_str(settings=settings2, note_str='Db4.2'))
        self.assertFalse(note.is_legal_note_str(settings=settings2, note_str='D$4'))

    def test_simplify(self):
        settings = Settings(audio_files_folder='piano-mp3', audio_files_type='mp3', first_used_octave=0,
                            last_used_octave=8, reference_note='C4')
        self.assertEqual("Bb4", str(note.Note(settings=settings, note_str="Bb4").simplify()))
        self.assertEqual("Db5", str(note.Note(settings=settings, note_str="C#5").simplify()))
        self.assertEqual("F3", str(note.Note(settings=settings, note_str="E#3").simplify()))
        self.assertEqual("E6", str(note.Note(settings=settings, note_str="Fb6").simplify()))
        self.assertEqual("C2", str(note.Note(settings=settings, note_str="B#1").simplify()))
        self.assertEqual("B6", str(note.Note(settings=settings, note_str="Cb7").simplify()))
        self.assertEqual("Eb1", str(note.Note(settings=settings, note_str="D#1").simplify()))

    def test_move(self):

        """======================================First settings case======================================"""

        settings1 = Settings(audio_files_folder='piano-mp3', audio_files_type='mp3', first_used_octave=4,
                             last_used_octave=4, reference_note='C4')
        with self.assertRaises(ValueError):
            note.Note(settings=settings1, note_str="B4").move(1)
            note.Note(settings=settings1, note_str="B4").move(10000)
            note.Note(settings=settings1, note_str="D4").move(10)
            note.Note(settings=settings1, note_str="D4").move(-4)
        self.assertEqual("C4", str(note.Note(settings=settings1, note_str="B4").move(1, cyclic=0)))
        self.assertEqual("C4", str(note.Note(settings=settings1, note_str="D4").move(10, cyclic=1)))
        self.assertEqual("G4", str(note.Note(settings=settings1, note_str="D#4").move(4, cyclic=12)))
        self.assertEqual("Gb4", str(note.Note(settings=settings1, note_str="A4").move(-3, cyclic=-4)))
        self.assertEqual("D4", str(note.Note(settings=settings1, note_str="B4").move(27, cyclic=0)))

        """======================================Second settings case======================================"""

        settings2 = Settings(audio_files_folder='piano-mp3', audio_files_type='mp3', first_used_octave=4,
                             last_used_octave=5, reference_note='C4')
        self.assertEqual("C5", str(note.Note(settings=settings2, note_str="B4").move(1, cyclic=0)))
        self.assertEqual("C5", str(note.Note(settings=settings2, note_str="D4").move(10, cyclic=0)))
        self.assertEqual("G4", str(note.Note(settings=settings2, note_str="D#4").move(4, cyclic=None)))
        self.assertEqual("Gb4", str(note.Note(settings=settings2, note_str="A4").move(-3, cyclic=0)))
        self.assertEqual("Db4", str(note.Note(settings=settings2, note_str="A5").move(4, cyclic=0)))
        self.assertEqual("Db5", str(note.Note(settings=settings2, note_str="A5").move(4, cyclic=1)))
        self.assertEqual("Db5", str(note.Note(settings=settings2, note_str="A5").move(4, cyclic=-1)))
        self.assertEqual("B5", str(note.Note(settings=settings2, note_str="C4").move(-1, cyclic=0)))


if __name__ == '__main__':
    unittest.main()
