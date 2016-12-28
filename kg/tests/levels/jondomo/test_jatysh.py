# coding=utf-8
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
            u'кит': [
                [u'китимде', u'китиңде', u'китинде', u'китибизде', u'китиңерде', u'китинде', u'китиңизде', u'китиңиздерде', ],
                [u'киттеримде', u'киттериңде', u'киттеринде', u'киттерибизде', u'киттериңерде', u'киттеринде', u'киттериңизде', u'киттериңиздерде', ]],
            u'козу': [
                [u'козумда', u'козуңда', u'козусунда', u'козубузда', u'козуңарда', u'козусунда', u'козуңузда', u'козуңуздарда', ],
                [u'козуларымда', u'козуларыңда', u'козуларында', u'козуларыбызда', u'козуларыңарда', u'козуларында', u'козуларыңызда', u'козуларыңыздарда', ]],
            u'тор': [
                [u'торумда', u'торуңда', u'торунда', u'торубузда', u'торуңарда', u'торунда', u'торуңузда', u'торуңуздарда', ],
                [u'торлорумда', u'торлоруңда', u'торлорунда', u'торлорубузда', u'торлоруңарда', u'торлорунда', u'торлоруңузда', u'торлоруңуздарда', ]],
            u'бөлө': [
                [u'бөлөмдө', u'бөлөңдө', u'бөлөсүндө', u'бөлөбүздө', u'бөлөңөрдө', u'бөлөсүндө', u'бөлөңүздө', u'бөлөңүздөрдө', ],
                [u'бөлөлөрүмдө', u'бөлөлөрүңдө', u'бөлөлөрүндө', u'бөлөлөрүбүздө', u'бөлөлөрүңөрдө', u'бөлөлөрүндө', u'бөлөлөрүңүздө', u'бөлөлөрүңүздөрдө', ]]
        }
