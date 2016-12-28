# coding=utf-8
from kg_lang.kyrgyz.helps.attrs import *
from kg_lang.kyrgyz.jondomo import Jondomo
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.kyrgyz.san import San
from kg_lang.kyrgyz.taandyk import Taandyk
from kg_lang.tests import KGTestCase


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
                self.assertEqual(unicode(jondomo.barysh()), jeke_form_expected)

                koptuk_form_expected = expected_forms[1][i]
                taandyk_koptuk = Taandyk(koptuk).make(attr.jak, attr.jeke, attr.sylyk)
                jondomo_koptuk = Jondomo(taandyk_koptuk)
                self.assertEqual(unicode(jondomo_koptuk.barysh()), koptuk_form_expected)

    def get_data(self):
        return {
            u'кит': [
                [u'китиме', u'китиңе', u'китине', u'китибизге', u'китиңерге', u'китине', u'китиңизге', u'китиңиздерге'],
                [u'киттериме', u'киттериңе', u'киттерине', u'киттерибизге', u'киттериңерге', u'киттерине', u'киттериңизге', u'киттериңиздерге']],
            u'казы': [
                [u'казыма', u'казыңа', u'казысына', u'казыбызга', u'казыңарга', u'казысына', u'казыңызга', u'казыңыздарга'],
                [u'казыларыма', u'казыларыңа', u'казыларына', u'казыларыбызга', u'казыларыңарга', u'казыларына', u'казыларыңызга', u'казыларыңыздарга']],
            u'тор': [
                [u'торума', u'торуңа', u'торуна', u'торубузга', u'торуңарга', u'торуна', u'торуңузга', u'торуңуздарга'],
                [u'торлорума', u'торлоруңа', u'торлоруна', u'торлорубузга', u'торлоруңарга', u'торлоруна', u'торлоруңузга', u'торлоруңуздарга']],
            u'бөлө': [
                [u'бөлөмө', u'бөлөңө', u'бөлөсүнө', u'бөлөбүзгө', u'бөлөңөргө', u'бөлөсүнө', u'бөлөңүзгө', u'бөлөңүздөргө'],
                [u'бөлөлөрүмө', u'бөлөлөрүңө', u'бөлөлөрүнө', u'бөлөлөрүбүзгө', u'бөлөлөрүңөргө', u'бөлөлөрүнө', u'бөлөлөрүңүзгө', u'бөлөлөрүңүздөргө']]
        }
