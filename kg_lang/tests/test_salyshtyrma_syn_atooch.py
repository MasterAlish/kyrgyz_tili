# coding=utf-8
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.kyrgyz.syn_atooch import SalyshtyrmaSynAtooch
from kg_lang.tests import KGTestCase


class SalyshtyrmaSynAtoochTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, form in data.items():
            syn_atooch = SalyshtyrmaSynAtooch(KyrgyzWord(word, False))
            self.assertEqual(syn_atooch.make(), form)

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
