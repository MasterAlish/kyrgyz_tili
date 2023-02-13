from kg.lang.affix import Affix
from kg.lang.lang import WordEndingTypes
from kg.lang.mucho import SpecialMucho, L


class LuuZatMuchosu(Affix):
    def __init__(self, word_object):
        self.word_object = word_object
        self.word_object.prepare()

    def transformers(self):
        return [LuuZatMuchosu.make]

    mucholor = [
        ["луу", "луу", "лүү", "лүү"],
        ["дуу", "дуу", "дүү", "дүү"],
        [L(("дуу", "луу")), L(("дуу", "луу")), "лүү", "лүү"],
        ["туу", "туу", "түү", "түү"],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[index_i][index_j]
            start_of_result = self.word_object.word + ""
            end_of_result = mucho
            if isinstance(end_of_result, SpecialMucho):
                start_of_result, end_of_result = end_of_result.make(self.word_object.word)
            return start_of_result + end_of_result
        return self.word_object.word
