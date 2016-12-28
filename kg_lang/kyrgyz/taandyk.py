# coding=utf-8
from kg_lang.kyrgyz.affix import Affix
from kg_lang.kyrgyz.helps.attrs import WordAttrs
from kg_lang.kyrgyz.lang import WordEndingTypes
from kg_lang.kyrgyz.mucho import *


class Taandyk(Affix):
    def __init__(self, word_object):
        """:type word_object: kg_lang.kyrgyz.lang.KyrgyzWord """
        self.word_object = word_object
        self.word_object.prepare()

    def is_pluralable(self):
        return True

    taandyk_jeke_1_jak_mucho = [
        [u"м", u"м", u"м", u"м"],
        [J(u"ым"), J(u"ум"), J(u"им"), J(u"үм")],
        [J(u"ым"), J(u"ум"), J(u"им"), J(u"үм")],
        [J(u"ым"), J(u"ум"), J(u"им"), J(u"үм")],
    ]

    taandyk_kop_1_jak_mucho = [
        [u"быз", u"буз", u"биз", u"бүз"],
        [J(u"ыбыз"), J(u"убуз"), J(u"ибиз"), J(u"үбүз")],
        [J(u"ыбыз"), J(u"убуз"), J(u"ибиз"), J(u"үбүз")],
        [J(u"ыбыз"), J(u"убуз"), J(u"ибиз"), J(u"үбүз")],
    ]

    taandyk_jeke_2_jak_mucho = [
        [u"ң", u"ң", u"ң", u"ң"],
        [J(u"ың"), J(u"уң"), J(u"иң"), J(u"үң")],
        [J(u"ың"), J(u"уң"), J(u"иң"), J(u"үң")],
        [J(u"ың"), J(u"уң"), J(u"иң"), J(u"үң")],
    ]

    taandyk_kop_2_jak_mucho = [
        [u"ңар", (u"ңор", u"ңар"), u"ңер", u"ңөр"],
        [J(u"ыңар"), J(u"уңар"), J(u"иңер"), J(u"үңөр")],
        [J(u"ыңар"), J(u"уңар"), J(u"иңер"), J(u"үңөр")],
        [J(u"ыңар"), J(u"уңар"), J(u"иңер"), J(u"үңөр")],
    ]

    taandyk_jeke_2_jak_sylyk_mucho = [
        [u"ңыз", u"ңуз", u"ңиз", u"ңүз"],
        [J(u"ыңыз"), J(u"уңуз"), J(u"иңиз"), J(u"үңүз")],
        [J(u"ыңыз"), J(u"уңуз"), J(u"иңиз"), J(u"үңүз")],
        [J(u"ыңыз"), J(u"уңуз"), J(u"иңиз"), J(u"үңүз")],
    ]

    taandyk_kop_2_jak_sylyk_mucho = [
        [u"ңыздар", u"ңуздар", u"ңиздер", u"ңүздөр"],
        [J(u"ыңыздар"), J(u"уңуздар"), J(u"иңиздер"), J(u"үңүздөр")],
        [J(u"ыңыздар"), J(u"уңуздар"), J(u"иңиздер"), J(u"үңүздөр")],
        [J(u"ыңыздар"), J(u"уңуздар"), J(u"иңиздер"), J(u"үңүздөр")],
    ]

    taandyk_jeke_3_jak_mucho = [
        [u"сы", u"су", u"си", u"сү"],
        [J(u"ы"), J(u"у"), J(u"и"), J(u"ү")],
        [J(u"ы"), J(u"у"), J(u"и"), J(u"ү")],
        [J(u"ы"), J(u"у"), J(u"и"), J(u"ү")],
    ]

    taandyk_kop_3_jak_mucho = [
        [u"сы", u"су", u"си", u"сү"],
        [J(u"ы"), J(u"у"), J(u"и"), J(u"ү")],
        [J(u"ы"), J(u"у"), J(u"и"), J(u"ү")],
        [J(u"ы"), J(u"у"), J(u"и"), J(u"ү")],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            if jak == 1:
                mucholor = self.taandyk_jeke_1_jak_mucho if jeke else self.taandyk_kop_1_jak_mucho
            elif jak == 2:
                if sylyk:
                    mucholor = self.taandyk_jeke_2_jak_sylyk_mucho if jeke else self.taandyk_kop_2_jak_sylyk_mucho
                else:
                    mucholor = self.taandyk_jeke_2_jak_mucho if jeke else self.taandyk_kop_2_jak_mucho
            else:
                mucholor = self.taandyk_jeke_3_jak_mucho if jeke else self.taandyk_kop_3_jak_mucho

            mucho = mucholor[index_i][index_j]
            start_of_result = self.word_object.word + u""
            end_of_result = mucho
            if isinstance(end_of_result, SpecialMucho):
                start_of_result, end_of_result = end_of_result.make(self.word_object.word)
            if isinstance(end_of_result, tuple):
                if self.word_object.unduu_type_jaaktuu:
                    end_of_result = end_of_result[0]
                else:
                    end_of_result = end_of_result[1]
            return self.word_object.change(start_of_result, end_of_result, "taandyk", WordAttrs(jak, jeke, sylyk))

        return self.word_object
