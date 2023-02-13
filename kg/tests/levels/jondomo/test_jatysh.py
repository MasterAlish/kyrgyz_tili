from kg.lang.helps.attrs import *
from kg.lang.jondomo import Jondomo
from kg.lang.lang import KyrgyzWord
from kg.lang.san import San
from kg.lang.taandyk import Taandyk
from kg.tests import KGTestCase


attrs_list = [men, sen, al, biz, siler, alar, siz, sizder]


class JondomoJatyshAfterTaandykTest(KGTestCase):
    def test_jatysh_after_taandyk(self):
        data = self.get_data()
        for word, expected_forms in data.items():
            koptuk = San(KyrgyzWord(word)).koptuk()
            for i in range(len(attrs_list)):
                attr = attrs_list[i]
                jeke_form_expected = expected_forms[0][i]
                taandyk = Taandyk(KyrgyzWord(word)).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo = Jondomo(taandyk)
                self.assertEqual(jondomo.jatysh(), jeke_form_expected)

                koptuk_form_expected = expected_forms[1][i]
                taandyk_koptuk = Taandyk(koptuk).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo_koptuk = Jondomo(taandyk_koptuk)
                self.assertEqual(jondomo_koptuk.jatysh(), koptuk_form_expected)

    def get_data(self):
        return {
            'кит': [
                ['китимде', 'китиңде', 'китинде', 'китибизде', 'китиңерде', 'китинде', 'китиңизде', 'китиңиздерде', ],
                ['киттеримде', 'киттериңде', 'киттеринде', 'киттерибизде', 'киттериңерде', 'киттеринде', 'киттериңизде', 'киттериңиздерде', ]],
            'козу': [
                ['козумда', 'козуңда', 'козусунда', 'козубузда', 'козуңарда', 'козусунда', 'козуңузда', 'козуңуздарда', ],
                ['козуларымда', 'козуларыңда', 'козуларында', 'козуларыбызда', 'козуларыңарда', 'козуларында', 'козуларыңызда', 'козуларыңыздарда', ]],
            'тор': [
                ['торумда', 'торуңда', 'торунда', 'торубузда', 'торуңарда', 'торунда', 'торуңузда', 'торуңуздарда', ],
                ['торлорумда', 'торлоруңда', 'торлорунда', 'торлорубузда', 'торлоруңарда', 'торлорунда', 'торлоруңузда', 'торлоруңуздарда', ]],
            'бөлө': [
                ['бөлөмдө', 'бөлөңдө', 'бөлөсүндө', 'бөлөбүздө', 'бөлөңөрдө', 'бөлөсүндө', 'бөлөңүздө', 'бөлөңүздөрдө', ],
                ['бөлөлөрүмдө', 'бөлөлөрүңдө', 'бөлөлөрүндө', 'бөлөлөрүбүздө', 'бөлөлөрүңөрдө', 'бөлөлөрүндө', 'бөлөлөрүңүздө', 'бөлөлөрүңүздөрдө', ]]
        }
