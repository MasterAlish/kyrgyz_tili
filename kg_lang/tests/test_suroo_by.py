# coding=utf-8
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.kyrgyz.suroo._by import ByZatMuchosu
from kg_lang.tests import KGTestCase


class ByMuchosuTest(KGTestCase):
    def test_1(self):

        data = self.get_data()

        for word, form in data.items():
            mucho = ByZatMuchosu(KyrgyzWord(word, False))
            self.assertEqual(mucho.make(), form)

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
