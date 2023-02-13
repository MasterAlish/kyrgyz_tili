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
            'суюк': 'суюгураак',
            'кичик': 'кичигирээк',
            'сонун': 'сонунураак',
            'тоголок': 'тогологураак',
            'арык': 'арыгыраак',
            'кызыл': 'кызылыраак',
            'тайгак': 'тайгагыраак',
            'тозоктой': 'тозоктойураак',
            'кооз': 'коозураак',
            'агыш': 'агышыраак',
            'көгүш': 'көгүшүрөөк',
            'киргил': 'киргилирээк',
            'сулуу': 'сулуураак',
            'кечиримдүү': 'кечиримдүүрөөк',
            'азоо': 'азоораак',
            'азылуу': 'азылуураак',
            'кичи': 'кичирээк',
            'адамгөй': 'адамгөйүрөөк',
        }
