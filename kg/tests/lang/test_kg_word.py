# coding=utf-8
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class KyrgyzWordTest(KGTestCase):
    def test_unicode_of_kyrgyz_words_returns_the_word_itself(self):
        self.assertEqual(unicode(KyrgyzWord(u'кара')), u'кара')
        self.assertEqual(unicode(KyrgyzWord(u'жашыл')), u'жашыл')
        self.assertEqual(unicode(KyrgyzWord(u'торт')), u'торт')

    def test_str_of_kyrgyz_words_returns_raw_word(self):
        self.assertTrue(str(KyrgyzWord(u'кара')) == 'кара')
        self.assertTrue(str(KyrgyzWord(u'жашыл')) == 'жашыл')
        self.assertTrue(str(KyrgyzWord(u'торт')) == 'торт')

    def test_method_is_correct_returns_True_for_correct_words(self):
        self.assertTrue(KyrgyzWord(u'пробел может быть в слове')._is_correct_word())
        self.assertTrue(KyrgyzWord(u'черточка-тоже')._is_correct_word())
        self.assertTrue(KyrgyzWord(u'словобезпробелов')._is_correct_word())
        self.assertTrue(KyrgyzWord(u'ЗАГЛАВНЫЕТОЛЬКО')._is_correct_word())
        self.assertTrue(KyrgyzWord(u'Название Чего-то')._is_correct_word())
        self.assertTrue(KyrgyzWord(u'Вроде все проверено')._is_correct_word())

    def test_method_is_correct_returns_False_for_incorrect_words(self):
        self.assertFalse(KyrgyzWord(u'буквы 5 с 1 цифрами')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'1233')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'подчеркивания_не_должно_быть')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'english is not supported')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'! туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'? туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'" туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'\' туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'& туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'* туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord(u'() туура эмес')._is_correct_word())
