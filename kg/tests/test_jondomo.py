from kg.lang.jondomo import Jondomo
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class JondomoTest(KGTestCase):
    def test_ilik(self):
        data = self.get_ilik_data()

        for word, expected_form in data.items():
            jondomo_affix = Jondomo(KyrgyzWord(word))
            self.assertEqual(jondomo_affix.ilik(), expected_form)

    def get_ilik_data(self):
        return {
            'мен': 'менин',
            'ал': 'анын',
            'тигүү': 'тигүүнүн',
            'киши': 'кишинин',
            'сулуу': 'сулуунун',
            'таза': 'тазанын',
            'сан': 'сандын',
            'кишилер': 'кишилердин',
            'кол': 'колдун',
            'көл': 'көлдүн',
            'тарак': 'тарактын',
            'ит': 'иттин',
            'боёк': 'боёктун',
            'түтүк': 'түтүктүн',
        }

    def test_barysh(self):
        data = self.get_barysh_data()

        for word, expected_form in data.items():
            jondomo_affix = Jondomo(KyrgyzWord(word))
            self.assertEqual(jondomo_affix.barysh(), expected_form)

    def get_barysh_data(self):
        return {
            'мен': 'мага',
            'ал': 'ага',
            'тигүү': 'тигүүгө',
            'киши': 'кишиге',
            'сулуу': 'сулууга',
            'таза': 'тазага',
            'сан': 'санга',
            'кишилер': 'кишилерге',
            'кол': 'колго',
            'көл': 'көлгө',
            'тарак': 'таракка',
            'ит': 'итке',
            'боёк': 'боёкко',
            'түтүк': 'түтүккө',
        }

    def test_tabysh(self):
        data = self.get_tabysh_data()

        for word, expected_form in data.items():
            jondomo_affix = Jondomo(KyrgyzWord(word))
            self.assertEqual(jondomo_affix.tabysh(), expected_form)

    def get_tabysh_data(self):
        return {
            'мен': 'мени',
            'ал': 'аны',
            'тигүү': 'тигүүнү',
            'киши': 'кишини',
            'сулуу': 'сулууну',
            'таза': 'тазаны',
            'сан': 'санды',
            'кишилер': 'кишилерди',
            'кол': 'колду',
            'көл': 'көлдү',
            'тарак': 'таракты',
            'ит': 'итти',
            'боёк': 'боёкту',
            'түтүк': 'түтүктү',
        }

    def test_jatysh(self):
        data = self.get_jatysh_data()

        for word, expected_form in data.items():
            jondomo_affix = Jondomo(KyrgyzWord(word))
            self.assertEqual(jondomo_affix.jatysh(), expected_form)

    def get_jatysh_data(self):
        return {
            'мен': 'менде',
            'ал': 'анда',
            'тигүү': 'тигүүдө',
            'киши': 'кишиде',
            'сулуу': 'сулууда',
            'таза': 'тазада',
            'сан': 'санда',
            'кишилер': 'кишилерде',
            'кол': 'колдо',
            'көл': 'көлдө',
            'тарак': 'таракта',
            'ит': 'итте',
            'боёк': 'боёкто',
            'түтүк': 'түтүктө',
        }

    def test_chygysh(self):
        data = self.get_chygysh_data()

        for word, expected_form in data.items():
            jondomo_affix = Jondomo(KyrgyzWord(word))
            self.assertEqual(jondomo_affix.chygysh(), expected_form)

    def get_chygysh_data(self):
        return {
            'мен': 'менен',
            'ал': 'андан',
            'тигүү': 'тигүүдөн',
            'киши': 'кишиден',
            'сулуу': 'сулуудан',
            'таза': 'тазадан',
            'сан': 'сандан',
            'кишилер': 'кишилерден',
            'кол': 'колдон',
            'көл': 'көлдөн',
            'тарак': 'тарактан',
            'ит': 'иттен',
            'боёк': 'боёктон',
            'түтүк': 'түтүктөн',
        }