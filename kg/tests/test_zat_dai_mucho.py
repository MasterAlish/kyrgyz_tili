# coding=utf-8
from kg.lang.lang import KyrgyzWord
from kg.lang.syn._dai import DaiZatMuchosu
from kg.tests import KGTestCase


class ZatDaiMuchoTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            affix = DaiZatMuchosu(KyrgyzWord(word))
            self.assertEqual(affix.make(), expected_form)

    def get_data(self):
        return {
            u'көзөмөлдүк': u'көзөмөлдүктөй',
            u'пианино': u'пианинодой',
            u'героин': u'героиндей',
            u'дулдул': u'дулдулдай',
            u'чил': u'чилдей',
            u'пицца': u'пиццадай',
            u'каңгыр-куңгур': u'каңгыр-куңгурдай',
            u'предмет': u'предметтей',
            u'айбанат': u'айбанаттай',
            u'катыш': u'катыштай',
            u'терек': u'теректей',
            u'запчасть': u'запчасттай',
            u'маселе': u'маселедей',
            u'үп': u'үптөй',
            u'жасоол': u'жасоолдой',
            u'кек': u'кектей',
            u'нускоочу': u'нускоочудай',
            u'баёолук': u'баёолуктай',
            u'кара курт': u'кара курттай',
            u'оорукана': u'ооруканадай',
            u'информатика': u'информатикадай',
            u'сай': u'сайдай',
            u'жож': u'жождой',
            u'лөлү': u'лөлүдөй',
            u'айыл-апа': u'айыл-ападай',
            u'гүлгүн': u'гүлгүндөй',
            u'матрос': u'матростой',
            u'табуучу': u'табуучудай',
            u'маалымдама': u'маалымдамадай',
            u'зыяпат': u'зыяпаттай',
            u'сыйкырчы': u'сыйкырчыдай',
            u'диктор': u'диктордой',
            u'диктофон': u'диктофондой',
            u'каңырык': u'каңырыктай',
            u'пордукция': u'пордукциядай',
            u'асылзаада': u'асылзаададай',
            u'айгай': u'айгайдай',
            u'каркыра': u'каркырадай',
            u'шейит': u'шейиттей',
            u'жер-жебер': u'жер-жебердей',
            u'барабан': u'барабандай',
            u'аксанатай': u'аксанатайдай',
            u'гамма': u'гаммадай',
            u'дарс': u'дарстай',
            u'арена': u'аренадай',
            u'барча': u'барчадай',
            u'жетекчи': u'жетекчидей',
            u'тулуп': u'тулуптай',
            u'жаңжал': u'жаңжалдай',
            u'тапанча': u'тапанчадай',
        }
