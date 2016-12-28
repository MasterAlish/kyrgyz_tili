# coding=utf-8
from kg_lang.kyrgyz.affix import Affix
from kg_lang.kyrgyz.lang import select_for_attrs


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
            [u"нын", u"нун", u"нин", u"нүн"],
            [u"дын", u"дун", u"дин", u"дүн"],
            [u"дын", u"дун", u"дин", u"дүн"],
            [u"тын", u"тун", u"тин",u"түн"]]
    
        taandyk_sen = [u"дын", u"дун", u"дин", u"дүн"]
    
        taandyk_siler = [u"дын", (u"дун", u"дын"), u"дин", u"дүн"]
    
        taandyk_al = [u"нын", u"нун", u"нин", u"нүн"]

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
                start_of_result = self.word_object.word + u""
                end_of_result = mucho
                if isinstance(end_of_result, tuple):
                    if self.word_object.unduu_type_jaaktuu:
                        end_of_result = end_of_result[0]
                    else:
                        end_of_result = end_of_result[1]
                return self.word_object.change(start_of_result, end_of_result, "ilik")
            return self.word_object

        def is_special_word(self):
            special_words = [u'мен', u'сен', u'ал', u'ол', u'бул', u'ушул', ]
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {u'мен': u'менин',
                                   u'сен': u'сенин',
                                   u'ал': u'анын',
                                   u'ол': u'онун',
                                   u'бул': u'бунун',
                                   u'ушул': u'ушунун'}
            return special_conversions[self.word_object.word]

    class Barysh(object):
        mucholor = [
            [u"га", (u"го", u"га"), u"ге", u"гө"],
            [u"га", (u"го", u"га"), u"ге", u"гө"],
            [u"га", (u"го", u"га"), u"ге", u"гө"],
            [u"ка", (u"ко", u"ка"), u"ке", u"кө"]]

        taandyk_men = [u"а", (u"о", u"а"), u"е", u"ө"]

        taandyk_al = [u"на", u"на", u"не", u"нө"]

        taandyk_biz = [u"га", u"га", u"ге", u"гө"]

        taandyk_siler = [u"га", (u"го", u"га"), u"ге", u"гө"]

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
                start_of_result = self.word_object.word + u""
                end_of_result = mucho
                if isinstance(end_of_result, tuple):
                    if self.word_object.unduu_type_jaaktuu:
                        end_of_result = end_of_result[0]
                    else:
                        end_of_result = end_of_result[1]
                return self.word_object.change(start_of_result, end_of_result, "barysh")
            return self.word_object

        def is_special_word(self):
            special_words = [u'мен', u'сен', u'ал', u'ол', u'бул', u'ушул']
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {u'мен': u'мага',
                                   u'сен': u'сага',
                                   u'ал': u'ага',
                                   u'ол': u'ого',
                                   u'бул': u'буга',
                                   u'ушул': u'ушуга'}
            return special_conversions[self.word_object.word]

    class Tabysh(object):
        mucholor = [[u"ны", u"ну", u"ни", u"нү"],
                    [u"ды", u"ду", u"ди", u"дү"],
                    [u"ды", u"ду", u"ди", u"дү"],
                    [u"ты", u"ту", u"ти", u"тү"]]

        taandyk_al = u"н"

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
                start_of_result = self.word_object.word + u""
                end_of_result = mucho
                return self.word_object.change(start_of_result, end_of_result, "tabysh")
            return self.word_object

        def is_special_word(self):
            special_words = [u'мен', u'сен', u'ал', u'ол', u'бул', u'ушул']
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {u'мен': u'мени',
                                   u'сен': u'сени',
                                   u'ал': u'аны',
                                   u'ол': u'ону',
                                   u'бул': u'буну',
                                   u'ушул': u'ушуну'}
            return special_conversions[self.word_object.word]

    class Jatysh(object):
        mucholor = [[u"да", (u"до", u"да"), u"де", u"дө"],
                    [u"да", (u"до", u"да"), u"де", u"дө"],
                    [u"да", (u"до", u"да"), u"де", u"дө"],
                    [u"та", (u"то", u"та"), u"те", u"тө"]]

        taandyk_al = [u"нда", (u"ндо", u"нда"), u"нде", u"ндө"]

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
                start_of_result = self.word_object.word + u""
                end_of_result = mucho
                if isinstance(end_of_result, tuple):
                    if self.word_object.unduu_type_jaaktuu:
                        end_of_result = end_of_result[0]
                    else:
                        end_of_result = end_of_result[1]
                return self.word_object.change(start_of_result, end_of_result, "jatysh")
            return self.word_object

        def is_special_word(self):
            special_words = [u'ал', u'ол', u'бул', u'ушул']
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {u'ал': u'анда',
                                   u'ол': u'ондо',
                                   u'бул': u'буда',
                                   u'ушул': u'ушуда'}
            return special_conversions[self.word_object.word]

    class Chygysh(object):
        mucholor = [[u"дан", (u"дон", u"дан"), u"ден", u"дөн"],
                    [u"дан", (u"дон", u"дан"), u"ден", u"дөн"],
                    [u"дан", (u"дон", u"дан"), u"ден", u"дөн"],
                    [u"тан", (u"тон", u"тан"), u"тен", u"төн"]]

        taandyk_al = [u"нан", u"нан", u"нен", u"нөн"]

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
                start_of_result = self.word_object.word + u""
                end_of_result = mucho
                if isinstance(end_of_result, tuple):
                    if self.word_object.unduu_type_jaaktuu:
                        end_of_result = end_of_result[0]
                    else:
                        end_of_result = end_of_result[1]
                return self.word_object.change(start_of_result, end_of_result, "chygysh")
            return self.word_object

        def is_special_word(self):
            special_words = [u'мен', u'сен', u'ал', u'ол', u'бул', u'ушул']
            return not self.word_object.is_name and self.word_object.word in special_words

        def special_conversion(self):
            special_conversions = {u'мен': u'менен',
                                   u'сен': u'сенен',
                                   u'ал': u'андан',
                                   u'ол': u'ондон',
                                   u'бул': u'будан',
                                   u'ушул': u'ушудан'}
            return special_conversions[self.word_object.word]
