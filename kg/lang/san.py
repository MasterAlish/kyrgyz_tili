from kg.lang.affix import Affix


class San(Affix):
    illegal_prev_affixes = ['taandyk']

    def __init__(self, word_object):
        """:type word_object: kg_lang.kyrgyz.lang.KyrgyzWord """
        self.word_object = word_object
        self.word_object.prepare()

    def transformers(self):
        if self.word_object.last_affix() in self.illegal_prev_affixes:
            return []
        return [San.koptuk]

    mucholor = [
        ["лар", ("лор", "лар"), "лер", "лөр"],
        ["дар", ("дор", "дар"), "дер", "дөр"],
        ["лар", ("лор", "лар"), "лер", "лөр"],
        ["тар", ("тор", "тар"), "тер", "төр"],
    ]

    def koptuk(self):
        if self.word_object.last_affix() in self.illegal_prev_affixes:
            return self.word_object
        if self.is_special_word():
            try:
                result, index = self.special_conversion()
                return self.word_object.change(result[:index], result[index:], "koptuk")
            except KeyError:
                pass

        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            i_unsuz, i_unduu = Affix.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[i_unsuz][i_unduu]
            end_of_result = mucho
            if isinstance(end_of_result, tuple):
                if self.word_object.unduu_type_jaaktuu:
                    end_of_result = end_of_result[0]
                else:
                    end_of_result = end_of_result[1]
            return self.word_object.change(self.word_object.word, end_of_result, "koptuk")
        return self.word_object

    def is_special_word(self):
        special_words = ['бала', 'мен', 'сен', 'ал', 'ол', 'биз', 'силер', 'сиздер', 'алар', 'бул', 'булар',
                         'ушул', 'ушулар']
        return not self.word_object.is_name and self.word_object.word in special_words

    def special_conversion(self):
        special_conversions = {
            'бала': ('балдар', 3),
            'мен': ('биз', 0),
            'сен': ('силер', 2),
            'ал': ('алар', 1),
            'ол': ('олор', 1),
            'биз': ('биз', 0),
            'силер': ('силер', 2),
            'сиздер': ('сиздер', 3),
            'алар': ('алар', 1),
            'бул': ('булар', 2),
            'булар': ('булар', 2),
            'ушул': ('ушулар', 3),
            'ушулар': ('ушулар', 3),
        }
        return special_conversions[self.word_object.word]
