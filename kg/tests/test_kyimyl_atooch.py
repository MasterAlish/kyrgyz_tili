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
            'чий': 'чийүү',
            'теп': 'тебүү',
            'чой': 'чоюу',
            'ал': 'алуу',
            'буруй': 'буруюу',
            'токто': 'токтоо',
            'каз': 'казуу',
            'кий': 'кийүү',
            'куй': 'куюу',
            'бойтой': 'бойтоюу',
            'кеңей': 'кеңейүү',
            'сай': 'саюу',
            'бар': 'баруу',
            'акшый': 'акшыюу',
            'тап': 'табуу',
            'алай': 'алаюу',
            'кара': 'кароо',
            'былчый': 'былчыюу',
            'ой': 'оюу',
            'жаса': 'жасоо',
            'күй': 'күйүү',
            'ташы': 'ташуу',
            'кыл': 'кылуу',
            'төмпөй': 'төмпөйүү',
            'ич': 'ичүү',
            'ук': 'угуу',
            'сүйө': 'сүйөө',
        }
