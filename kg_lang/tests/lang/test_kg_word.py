# coding=utf-8
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.tests import KGTestCase


class KyrgyzWordTest(KGTestCase):
    def test_unicode_of_kyrgyz_words_returns_word(self):
        self.assertEqual(unicode(KyrgyzWord(u'кара')), u'кара')
        self.assertEqual(unicode(KyrgyzWord(u'жашыл')), u'жашыл')
        self.assertEqual(unicode(KyrgyzWord(u'торт')), u'торт')

    def test_str_of_kyrgyz_words_returns_raw_word(self):
        self.assertTrue(str(KyrgyzWord(u'кара')) == 'кара')
        self.assertTrue(str(KyrgyzWord(u'жашыл')) == 'жашыл')
        self.assertTrue(str(KyrgyzWord(u'торт')) == 'торт')
