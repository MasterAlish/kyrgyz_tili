from kg.lang.lang import KyrgyzWord
from kg.lang.syn._luu import LuuZatMuchosu
from kg.tests import KGTestCase


class ZatLuuMuchoTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            affix = LuuZatMuchosu(KyrgyzWord(word))
            self.assertEqual(affix.make(), expected_form)

    def get_data(self):
        return {
            'кой': 'койлуу',
            'тир': 'тирлүү',
            'чай': 'чайлуу',
            'каш': 'каштуу',
            'торт': 'торттуу',
            'тиш': 'тиштүү',
            'нан': 'нандуу',
            'чечен': 'чечендүү',
            'кеп': 'кептүү',
            'үй': 'үйлүү',
            'январь': 'январдуу',
            'миля': 'милялуу',
            'киль': 'килдүү',
            'чач': 'чачтуу',
        }
