from kg.lang.helps.attrs import *
from kg.lang.jondomo import Jondomo
from kg.lang.lang import KyrgyzWord
from kg.lang.san import San
from kg.lang.taandyk import Taandyk
from kg.tests import KGTestCase


attrs_list = [men, sen, al, biz, siler, alar, siz, sizder]


class JondomoChygyshAfterTaandykTest(KGTestCase):
    def test_chygysh_after_taandyk(self):
        data = self.get_data()
        for word, expected_forms in data.items():
            koptuk = San(KyrgyzWord(word)).koptuk()
            for i in range(len(attrs_list)):
                attr = attrs_list[i]
                jeke_form_expected = expected_forms[0][i]
                taandyk = Taandyk(KyrgyzWord(word)).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo = Jondomo(taandyk)
                self.assertEqual(jondomo.chygysh(), jeke_form_expected)

                koptuk_form_expected = expected_forms[1][i]
                taandyk_koptuk = Taandyk(koptuk).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo_koptuk = Jondomo(taandyk_koptuk)
                self.assertEqual(jondomo_koptuk.chygysh(), koptuk_form_expected)

    def get_data(self):
        return {
            'кит': [
                ['китимден', 'китиңден', 'китинен', 'китибизден', 'китиңерден', 'китинен', 'китиңизден', 'китиңиздерден', ],
                ['киттеримден', 'киттериңден', 'киттеринен', 'киттерибизден', 'киттериңерден', 'киттеринен', 'киттериңизден', 'киттериңиздерден', ]],
            'козу': [
                ['козумдан', 'козуңдан', 'козусунан', 'козубуздан', 'козуңардан', 'козусунан', 'козуңуздан', 'козуңуздардан', ],
                ['козуларымдан', 'козуларыңдан', 'козуларынан', 'козуларыбыздан', 'козуларыңардан', 'козуларынан', 'козуларыңыздан', 'козуларыңыздардан', ]],
            'тор': [
                ['торумдан', 'торуңдан', 'торунан', 'торубуздан', 'торуңардан', 'торунан', 'торуңуздан', 'торуңуздардан', ],
                ['торлорумдан', 'торлоруңдан', 'торлорунан', 'торлорубуздан', 'торлоруңардан', 'торлорунан', 'торлоруңуздан', 'торлоруңуздардан', ]],
            'бөлө': [
                ['бөлөмдөн', 'бөлөңдөн', 'бөлөсүнөн', 'бөлөбүздөн', 'бөлөңөрдөн', 'бөлөсүнөн', 'бөлөңүздөн', 'бөлөңүздөрдөн', ],
                ['бөлөлөрүмдөн', 'бөлөлөрүңдөн', 'бөлөлөрүнөн', 'бөлөлөрүбүздөн', 'бөлөлөрүңөрдөн', 'бөлөлөрүнөн', 'бөлөлөрүңүздөн', 'бөлөлөрүңүздөрдөн', ]]
        }
