# coding=utf-8
from kg_lang.kyrgyz.etish._bash import BashEtishMuchosu
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.tests import KGTestCase


class EtishBashMuchoTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            affix = BashEtishMuchosu(KyrgyzWord(word))
            self.assertEqual(affix.make(), expected_form)

    def get_data(self):
        return {
            u'сүйүн': u'сүйүнбөш',
            u'өлчө': u'өлчөбөш',
            u'куйтулан': u'куйтуланбаш',
            u'легалдаш': u'легалдашпаш',
            u'ызырын': u'ызырынбаш',
            u'утул': u'утулбаш',
            u'колтукташ': u'колтукташпаш',
            u'жылаңаякта': u'жылаңаяктабаш',
            u'магдыра': u'магдырабаш',
            u'жылбыш': u'жылбышпаш',
            u'тартыш': u'тартышпаш',
            u'ылдамда': u'ылдамдабаш',
            u'чымыра': u'чымырабаш',
            u'суу': u'суубаш',
            u'кур': u'курбаш',
            u'ичир': u'ичирбеш',
            u'кир': u'кирбеш',
            u'жайыл': u'жайылбаш',
            u'үксүй': u'үксүйбөш',
            u'ныкта': u'ныктабаш',
            u'ыргышта': u'ыргыштабаш',
            u'сабырка': u'сабыркабаш',
            u'үлгүр': u'үлгүрбөш',
            u'ысыла': u'ысылабаш',
            u'жакындаш': u'жакындашпаш',
            u'ышта': u'ыштабаш',
            u'бажыра': u'бажырабаш',
            u'кутул': u'кутулбаш',
            u'кымырын': u'кымырынбаш',
            u'кынжый': u'кынжыйбаш',
            u'түрлөн': u'түрлөнбөш',
            u'тайгалан': u'тайгаланбаш',
            u'зөөкүрлөн': u'зөөкүрлөнбөш',
            u'кылтый': u'кылтыйбаш',
            u'тыкылда': u'тыкылдабаш',
            u'коомайсыздан': u'коомайсызданбаш',
            u'кийри': u'кийрибеш',
            u'такшал': u'такшалбаш',
            u'көңүлдөн': u'көңүлдөнбөш',
            u'шиле': u'шилебеш',
            u'карттан': u'карттанбаш',
            u'ийик': u'ийикпеш',
            u'ийинде': u'ийиндебеш',
            u'мөңкү': u'мөңкүбөш',
            u'талык': u'талыкпаш',
            u'өркүндө': u'өркүндөбөш',
            u'жойло': u'жойлобош',
            u'пулда': u'пулдабаш',
            u'жет': u'жетпеш',
            u'баш катыр': u'баш катырбаш',
        }
