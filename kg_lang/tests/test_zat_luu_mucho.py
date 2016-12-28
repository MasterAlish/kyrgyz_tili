# coding=utf-8
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.kyrgyz.syn._luu import LuuZatMuchosu
from kg_lang.tests import KGTestCase


class ZatLuuMuchoTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            affix = LuuZatMuchosu(KyrgyzWord(word))
            self.assertEqual(affix.make(), expected_form)

    def get_data(self):
        return {
            u'кой': u'койлуу',
            u'тир': u'тирлүү',
            u'чай': u'чайлуу',
            u'каш': u'каштуу',
            u'торт': u'торттуу',
            u'тиш': u'тиштүү',
            u'нан': u'нандуу',
            u'чечен': u'чечендүү',
            u'кеп': u'кептүү',
            u'үй': u'үйлүү',
            u'январь': u'январдуу',
            u'миля': u'милялуу',
            u'киль': u'килдүү',
            u'чач': u'чачтуу',
        }
