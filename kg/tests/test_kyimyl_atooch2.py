from kg.lang.etish.kyimyl_atooch import KyimylAtooch2
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class KyimylAtooch2Test(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            kyimyl_atooch2 = KyimylAtooch2(KyrgyzWord(word))
            self.assertEqual(kyimyl_atooch2.make(), expected_form)

    def get_data(self):
        return {
            'чий': 'чийиш',
            'теп': 'тебиш',
            'чой': 'чоюш',
            'ал': 'алыш',
            'буруй': 'буруюш',
            'токто': 'токтош',
            'каз': 'казыш',
            'кий': 'кийиш',
            'куй': 'куюш',
            'бойтой': 'бойтоюш',
            'кеңей': 'кеңейиш',
            'сай': 'сайыш',
            'бар': 'барыш',
            'акшый': 'акшыйыш',
            'тап': 'табыш',
            'алай': 'алайыш',
            'кара': 'караш',
            'былчый': 'былчыйыш',
            'ой': 'оюш',
            'жаса': 'жасаш',
            'күй': 'күйүш',
            'ташы': 'ташыш',
            'кыл': 'кылыш',
            'төмпөй': 'төмпөйүш',
            'ич': 'ичиш',
            'ук': 'угуш',
            'сүйө': 'сүйөш',
            'боё': 'боёш',
            'тая': 'таяш',
        }
