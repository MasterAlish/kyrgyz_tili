# coding=utf-8
from kg.lang.etish._gan import GanEtishMuchosu
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class EtishGanMuchoTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            affix = GanEtishMuchosu(KyrgyzWord(word))
            self.assertEqual(affix.make().word, expected_form)

    def get_data(self):
        return {
            u'таңдан': u'таңданган',
            u'сонурка': u'сонуркаган',
            u'тап бер': u'тап берген',
            u'тара': u'тараган',
            u'тиште': u'тиштеген',
            u'карга': u'каргаган',
            u'уруш': u'урушкан',
            u'конокто': u'коноктогон',
            u'кандыр': u'кандырган',
            u'аныкта': u'аныктаган',
            u'жоопко ал': u'жоопко алган',
            u'эңил': u'эңилген',
            u'чачыра': u'чачыраган',
            u'арыкта': u'арыктаган',
            u'кой': u'койгон',
            u'кылтыйт': u'кылтыйткан',
            u'окшоңдо': u'окшоңдогон',
            u'үшү': u'үшүгөн',
            u'барсай': u'барсайган',
            u'былчый': u'былчыйган',
            u'дуулда': u'дуулдаган',
            u'алмаштыр': u'алмаштырган',
            u'бышкыр': u'бышкырган',
            u'кырчын': u'кырчынган',
            u'дүрдүк': u'дүрдүккөн',
            u'жепирей': u'жепирейген',
            u'кайында': u'кайындаган',
            u'касам ич': u'касам ичкен',
            u'ашык': u'ашыккан',
            u'жүлжүй': u'жүлжүйгөн',
        }
