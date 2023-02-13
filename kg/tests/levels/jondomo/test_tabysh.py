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
            'кит': [
                ['китимди', 'китиңди', 'китин', 'китибизди', 'китиңерди', 'китин', 'китиңизди', 'китиңиздерди', ],
                ['киттеримди', 'киттериңди', 'киттерин', 'киттерибизди', 'киттериңерди', 'киттерин', 'киттериңизди', 'киттериңиздерди', ]],
            'козу': [
                ['козумду', 'козуңду', 'козусун', 'козубузду', 'козуңарды', 'козусун', 'козуңузду', 'козуңуздарды', ],
                ['козуларымды', 'козуларыңды', 'козуларын', 'козуларыбызды', 'козуларыңарды', 'козуларын', 'козуларыңызды', 'козуларыңыздарды', ]],
            'тор': [
                ['торумду', 'торуңду', 'торун', 'торубузду', 'торуңарды', 'торун', 'торуңузду', 'торуңуздарды', ],
                ['торлорумду', 'торлоруңду', 'торлорун', 'торлорубузду', 'торлоруңарды', 'торлорун', 'торлоруңузду', 'торлоруңуздарды', ]],
            'бөлө': [
                ['бөлөмдү', 'бөлөңдү', 'бөлөсүн', 'бөлөбүздү', 'бөлөңөрдү', 'бөлөсүн', 'бөлөңүздү', 'бөлөңүздөрдү'],
                ['бөлөлөрүмдү', 'бөлөлөрүңдү', 'бөлөлөрүн', 'бөлөлөрүбүздү', 'бөлөлөрүңөрдү', 'бөлөлөрүн', 'бөлөлөрүңүздү', 'бөлөлөрүңүздөрдү']]
        }
