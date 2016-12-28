# coding=utf-8
from kg.lang.affixing import apply_affix
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class ApplyAffixMethodAndChangeHistoryTest(KGTestCase):
    def test_method_can_apply_two_level_affix(self):
        word_object = KyrgyzWord(u"бала")
        result = apply_affix({'taandyk': ['jondomo']}, word_object)
        self.assertTrue(len(result) > 2)

    def test_second_level_affix_results(self):
        word_object = KyrgyzWord(u"бала")
        result = apply_affix({'taandyk': ['jondomo']}, word_object)
        baldarybyz = None
        for name, affix in result.items():
            if u"балдарыбыз" == affix.word_object.word:
                baldarybyz = affix.word_object
                break
        self.assertTrue(baldarybyz is not None)
        self.assertEqual(len(baldarybyz.change_history), 2)
        self.assertEqual(baldarybyz.change_history[0].affix, 'koptuk')
        self.assertEqual(baldarybyz.change_history[1].affix, 'taandyk')
        self.assertEqual(baldarybyz.change_history[1].attrs.jak, 1)
        self.assertEqual(baldarybyz.change_history[1].attrs.jeke, False)
        self.assertEqual(baldarybyz.change_history[1].attrs.sylyk, False)
        self.assertEqual(baldarybyz.change_history[0].index, 3)
        self.assertEqual(baldarybyz.change_history[1].index, 6)

    def test_third_level_affix_results(self):
        word_object = KyrgyzWord(u"ташта")
        result = apply_affix({'ba': [{'gan': ['jondomo']}]}, word_object)
        tashtabagander = None
        for name, affix in result.items():
            if u"таштабагандар" == affix.word_object.word:
                tashtabagander = affix.word_object
                break
        self.assertTrue(tashtabagander is not None)
        self.assertEqual(len(tashtabagander.change_history), 3)
        self.assertEqual(tashtabagander.change_history[0].affix, 'ba')
        self.assertEqual(tashtabagander.change_history[1].affix, 'gan')
        self.assertEqual(tashtabagander.change_history[2].affix, 'koptuk')
        self.assertEqual(tashtabagander.change_history[0].index, 5)
        self.assertEqual(tashtabagander.change_history[1].index, 7)
        self.assertEqual(tashtabagander.change_history[2].index, 10)

