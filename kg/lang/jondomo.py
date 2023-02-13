from kg.lang.affix import Affix
from kg.lang.lang import select_for_attrs


class Jondomo(Affix):
    def __init__(self, word_object):
        self.word_object = word_object
        self.word_object.prepare()

    def transformers(self):
        return [Jondomo.ilik, Jondomo.barysh, Jondomo.tabysh, Jondomo.jatysh, Jondomo.chygysh]

    def atooch(self):
        return self.word_object

    def ilik(self):
        return self.Ilik(self.word_object).make()

    def barysh(self):
        return self.Barysh(self.word_object).make()

    def tabysh(self):
        return self.Tabysh(self.word_object).make()

    def jatysh(self):
        return self.Jatysh(self.word_object).make()

    def chygysh(self):
        return self.Chygysh(self.word_object).make()

    class Ilik(object):

        mucholor = [
            ["нын", "нун", "нин", "нүн"],
            ["дын", "дун", "дин", "дүн"],
            ["дын", "дун", "дин", "дүн"],
            ["тын", "тун", "тин", "түн"],
        ]

        taandyk_sen = ["дын", "дун", "дин", "дүн"]

        taandyk_siler = ["дын", ("дун", "дын"), "дин", "дүн"]

        taandyk_al = ["нын", "нун", "нин", "нүн"]

        def __init__(self, word_object):
            self.word_object = word_object

        def make(self):
            if self.is_special_word():
                try:
                    return self.special_conversion()
                except KeyError:
                    pass

            if self.word_object.unsuz_end_type and self.word_object.unduu_type:
                i_unsuz, i_unduu = Affix.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
                mucho = self.mucholor[i_unsuz][i_unduu]
                if self.word_object.last_affix() == 'taandyk' and self.word_object.last_change_attrs():
                    attrs = self.word_object.last_change_attrs()
                    mucho = select_for_attrs(attrs.jak, attrs.jeke, attrs.sylyk, self.taandyk_sen, self.taandyk_sen,
                                             self.taandyk_al, self.taandyk_sen, self.taandyk_siler, self.taandyk_al,
                                             self.taandyk_sen, self.taandyk_sen)
                    mucho = mucho[i_unduu]
                start_of_result = self.word_object.word + ""
                end_of_result = mucho
                if isinstance(end_of_result, tuple):
                    if self.word_object.unduu_type_jaaktuu:
                        end_of_result = end_of_result[0]
                    else:
                        end_of_result = end_of_result[1]
                return self.word_object.change(start_of_result, end_of_result, "ilik")
            return self.word_object

        def is_special_word(self):
            special_words = ['мен', 'сен', 'ал', 'ол', 'бул', 'ушул', ]
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {
                'мен': 'менин',
                'сен': 'сенин',
                'ал': 'анын',
                'ол': 'онун',
                'бул': 'бунун',
                'ушул': 'ушунун',
            }
            return special_conversions[self.word_object.word]

    class Barysh(object):
        mucholor = [
            ["га", ("го", "га"), "ге", "гө"],
            ["га", ("го", "га"), "ге", "гө"],
            ["га", ("го", "га"), "ге", "гө"],
            ["ка", ("ко", "ка"), "ке", "кө"],
        ]

        taandyk_men = ["а", ("о", "а"), "е", "ө"]

        taandyk_al = ["на", "на", "не", "нө"]

        taandyk_biz = ["га", "га", "ге", "гө"]

        taandyk_siler = ["га", ("го", "га"), "ге", "гө"]

        def __init__(self, word_object):
            """:type word_object: kg_lang.kyrgyz.lang.KyrgyzWord"""
            self.word_object = word_object

        def make(self):
            if self.is_special_word():
                try:
                    return self.special_conversion()
                except KeyError:
                    pass

            if self.word_object.unsuz_end_type and self.word_object.unduu_type:
                i_unsuz, i_unduu = Affix.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
                mucho = self.mucholor[i_unsuz][i_unduu]
                if self.word_object.last_affix() == 'taandyk' and self.word_object.last_change_attrs():
                    attrs = self.word_object.last_change_attrs()
                    mucho = select_for_attrs(attrs.jak, attrs.jeke, attrs.sylyk, self.taandyk_men, self.taandyk_men,
                                             self.taandyk_al, self.taandyk_biz, self.taandyk_siler, self.taandyk_al,
                                             self.taandyk_siler, self.taandyk_biz)
                    mucho = mucho[i_unduu]
                start_of_result = self.word_object.word + ""
                end_of_result = mucho
                if isinstance(end_of_result, tuple):
                    if self.word_object.unduu_type_jaaktuu:
                        end_of_result = end_of_result[0]
                    else:
                        end_of_result = end_of_result[1]
                return self.word_object.change(start_of_result, end_of_result, "barysh")
            return self.word_object

        def is_special_word(self):
            special_words = ['мен', 'сен', 'ал', 'ол', 'бул', 'ушул']
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {
                'мен': 'мага',
                'сен': 'сага',
                'ал': 'ага',
                'ол': 'ого',
                'бул': 'буга',
                'ушул': 'ушуга',
            }
            return special_conversions[self.word_object.word]

    class Tabysh(object):
        mucholor = [
            ["ны", "ну", "ни", "нү"],
            ["ды", "ду", "ди", "дү"],
            ["ды", "ду", "ди", "дү"],
            ["ты", "ту", "ти", "тү"],
        ]

        taandyk_al = "н"

        def __init__(self, word_object):
            self.word_object = word_object

        def make(self):
            if self.is_special_word():
                try:
                    return self.special_conversion()
                except KeyError:
                    pass

            if self.word_object.unsuz_end_type and self.word_object.unduu_type:
                i_unsuz, i_unduu = Affix.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
                mucho = self.mucholor[i_unsuz][i_unduu]
                if self.word_object.last_affix() == 'taandyk' and self.word_object.last_change_attrs():
                    if self.word_object.last_change_attrs().jak == 3:
                        mucho = self.taandyk_al
                start_of_result = self.word_object.word + ""
                end_of_result = mucho
                return self.word_object.change(start_of_result, end_of_result, "tabysh")
            return self.word_object

        def is_special_word(self):
            special_words = ['мен', 'сен', 'ал', 'ол', 'бул', 'ушул']
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {
                'мен': 'мени',
                'сен': 'сени',
                'ал': 'аны',
                'ол': 'ону',
                'бул': 'буну',
                'ушул': 'ушуну',
            }
            return special_conversions[self.word_object.word]

    class Jatysh(object):
        mucholor = [
            ["да", ("до", "да"), "де", "дө"],
            ["да", ("до", "да"), "де", "дө"],
            ["да", ("до", "да"), "де", "дө"],
            ["та", ("то", "та"), "те", "тө"],
        ]

        taandyk_al = ["нда", ("ндо", "нда"), "нде", "ндө"]

        def __init__(self, word_object):
            self.word_object = word_object

        def make(self):
            if self.is_special_word():
                try:
                    return self.special_conversion()
                except KeyError:
                    pass

            if self.word_object.unsuz_end_type and self.word_object.unduu_type:
                i_unsuz, i_unduu = Affix.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
                mucho = self.mucholor[i_unsuz][i_unduu]
                if self.word_object.last_affix() == 'taandyk' and self.word_object.last_change_attrs():
                    if self.word_object.last_change_attrs().jak == 3:
                        mucho = self.taandyk_al[i_unduu]
                start_of_result = self.word_object.word + ""
                end_of_result = mucho
                if isinstance(end_of_result, tuple):
                    if self.word_object.unduu_type_jaaktuu:
                        end_of_result = end_of_result[0]
                    else:
                        end_of_result = end_of_result[1]
                return self.word_object.change(start_of_result, end_of_result, "jatysh")
            return self.word_object

        def is_special_word(self):
            special_words = ['ал', 'ол', 'бул', 'ушул']
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {
                'ал': 'анда',
                'ол': 'ондо',
                'бул': 'буда',
                'ушул': 'ушуда',
            }
            return special_conversions[self.word_object.word]

    class Chygysh(object):
        mucholor = [
            ["дан", ("дон", "дан"), "ден", "дөн"],
            ["дан", ("дон", "дан"), "ден", "дөн"],
            ["дан", ("дон", "дан"), "ден", "дөн"],
            ["тан", ("тон", "тан"), "тен", "төн"],
        ]

        taandyk_al = ["нан", "нан", "нен", "нөн"]

        def __init__(self, word_object):
            self.word_object = word_object

        def make(self):
            if self.is_special_word():
                try:
                    return self.special_conversion()
                except KeyError:
                    pass

            if self.word_object.unsuz_end_type and self.word_object.unduu_type:
                i_unsuz, i_unduu = Affix.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
                mucho = self.mucholor[i_unsuz][i_unduu]
                if self.word_object.last_affix() == 'taandyk' and self.word_object.last_change_attrs():
                    if self.word_object.last_change_attrs().jak == 3:
                        mucho = self.taandyk_al[i_unduu]
                start_of_result = self.word_object.word + ""
                end_of_result = mucho
                if isinstance(end_of_result, tuple):
                    if self.word_object.unduu_type_jaaktuu:
                        end_of_result = end_of_result[0]
                    else:
                        end_of_result = end_of_result[1]
                return self.word_object.change(start_of_result, end_of_result, "chygysh")
            return self.word_object

        def is_special_word(self):
            special_words = ['мен', 'сен', 'ал', 'ол', 'бул', 'ушул']
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {
                'мен': 'менен',
                'сен': 'сенен',
                'ал': 'андан',
                'ол': 'ондон',
                'бул': 'будан',
                'ушул': 'ушудан'
            }
            return special_conversions[self.word_object.word]
