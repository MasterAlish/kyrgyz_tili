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
            'мисал': 'мисалбы',
            'каз': 'казбы',
            'кий': 'кийби',
            'кыл': 'кылбы',
            'китеп': 'китеппи',
            'торт': 'тортпу',
            'уй': 'уйбу',
            'көрө': 'көрөбү',
            'теше': 'тешеби',
            'кийиз': 'кийизби',
        }
