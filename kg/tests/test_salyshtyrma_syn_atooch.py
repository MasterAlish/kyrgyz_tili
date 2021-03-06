# coding=utf-8
from kg.lang.lang import KyrgyzWord
from kg.lang.syn_atooch import SalyshtyrmaSynAtooch
from kg.tests import KGTestCase


class SalyshtyrmaSynAtoochTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            syn_atooch = SalyshtyrmaSynAtooch(KyrgyzWord(word))
            self.assertEqual(syn_atooch.make(), expected_form)

    def get_data(self):
        return {
            u'суюк': u'суюгураак',
            u'кичик': u'кичигирээк',
            u'сонун': u'сонунураак',
            u'тоголок': u'тогологураак',
            u'арык': u'арыгыраак',
            u'кызыл': u'кызылыраак',
            u'тайгак': u'тайгагыраак',
            u'тозоктой': u'тозоктойураак',
            u'кооз': u'коозураак',
            u'агыш': u'агышыраак',
            u'көгүш': u'көгүшүрөөк',
            u'киргил': u'киргилирээк',
            u'сулуу': u'сулуураак',
            u'кечиримдүү': u'кечиримдүүрөөк',
            u'азоо': u'азоораак',
            u'азылуу': u'азылуураак',
            u'кичи': u'кичирээк',
            u'адамгөй': u'адамгөйүрөөк',
        }
