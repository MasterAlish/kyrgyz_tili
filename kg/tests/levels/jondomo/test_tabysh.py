# coding=utf-8
from kg.lang.helps.attrs import *
from kg.lang.jondomo import Jondomo
from kg.lang.lang import KyrgyzWord
from kg.lang.san import San
from kg.lang.taandyk import Taandyk
from kg.tests import KGTestCase


attrs_list = [men, sen, al, biz, siler, alar, siz, sizder]


class JondomoTabyshAfterTaandykTest(KGTestCase):
    def test_tabysh_after_taandyk(self):
        data = self.get_data()
        for word, expected_forms in data.items():
            koptuk = San(KyrgyzWord(word)).koptuk()
            for i in range(len(attrs_list)):
                attr = attrs_list[i]
                jeke_form_expected = expected_forms[0][i]
                taandyk = Taandyk(KyrgyzWord(word)).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo = Jondomo(taandyk)
                self.assertEqual(jondomo.tabysh(), jeke_form_expected)

                koptuk_form_expected = expected_forms[1][i]
                taandyk_koptuk = Taandyk(koptuk).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo_koptuk = Jondomo(taandyk_koptuk)
                self.assertEqual(jondomo_koptuk.tabysh(), koptuk_form_expected)

    def get_data(self):
        return {
            u'кит': [
                [u'китимди', u'китиңди', u'китин', u'китибизди', u'китиңерди', u'китин', u'китиңизди', u'китиңиздерди', ],
                [u'киттеримди', u'киттериңди', u'киттерин', u'киттерибизди', u'киттериңерди', u'киттерин', u'киттериңизди', u'киттериңиздерди', ]],
            u'козу': [
                [u'козумду', u'козуңду', u'козусун', u'козубузду', u'козуңарды', u'козусун', u'козуңузду', u'козуңуздарды', ],
                [u'козуларымды', u'козуларыңды', u'козуларын', u'козуларыбызды', u'козуларыңарды', u'козуларын', u'козуларыңызды', u'козуларыңыздарды', ]],
            u'тор': [
                [u'торумду', u'торуңду', u'торун', u'торубузду', u'торуңарды', u'торун', u'торуңузду', u'торуңуздарды', ],
                [u'торлорумду', u'торлоруңду', u'торлорун', u'торлорубузду', u'торлоруңарды', u'торлорун', u'торлоруңузду', u'торлоруңуздарды', ]],
            u'бөлө': [
                [u'бөлөмдү', u'бөлөңдү', u'бөлөсүн', u'бөлөбүздү', u'бөлөңөрдү', u'бөлөсүн', u'бөлөңүздү', u'бөлөңүздөрдү'],
                [u'бөлөлөрүмдү', u'бөлөлөрүңдү', u'бөлөлөрүн', u'бөлөлөрүбүздү', u'бөлөлөрүңөрдү', u'бөлөлөрүн', u'бөлөлөрүңүздү', u'бөлөлөрүңүздөрдү']]
        }
