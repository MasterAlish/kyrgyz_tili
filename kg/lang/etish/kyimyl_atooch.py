from kg.lang.affix import Affix
from kg.lang.helps.attrs import WordAttrs
from kg.lang.lang import WordEndingTypes
from kg.lang.mucho import *


class KyimylAtooch(Affix):
    def __init__(self, word_object):
        self.word_object = word_object
        self.word_object.prepare()

    def transformers(self):
        return [KyimylAtooch.make]

    mucholor = [
        [U(("оо", "уу")), U(("оо", "уу")), U(("өө", "үү")), U(("өө", "үү"))],
        [J("уу"), J("уу"), J("үү"), J("үү")],
        [J("уу"), J("уу"), J("үү"), J("үү")],
        [J("уу"), J("уу"), J("үү"), J("үү")],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[index_i][index_j]
            start_of_result = self.word_object.word + ""
            end_of_result = mucho
            if isinstance(end_of_result, SpecialMucho):
                start_of_result, end_of_result = end_of_result.make(self.word_object.word)
            if isinstance(end_of_result, tuple):
                if self.word_object.unduu_type_jaaktuu:
                    end_of_result = end_of_result[0]
                else:
                    end_of_result = end_of_result[1]
            start_of_result, end_of_result = self._change_yottoshkon_tamga(start_of_result, end_of_result)
            return self.word_object.change(start_of_result, end_of_result, "kyimyl_atooch", WordAttrs(jak, jeke, sylyk))
        return self.word_object

    def _change_yottoshkon_tamga(self, start_of_result, end_of_result):
        if start_of_result[-1] in ['ё', 'ю']:
            return start_of_result, end_of_result[0]
        elif start_of_result[-1] in ['й', 'я']:
            new_start_of_result = self._change_start_of_result(start_of_result, end_of_result)
            if start_of_result != new_start_of_result:
                return new_start_of_result, end_of_result[0]
        return start_of_result, end_of_result

    def _change_start_of_result(self, start_of_result, end_of_result):
        if end_of_result[0] == "у":
            start_of_result = start_of_result[:-1] + 'ю'
        elif end_of_result[0] == "о":
            start_of_result = start_of_result[:-1] + 'ё'
        return start_of_result


class KyimylAtooch2(KyimylAtooch):
    def transformers(self):
        return [KyimylAtooch2.make]

    mucholor = [
        [J("ш"), J("ш"), J("ш"), J("ш")],
        [J("ыш"), J("уш"), J("иш"), J("үш")],
        [J("ыш"), J("уш"), J("иш"), J("үш")],
        [J("ыш"), J("уш"), J("иш"), J("үш")],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[index_i][index_j]
            start_of_result = self.word_object.word + ""
            end_of_result = mucho
            if isinstance(end_of_result, SpecialMucho):
                start_of_result, end_of_result = end_of_result.make(self.word_object.word)
            start_of_result, end_of_result = self._change_yottoshkon_tamga(start_of_result, end_of_result)
            return self.word_object.change(start_of_result, end_of_result, "kyimyl_atooch2", WordAttrs(jak, jeke, sylyk))
        return self.word_object.word

    def _change_yottoshkon_tamga(self, start_of_result, end_of_result):
        if start_of_result[-1] in ['й']:
            new_start_of_result = self._change_start_of_result(start_of_result, end_of_result)
            if start_of_result != new_start_of_result:
                return new_start_of_result, end_of_result[1:]
        return start_of_result, end_of_result