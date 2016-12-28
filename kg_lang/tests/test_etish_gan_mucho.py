# coding=utf-8
from kg_lang.kyrgyz.etish._gan import GanEtishMuchosu
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.tests import KGTestCase


class EtishGanMuchoTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, form in data.items():
            atooch = GanEtishMuchosu(KyrgyzWord(word, False))
            self.assertEqual(atooch.make().word, form)

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
