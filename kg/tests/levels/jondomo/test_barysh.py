from kg.lang.helps.attrs import *
from kg.lang.jondomo import Jondomo
from kg.lang.lang import KyrgyzWord
from kg.lang.san import San
from kg.lang.taandyk import Taandyk
from kg.tests import KGTestCase


attrs_list = [men, sen, al, biz, siler, alar, siz, sizder]


class JondomoBaryshAfterTaandykTest(KGTestCase):
    def test_barysh_after_taandyk(self):
        data = self.get_data()
        for word, expected_forms in data.items():
            koptuk = San(KyrgyzWord(word)).koptuk()
            for i in range(len(attrs_list)):
                attr = attrs_list[i]
                jeke_form_expected = expected_forms[0][i]
                taandyk = Taandyk(KyrgyzWord(word)).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo = Jondomo(taandyk)
                self.assertEqual(jondomo.barysh(), jeke_form_expected)

                koptuk_form_expected = expected_forms[1][i]
                taandyk_koptuk = Taandyk(koptuk).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo_koptuk = Jondomo(taandyk_koptuk)
                self.assertEqual(jondomo_koptuk.barysh(), koptuk_form_expected)

    def get_data(self):
        return {
            'кит': [
                ['китиме', 'китиңе', 'китине', 'китибизге', 'китиңерге', 'китине', 'китиңизге', 'китиңиздерге'],
                ['киттериме', 'киттериңе', 'киттерине', 'киттерибизге', 'киттериңерге', 'киттерине', 'киттериңизге', 'киттериңиздерге']],
            'казы': [
                ['казыма', 'казыңа', 'казысына', 'казыбызга', 'казыңарга', 'казысына', 'казыңызга', 'казыңыздарга'],
                ['казыларыма', 'казыларыңа', 'казыларына', 'казыларыбызга', 'казыларыңарга', 'казыларына', 'казыларыңызга', 'казыларыңыздарга']],
            'тор': [
                ['торума', 'торуңа', 'торуна', 'торубузга', 'торуңарга', 'торуна', 'торуңузга', 'торуңуздарга'],
                ['торлорума', 'торлоруңа', 'торлоруна', 'торлорубузга', 'торлоруңарга', 'торлоруна', 'торлоруңузга', 'торлоруңуздарга']],
            'бөлө': [
                ['бөлөмө', 'бөлөңө', 'бөлөсүнө', 'бөлөбүзгө', 'бөлөңөргө', 'бөлөсүнө', 'бөлөңүзгө', 'бөлөңүздөргө'],
                ['бөлөлөрүмө', 'бөлөлөрүңө', 'бөлөлөрүнө', 'бөлөлөрүбүзгө', 'бөлөлөрүңөргө', 'бөлөлөрүнө', 'бөлөлөрүңүзгө', 'бөлөлөрүңүздөргө']]
        }
