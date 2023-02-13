from kg.lang.affix import Affix
from kg.lang.helps.attrs import WordAttrs
from kg.lang.lang import WordEndingTypes
from kg.lang.mucho import *


class Taandyk(Affix):
    def __init__(self, word_object):
        """:type word_object: kg_lang.kyrgyz.lang.KyrgyzWord """
        self.word_object = word_object
        self.word_object.prepare()

    def is_pluralable(self):
        return True

    taandyk_jeke_1_jak_mucho = [
        ["м", "м", "м", "м"],
        [J("ым"), J("ум"), J("им"), J("үм")],
        [J("ым"), J("ум"), J("им"), J("үм")],
        [J("ым"), J("ум"), J("им"), J("үм")],
    ]

    taandyk_kop_1_jak_mucho = [
        ["быз", "буз", "биз", "бүз"],
        [J("ыбыз"), J("убуз"), J("ибиз"), J("үбүз")],
        [J("ыбыз"), J("убуз"), J("ибиз"), J("үбүз")],
        [J("ыбыз"), J("убуз"), J("ибиз"), J("үбүз")],
    ]

    taandyk_jeke_2_jak_mucho = [
        ["ң", "ң", "ң", "ң"],
        [J("ың"), J("уң"), J("иң"), J("үң")],
        [J("ың"), J("уң"), J("иң"), J("үң")],
        [J("ың"), J("уң"), J("иң"), J("үң")],
    ]

    taandyk_kop_2_jak_mucho = [
        ["ңар", ("ңор", "ңар"), "ңер", "ңөр"],
        [J("ыңар"), J("уңар"), J("иңер"), J("үңөр")],
        [J("ыңар"), J("уңар"), J("иңер"), J("үңөр")],
        [J("ыңар"), J("уңар"), J("иңер"), J("үңөр")],
    ]

    taandyk_jeke_2_jak_sylyk_mucho = [
        ["ңыз", "ңуз", "ңиз", "ңүз"],
        [J("ыңыз"), J("уңуз"), J("иңиз"), J("үңүз")],
        [J("ыңыз"), J("уңуз"), J("иңиз"), J("үңүз")],
        [J("ыңыз"), J("уңуз"), J("иңиз"), J("үңүз")],
    ]

    taandyk_kop_2_jak_sylyk_mucho = [
        ["ңыздар", "ңуздар", "ңиздер", "ңүздөр"],
        [J("ыңыздар"), J("уңуздар"), J("иңиздер"), J("үңүздөр")],
        [J("ыңыздар"), J("уңуздар"), J("иңиздер"), J("үңүздөр")],
        [J("ыңыздар"), J("уңуздар"), J("иңиздер"), J("үңүздөр")],
    ]

    taandyk_jeke_3_jak_mucho = [
        ["сы", "су", "си", "сү"],
        [J("ы"), J("у"), J("и"), J("ү")],
        [J("ы"), J("у"), J("и"), J("ү")],
        [J("ы"), J("у"), J("и"), J("ү")],
    ]

    taandyk_kop_3_jak_mucho = [
        ["сы", "су", "си", "сү"],
        [J("ы"), J("у"), J("и"), J("ү")],
        [J("ы"), J("у"), J("и"), J("ү")],
        [J("ы"), J("у"), J("и"), J("ү")],
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
            start_of_result = self.word_object.word + ""
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
