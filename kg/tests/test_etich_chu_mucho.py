# coding=utf-8
from kg.lang.etish._ba import BaEtishMuchosu
from kg.lang.etish._chu import ChuEtishMuchosu
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class EtishChuMuchoTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            affix = ChuEtishMuchosu(KyrgyzWord(word, False))
            self.assertEqual(affix.make(), expected_form)

    def get_data(self):
        return {
            u'кийин': u'кийинчү',
            u'күчүктө': u'күчүктөчү',
            u'күчүркө': u'күчүркөчү',
            u'жаңыла': u'жаңылачу',
            u'чыңа': u'чыңачу',
            u'кержей': u'кержейчү',
            u'түнө': u'түнөчү',
            u'чөбүрө': u'чөбүрөчү',
            u'кон': u'кончу',
            u'тезде': u'тездечү',
            u'чуба': u'чубачу',
            u'тат': u'татчу',
            u'парала': u'паралачу',
            u'жаркы': u'жаркычу',
            u'кур': u'курчу',
            u'таятала': u'таяталачу',
            u'божомолдо': u'божомолдочу',
            u'чүйрү': u'чүйрүчү',
            u'үз': u'үзчү',
            u'курсак ач': u'курсак аччу',
            u'бүр': u'бүрчү',
            u'жалоору': u'жалооручу',
            u'жакшыр': u'жакшырчу',
            u'баш бак': u'баш бакчу',
            u'жалакайлан': u'жалакайланчу',
            u'кезектеш': u'кезектешчү',
            u'химиялаштыр': u'химиялаштырчу',
            u'кууру': u'кууручу',
            u'самтыра': u'самтырачу',
            u'күт': u'күтчү',
            u'тетирилен': u'тетириленчү',
            u'чөктүр': u'чөктүрчү',
            u'атан': u'атанчу',
            u'бырылда': u'бырылдачу',
            u'түптө': u'түптөчү',
            u'көктө': u'көктөчү',
            u'түр': u'түрчү',
            u'зыңкый': u'зыңкыйчу',
            u'чиймеле': u'чиймелечү',
            u'такшал': u'такшалчу',
            u'жумшакта': u'жумшактачу',
            u'тыпыра': u'тыпырачу',
            u'көңүлдөн': u'көңүлдөнчү',
            u'чатакташ': u'чатакташчу',
            u'ыңгайлаш': u'ыңгайлашчу',
            u'жылжы': u'жылжычу',
            u'күрсүлдө': u'күрсүлдөчү',
            u'төмпөй': u'төмпөйчү',
            u'сойло': u'сойлочу',
        }
