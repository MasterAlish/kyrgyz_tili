from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class KyrgyzWordTest(KGTestCase):
    def test_str_of_kyrgyz_words_returns_raw_word(self):
        self.assertTrue(str(KyrgyzWord('кара')) == 'кара')
        self.assertTrue(str(KyrgyzWord('жашыл')) == 'жашыл')
        self.assertTrue(str(KyrgyzWord('торт')) == 'торт')

    def test_method_is_correct_returns_True_for_correct_words(self):
        self.assertTrue(KyrgyzWord('пробел может быть в слове')._is_correct_word())
        self.assertTrue(KyrgyzWord('черточка-тоже')._is_correct_word())
        self.assertTrue(KyrgyzWord('словобезпробелов')._is_correct_word())
        self.assertTrue(KyrgyzWord('ЗАГЛАВНЫЕТОЛЬКО')._is_correct_word())
        self.assertTrue(KyrgyzWord('Название Чего-то')._is_correct_word())
        self.assertTrue(KyrgyzWord('Вроде все проверено')._is_correct_word())

    def test_method_is_correct_returns_False_for_incorrect_words(self):
        self.assertFalse(KyrgyzWord('буквы 5 с 1 цифрами')._is_correct_word())
        self.assertFalse(KyrgyzWord('1233')._is_correct_word())
        self.assertFalse(KyrgyzWord('подчеркивания_не_должно_быть')._is_correct_word())
        self.assertFalse(KyrgyzWord('english is not supported')._is_correct_word())
        self.assertFalse(KyrgyzWord('! туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord('? туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord('" туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord('\' туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord('& туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord('* туура эмес')._is_correct_word())
        self.assertFalse(KyrgyzWord('() туура эмес')._is_correct_word())
