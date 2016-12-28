# coding=utf-8
from kg_lang.kyrgyz.jondomo import Jondomo
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.tests import KGTestCase


class JondomoTest(KGTestCase):
    def test_ilik(self):

        data = self.get_ilik_data()

        for word, form in data.items():
            atooch = Jondomo(KyrgyzWord(word, False))
            self.assertEqual(atooch.ilik(), form)

    def get_ilik_data(self):
        return {
            u'мен': u'менин',
            u'ал': u'анын',
            u'тигүү': u'тигүүнүн',
            u'киши': u'кишинин',
            u'сулуу': u'сулуунун',
            u'таза': u'тазанын',
            u'сан': u'сандын',
            u'кишилер': u'кишилердин',
            u'кол': u'колдун',
            u'көл': u'көлдүн',
            u'тарак': u'тарактын',
            u'ит': u'иттин',
            u'боёк': u'боёктун',
            u'түтүк': u'түтүктүн',
        }

    def test_barysh(self):

        data = self.get_barysh_data()

        for word, form in data.items():
            atooch = Jondomo(KyrgyzWord(word, False))
            self.assertEqual(atooch.barysh(), form)

    def get_barysh_data(self):
        return {
            u'мен': u'мага',
            u'ал': u'ага',
            u'тигүү': u'тигүүгө',
            u'киши': u'кишиге',
            u'сулуу': u'сулууга',
            u'таза': u'тазага',
            u'сан': u'санга',
            u'кишилер': u'кишилерге',
            u'кол': u'колго',
            u'көл': u'көлгө',
            u'тарак': u'таракка',
            u'ит': u'итке',
            u'боёк': u'боёкко',
            u'түтүк': u'түтүккө',
        }

    def test_tabysh(self):

        data = self.get_tabysh_data()

        for word, form in data.items():
            atooch = Jondomo(KyrgyzWord(word, False))
            self.assertEqual(atooch.tabysh(), form)

    def get_tabysh_data(self):
        return {
            u'мен': u'мени',
            u'ал': u'аны',
            u'тигүү': u'тигүүнү',
            u'киши': u'кишини',
            u'сулуу': u'сулууну',
            u'таза': u'тазаны',
            u'сан': u'санды',
            u'кишилер': u'кишилерди',
            u'кол': u'колду',
            u'көл': u'көлдү',
            u'тарак': u'таракты',
            u'ит': u'итти',
            u'боёк': u'боёкту',
            u'түтүк': u'түтүктү',
        }

    def test_jatysh(self):

        data = self.get_jatysh_data()

        for word, form in data.items():
            atooch = Jondomo(KyrgyzWord(word, False))
            self.assertEqual(atooch.jatysh(), form)

    def get_jatysh_data(self):
        return {
            u'мен': u'менде',
            u'ал': u'анда',
            u'тигүү': u'тигүүдө',
            u'киши': u'кишиде',
            u'сулуу': u'сулууда',
            u'таза': u'тазада',
            u'сан': u'санда',
            u'кишилер': u'кишилерде',
            u'кол': u'колдо',
            u'көл': u'көлдө',
            u'тарак': u'таракта',
            u'ит': u'итте',
            u'боёк': u'боёкто',
            u'түтүк': u'түтүктө',
        }

    def test_chygysh(self):

        data = self.get_chygysh_data()

        for word, form in data.items():
            atooch = Jondomo(KyrgyzWord(word, False))
            self.assertEqual(unicode(atooch.chygysh()), form)

    def get_chygysh_data(self):
        return {
            u'мен': u'менен',
            u'ал': u'андан',
            u'тигүү': u'тигүүдөн',
            u'киши': u'кишиден',
            u'сулуу': u'сулуудан',
            u'таза': u'тазадан',
            u'сан': u'сандан',
            u'кишилер': u'кишилерден',
            u'кол': u'колдон',
            u'көл': u'көлдөн',
            u'тарак': u'тарактан',
            u'ит': u'иттен',
            u'боёк': u'боёктон',
            u'түтүк': u'түтүктөн',
        }