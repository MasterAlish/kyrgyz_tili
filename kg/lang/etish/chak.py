# coding=utf-8
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
        if start_of_result[-1] == u'й' and end_of_result[0] == u'е':
            return start_of_result[:-1], end_of_result
        elif start_of_result[-1] == u'й' and end_of_result[0] == u'а':
            return start_of_result[:-1] + u'я', end_of_result[1:]
        elif start_of_result[-1] == u'й' and end_of_result[0] == u'о':
            return start_of_result[:-1] + u'ё', end_of_result[1:]
        elif start_of_result[-1] == u'й' and end_of_result[0] == u'у':
            return start_of_result[:-1] + u'ю', end_of_result[1:]
        return start_of_result, end_of_result


class OtkonChak(Chak):

    men = [
        [u"дым", u"дум", u"дим", u"дүм"],
        [u"дым", u"дум", u"дим", u"дүм"],
        [u"дым", u"дум", u"дим", u"дүм"],
        [u"тым", u"тум", u"тим", u"түм"]
    ]

    biz = [
        [u"дык", u"дук", u"дик", u"дүк"],
        [u"дык", u"дук", u"дик", u"дүк"],
        [u"дык", u"дук", u"дик", u"дүк"],
        [u"тык", u"тук", u"тик", u"түк"]
    ]

    sen = [
        [u"дың", u"дуң", u"диң", u"дүң"],
        [u"дың", u"дуң", u"диң", u"дүv"],
        [u"дың", u"дуң", u"диң", u"дүң"],
        [u"тың", u"туң", u"тиң", u"түң"]
    ]

    siler = [
        [u"дыңар", u"дуңар", u"диңер", u"дүңөр"],
        [u"дыңар", u"дуңар", u"диңер", u"дүңөр"],
        [u"дыңар", u"дуңар", u"диңер", u"дүңөр"],
        [u"тыңар", u"туңар", u"тиңер", u"түңөр"],
    ]

    siz = [
        [u"дыңыз", u"дуңуз", u"диңиз", u"дүңүз"],
        [u"дыңыз", u"дуңуз", u"диңиз", u"дүңүз"],
        [u"дыңыз", u"дуңуз", u"диңиз", u"дүңүз"],
        [u"тыңыз", u"туңуз", u"тиңиз", u"түңүз"],
    ]

    sizder = [
        [u"дыңыздар", u"дуңуздар", u"диңиздер", u"дүңүздөр"],
        [u"дыңыздар", u"дуңуздар", u"диңиздер", u"дүңүздөр"],
        [u"дыңыздар", u"дуңуздар", u"диңиздер", u"дүңүздөр"],
        [u"тыңыздар", u"туңуздар", u"тиңиздер", u"түңүздөр"],
    ]

    al = [
        [u"ды", u"ду", u"ди", u"дү"],
        [u"ды", u"ду", u"ди", u"дү"],
        [u"ды", u"ду", u"ди", u"дү"],
        [u"ты", u"ту", u"ти", u"тү"]
    ]

    alar = [
        [u"шты", u"шту", u"шти", u"штү"],
        [J(u"ышты"), J(u"ушту"), J(u"ишти"), J(u"үштү")],
        [J(u"ышты"), J(u"ушту"), J(u"ишти"), J(u"үштү")],
        [J(u"ышты"), J(u"ушту"), J(u"ишти"), J(u"үштү")],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucholor = select_for_attrs(jak, jeke, sylyk, self.men, self.sen, self.al, self.biz, self.siler, self.alar,
                                        self.siz, self.sizder)
            mucho = mucholor[index_i][index_j]
            start_of_result = self.word_object.word + u""
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
        [u"п", u"п", u"п", u"п"],
        [P(J(u"ып")), P(J(u"уп")), P(J(u"ип")), P(J(u"үп"))],
        [P(J(u"ып")), P(J(u"уп")), P(J(u"ип")), P(J(u"үп"))],
        [P(J(u"ып")), P(J(u"уп")), P(J(u"ип")), P(J(u"үп"))],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            jatuu = select_for_attrs(jak, jeke, sylyk, u"жатам", u"жатасың", u"жатат", u"жатабыз", u"жатасыңар",
                                     u"жатышат", u"жатасыз", u"жатасыздар")
            new_form = self.uchur_base_form(WordAttrs(jak, jeke, sylyk))
            new_form.word += u" " + jatuu
            return new_form
        return self.word_object

    def uchur_base_form(self, word_attrs=None):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[index_i][index_j]
            start_of_result = self.word_object.word + u""
            end_of_result = mucho
            if isinstance(end_of_result, SpecialMucho):
                start_of_result, end_of_result = end_of_result.make(self.word_object.word)
            start_of_result, end_of_result = self.change_yottoshkon_tamga(end_of_result, start_of_result)
            return self.word_object.change(start_of_result, end_of_result, "uchur_chak", word_attrs)
        return self.word_object


class KelerChak(Chak):

    men = [
        [u"йм", u"йм", u"йм", u"йм"],
        [J(u"ам"), J((u"ом", u"ам")), J(u"ем"), J(u"өм")],
        [J(u"ам"), J((u"ом", u"ам")), J(u"ем"), J(u"өм")],
        [J(u"ам"), J((u"ом", u"ам")), J(u"ем"), J(u"өм")],
    ]

    biz = [
        [u"йбыз", u"йбуз", u"йбиз", u"йбүз"],
        [J(u"абыз"), J((u"обуз", u"абыз")), J(u"ебиз"), J(u"өбүз")],
        [J(u"абыз"), J((u"обуз", u"абыз")), J(u"ебиз"), J(u"өбүз")],
        [J(u"абыз"), J((u"обуз", u"абыз")), J(u"ебиз"), J(u"өбүз")],
    ]

    sen = [
        [u"йсың", u"йсуң", u"йсиң", u"йсүң"],
        [J(u"асың"), J((u"осуң", u"асың")), J(u"есиң"), J(u"өсүң")],
        [J(u"асың"), J((u"осуң", u"асың")), J(u"есиң"), J(u"өсүң")],
        [J(u"асың"), J((u"осуң", u"асың")), J(u"есиң"), J(u"өсүң")],
    ]

    siler = [
        [u"йсыңар", u"йсуңар", u"йсиңер", u"йсүңөр"],
        [J(u"асыңар"), J((u"осуңар", u"асыңар")), J(u"есиңер"), J(u"өсүңөр")],
        [J(u"асыңар"), J((u"осуңар", u"асыңар")), J(u"есиңер"), J(u"өсүңөр")],
        [J(u"асыңар"), J((u"осуңар", u"асыңар")), J(u"есиңер"), J(u"өсүңөр")],
    ]

    siz = [
        [u"йсыз", u"йсуз", u"йсиз", u"йсүз"],
        [J(u"асыз"), J((u"осуз", u"асыз")), J(u"есиз"), J(u"өсүз")],
        [J(u"асыз"), J((u"осуз", u"асыз")), J(u"есиз"), J(u"өсүз")],
        [J(u"асыз"), J((u"осуз", u"асыз")), J(u"есиз"), J(u"өсүз")],
    ]

    sizder = [
        [u"йсыздар", u"йсуздар", u"йсиздер", u"йсүздөр"],
        [J(u"асыздар"), J((u"осуздар", u"асыздар")), J(u"есиздер"), J(u"өсүздөр")],
        [J(u"асыздар"), J((u"осуздар", u"асыздар")), J(u"есиздер"), J(u"өсүздөр")],
        [J(u"асыздар"), J((u"осуздар", u"асыздар")), J(u"есиздер"), J(u"өсүздөр")],
    ]

    al = [
        [u"йт", u"йт", u"йт", u"йт"],
        [J(u"ат"), J((u"от", u"ат")), J(u"ет"), J(u"өт")],
        [J(u"ат"), J((u"от", u"ат")), J(u"ет"), J(u"өт")],
        [J(u"ат"), J((u"от", u"ат")), J(u"ет"), J(u"өт")],
    ]

    alar = [
        [u"шат", (u"шот", u"шат"), u"шет", u"шөт"],
        [J(u"ышат"), J(u"ушат"), J(u"ишет"), J(u"үшөт")],
        [J(u"ышат"), J(u"ушат"), J(u"ишет"), J(u"үшөт")],
        [J(u"ышат"), J(u"ушат"), J(u"ишет"), J(u"үшөт")],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucholor = select_for_attrs(jak, jeke, sylyk, self.men, self.sen, self.al, self.biz, self.siler, self.alar,
                                        self.siz, self.sizder)

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
            start_of_result, end_of_result = self.change_yottoshkon_tamga(end_of_result, start_of_result)
            return self.word_object.change(start_of_result, end_of_result, "keler_chak", WordAttrs(jak, jeke, sylyk))
        return self.word_object
