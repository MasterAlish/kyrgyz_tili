"""
WordChange - Одно изменение слова, которая составляет историю изменения слова
    affix = название аффикса, который был применен
    attrs - абрибуты слова по трем координатам
    index - индекс начала аффикса в слове
"""


class WordChange(object):
    def __init__(self, affix, index, attrs=None):
        self.affix = affix
        self.attrs = attrs
        self.index = index

    def __str__(self):
        return "%s %s" % (self.affix, ("("+self.attrs+")" if self.attrs else ""))
