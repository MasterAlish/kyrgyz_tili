# coding=utf-8
from kg.lang.lang import KyrgyzWord
from kg.lang.suroo._by import ByZatMuchosu
from kg.tests import KGTestCase


class ByMuchosuTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            affix = ByZatMuchosu(KyrgyzWord(word))
            self.assertEqual(affix.make(), expected_form)

    def get_data(self):
        return {
            u'мисал': u'мисалбы',
            u'каз': u'казбы',
            u'кий': u'кийби',
            u'кыл': u'кылбы',
            u'китеп': u'китеппи',
            u'торт': u'тортпу',
            u'уй': u'уйбу',
            u'көрө': u'көрөбү',
            u'теше': u'тешеби',
            u'кийиз': u'кийизби',
        }
