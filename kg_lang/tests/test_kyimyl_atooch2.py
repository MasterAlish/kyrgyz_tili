# coding=utf-8
from kg_lang.kyrgyz.chak import UchurChak
from kg_lang.kyrgyz.kyimyl_atooch import KyimylAtooch, KyimylAtooch2
from kg_lang.kyrgyz.lang import KyrgyzWord
from kg_lang.tests import KGTestCase


class KyimylAtooch2Test(KGTestCase):
    def test_1(self):

        data = self.get_data()

        for word, form in data.items():
            kyimyl_atooch2 = KyimylAtooch2(KyrgyzWord(word, False))
            self.assertEqual(kyimyl_atooch2.make(), form)

    def get_data(self):
        return {
            u'чий': u'чийиш',
            u'теп': u'тебиш',
            u'чой': u'чоюш',
            u'ал': u'алыш',
            u'буруй': u'буруюш',
            u'токто': u'токтош',
            u'каз': u'казыш',
            u'кий': u'кийиш',
            u'куй': u'куюш',
            u'бойтой': u'бойтоюш',
            u'кеңей': u'кеңейиш',
            u'сай': u'сайыш',
            u'бар': u'барыш',
            u'акшый': u'акшыйыш',
            u'тап': u'табыш',
            u'алай': u'алайыш',
            u'кара': u'караш',
            u'былчый': u'былчыйыш',
            u'ой': u'оюш',
            u'жаса': u'жасаш',
            u'күй': u'күйүш',
            u'ташы': u'ташыш',
            u'кыл': u'кылыш',
            u'төмпөй': u'төмпөйүш',
            u'ич': u'ичиш',
            u'ук': u'угуш',
            u'сүйө': u'сүйөш',
            u'боё': u'боёш',
            u'тая': u'таяш',
        }
