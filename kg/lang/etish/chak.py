from kg.lang.affix import Affix
from kg.lang.helps.attrs import WordAttrs
from kg.lang.lang import select_for_attrs
from kg.lang.mucho import J, P, SpecialMucho


class Chak(Affix):
    def __init__(self, word_object):
        self.word_object = word_object
        self.word_object.prepare()

    def is_pluralable(self):
        return True

    def make(self, jak=1, jeke=True, sylyk=False):
        return self.word_object.word

    def change_yottoshkon_tamga(self, end_of_result, start_of_result):
        if start_of_result[-1] == 'й' and end_of_result[0] == 'е':
            return start_of_result[:-1], end_of_result
        elif start_of_result[-1] == 'й' and end_of_result[0] == 'а':
            return start_of_result[:-1] + 'я', end_of_result[1:]
        elif start_of_result[-1] == 'й' and end_of_result[0] == 'о':
            return start_of_result[:-1] + 'ё', end_of_result[1:]
        elif start_of_result[-1] == 'й' and end_of_result[0] == 'у':
            return start_of_result[:-1] + 'ю', end_of_result[1:]
        return start_of_result, end_of_result


class OtkonChak(Chak):

    men = [
        ["дым", "дум", "дим", "дүм"],
        ["дым", "дум", "дим", "дүм"],
        ["дым", "дум", "дим", "дүм"],
        ["тым", "тум", "тим", "түм"]
    ]

    biz = [
        ["дык", "дук", "дик", "дүк"],
        ["дык", "дук", "дик", "дүк"],
        ["дык", "дук", "дик", "дүк"],
        ["тык", "тук", "тик", "түк"]
    ]

    sen = [
        ["дың", "дуң", "диң", "дүң"],
        ["дың", "дуң", "диң", "дүv"],
        ["дың", "дуң", "диң", "дүң"],
        ["тың", "туң", "тиң", "түң"]
    ]

    siler = [
        ["дыңар", "дуңар", "диңер", "дүңөр"],
        ["дыңар", "дуңар", "диңер", "дүңөр"],
        ["дыңар", "дуңар", "диңер", "дүңөр"],
        ["тыңар", "туңар", "тиңер", "түңөр"],
    ]

    siz = [
        ["дыңыз", "дуңуз", "диңиз", "дүңүз"],
        ["дыңыз", "дуңуз", "диңиз", "дүңүз"],
        ["дыңыз", "дуңуз", "диңиз", "дүңүз"],
        ["тыңыз", "туңуз", "тиңиз", "түңүз"],
    ]

    sizder = [
        ["дыңыздар", "дуңуздар", "диңиздер", "дүңүздөр"],
        ["дыңыздар", "дуңуздар", "диңиздер", "дүңүздөр"],
        ["дыңыздар", "дуңуздар", "диңиздер", "дүңүздөр"],
        ["тыңыздар", "туңуздар", "тиңиздер", "түңүздөр"],
    ]

    al = [
        ["ды", "ду", "ди", "дү"],
        ["ды", "ду", "ди", "дү"],
        ["ды", "ду", "ди", "дү"],
        ["ты", "ту", "ти", "тү"]
    ]

    alar = [
        ["шты", "шту", "шти", "штү"],
        [J("ышты"), J("ушту"), J("ишти"), J("үштү")],
        [J("ышты"), J("ушту"), J("ишти"), J("үштү")],
        [J("ышты"), J("ушту"), J("ишти"), J("үштү")],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucholor = select_for_attrs(jak, jeke, sylyk, self.men, self.sen, self.al, self.biz, self.siler, self.alar,
                                        self.siz, self.sizder)
            mucho = mucholor[index_i][index_j]
            start_of_result = self.word_object.word + ""
            end_of_result = mucho
            if isinstance(end_of_result, SpecialMucho):
                start_of_result, end_of_result = end_of_result.make(self.word_object.word)
            start_of_result, end_of_result = self.change_yottoshkon_tamga(end_of_result, start_of_result)
            return self.word_object.change(start_of_result, end_of_result, "otkon_chak", WordAttrs(jak, jeke, sylyk))
        return self.word_object


class UchurChak(Chak):

    def is_pluralable(self):
        return False

    def transformers(self):
        return [UchurChak.uchur_base_form]

    mucholor = [
        ["п", "п", "п", "п"],
        [P(J("ып")), P(J("уп")), P(J("ип")), P(J("үп"))],
        [P(J("ып")), P(J("уп")), P(J("ип")), P(J("үп"))],
        [P(J("ып")), P(J("уп")), P(J("ип")), P(J("үп"))],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            jatuu = select_for_attrs(jak, jeke, sylyk, "жатам", "жатасың", "жатат", "жатабыз", "жатасыңар",
                                     "жатышат", "жатасыз", "жатасыздар")
            new_form = self.uchur_base_form(WordAttrs(jak, jeke, sylyk))
            new_form.word += " " + jatuu
            return new_form
        return self.word_object

    def uchur_base_form(self, word_attrs=None):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[index_i][index_j]
            start_of_result = self.word_object.word + ""
            end_of_result = mucho
            if isinstance(end_of_result, SpecialMucho):
                start_of_result, end_of_result = end_of_result.make(self.word_object.word)
            start_of_result, end_of_result = self.change_yottoshkon_tamga(end_of_result, start_of_result)
            return self.word_object.change(start_of_result, end_of_result, "uchur_chak", word_attrs)
        return self.word_object


class KelerChak(Chak):

    men = [
        ["йм", "йм", "йм", "йм"],
        [J("ам"), J(("ом", "ам")), J("ем"), J("өм")],
        [J("ам"), J(("ом", "ам")), J("ем"), J("өм")],
        [J("ам"), J(("ом", "ам")), J("ем"), J("өм")],
    ]

    biz = [
        ["йбыз", "йбуз", "йбиз", "йбүз"],
        [J("абыз"), J(("обуз", "абыз")), J("ебиз"), J("өбүз")],
        [J("абыз"), J(("обуз", "абыз")), J("ебиз"), J("өбүз")],
        [J("абыз"), J(("обуз", "абыз")), J("ебиз"), J("өбүз")],
    ]

    sen = [
        ["йсың", "йсуң", "йсиң", "йсүң"],
        [J("асың"), J(("осуң", "асың")), J("есиң"), J("өсүң")],
        [J("асың"), J(("осуң", "асың")), J("есиң"), J("өсүң")],
        [J("асың"), J(("осуң", "асың")), J("есиң"), J("өсүң")],
    ]

    siler = [
        ["йсыңар", "йсуңар", "йсиңер", "йсүңөр"],
        [J("асыңар"), J(("осуңар", "асыңар")), J("есиңер"), J("өсүңөр")],
        [J("асыңар"), J(("осуңар", "асыңар")), J("есиңер"), J("өсүңөр")],
        [J("асыңар"), J(("осуңар", "асыңар")), J("есиңер"), J("өсүңөр")],
    ]

    siz = [
        ["йсыз", "йсуз", "йсиз", "йсүз"],
        [J("асыз"), J(("осуз", "асыз")), J("есиз"), J("өсүз")],
        [J("асыз"), J(("осуз", "асыз")), J("есиз"), J("өсүз")],
        [J("асыз"), J(("осуз", "асыз")), J("есиз"), J("өсүз")],
    ]

    sizder = [
        ["йсыздар", "йсуздар", "йсиздер", "йсүздөр"],
        [J("асыздар"), J(("осуздар", "асыздар")), J("есиздер"), J("өсүздөр")],
        [J("асыздар"), J(("осуздар", "асыздар")), J("есиздер"), J("өсүздөр")],
        [J("асыздар"), J(("осуздар", "асыздар")), J("есиздер"), J("өсүздөр")],
    ]

    al = [
        ["йт", "йт", "йт", "йт"],
        [J("ат"), J(("от", "ат")), J("ет"), J("өт")],
        [J("ат"), J(("от", "ат")), J("ет"), J("өт")],
        [J("ат"), J(("от", "ат")), J("ет"), J("өт")],
    ]

    alar = [
        ["шат", ("шот", "шат"), "шет", "шөт"],
        [J("ышат"), J("ушат"), J("ишет"), J("үшөт")],
        [J("ышат"), J("ушат"), J("ишет"), J("үшөт")],
        [J("ышат"), J("ушат"), J("ишет"), J("үшөт")],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucholor = select_for_attrs(jak, jeke, sylyk, self.men, self.sen, self.al, self.biz, self.siler, self.alar,
                                        self.siz, self.sizder)

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
            start_of_result, end_of_result = self.change_yottoshkon_tamga(end_of_result, start_of_result)
            return self.word_object.change(start_of_result, end_of_result, "keler_chak", WordAttrs(jak, jeke, sylyk))
        return self.word_object
