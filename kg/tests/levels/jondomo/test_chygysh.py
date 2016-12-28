# coding=utf-8
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
                self.assertEqual(unicode(jondomo.chygysh()), jeke_form_expected)

                koptuk_form_expected = expected_forms[1][i]
                taandyk_koptuk = Taandyk(koptuk).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo_koptuk = Jondomo(taandyk_koptuk)
                self.assertEqual(unicode(jondomo_koptuk.chygysh()), koptuk_form_expected)

    def get_data(self):
        return {
            u'кит': [
                [u'китимден', u'китиңден', u'китинен', u'китибизден', u'китиңерден', u'китинен', u'китиңизден', u'китиңиздерден', ],
                [u'киттеримден', u'киттериңден', u'киттеринен', u'киттерибизден', u'киттериңерден', u'киттеринен', u'киттериңизден', u'киттериңиздерден', ]],
            u'козу': [
                [u'козумдан', u'козуңдан', u'козусунан', u'козубуздан', u'козуңардан', u'козусунан', u'козуңуздан', u'козуңуздардан', ],
                [u'козуларымдан', u'козуларыңдан', u'козуларынан', u'козуларыбыздан', u'козуларыңардан', u'козуларынан', u'козуларыңыздан', u'козуларыңыздардан', ]],
            u'тор': [
                [u'торумдан', u'торуңдан', u'торунан', u'торубуздан', u'торуңардан', u'торунан', u'торуңуздан', u'торуңуздардан', ],
                [u'торлорумдан', u'торлоруңдан', u'торлорунан', u'торлорубуздан', u'торлоруңардан', u'торлорунан', u'торлоруңуздан', u'торлоруңуздардан', ]],
            u'бөлө': [
                [u'бөлөмдөн', u'бөлөңдөн', u'бөлөсүнөн', u'бөлөбүздөн', u'бөлөңөрдөн', u'бөлөсүнөн', u'бөлөңүздөн', u'бөлөңүздөрдөн', ],
                [u'бөлөлөрүмдөн', u'бөлөлөрүңдөн', u'бөлөлөрүнөн', u'бөлөлөрүбүздөн', u'бөлөлөрүңөрдөн', u'бөлөлөрүнөн', u'бөлөлөрүңүздөн', u'бөлөлөрүңүздөрдөн', ]]
        }
