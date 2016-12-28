# coding=utf-8
from kg.lang.etish.kyimyl_atooch import KyimylAtooch
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class KyimylAtoochTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            affix = KyimylAtooch(KyrgyzWord(word))
            self.assertEqual(affix.make(), expected_form)

    def get_data(self):
        return {
            u'чий': u'чийүү',
            u'теп': u'тебүү',
            u'чой': u'чоюу',
            u'ал': u'алуу',
            u'буруй': u'буруюу',
            u'токто': u'токтоо',
            u'каз': u'казуу',
            u'кий': u'кийүү',
            u'куй': u'куюу',
            u'бойтой': u'бойтоюу',
            u'кеңей': u'кеңейүү',
            u'сай': u'саюу',
            u'бар': u'баруу',
            u'акшый': u'акшыюу',
            u'тап': u'табуу',
            u'алай': u'алаюу',
            u'кара': u'кароо',
            u'былчый': u'былчыюу',
            u'ой': u'оюу',
            u'жаса': u'жасоо',
            u'күй': u'күйүү',
            u'ташы': u'ташуу',
            u'кыл': u'кылуу',
            u'төмпөй': u'төмпөйүү',
            u'ич': u'ичүү',
            u'ук': u'угуу',
            u'сүйө': u'сүйөө',
        }
