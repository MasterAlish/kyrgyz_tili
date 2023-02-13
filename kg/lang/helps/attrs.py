"""
WordAttrs - Структура хранящая свойства слова по трем измерениям:
    jak - лицо(1, 2, 3)
    jeke - число(True-един, False-множ)
    sylyk - уважительная форма(True-да, False-нет)
"""


class WordAttrs(object):
    def __init__(self, jak=1, jeke=True, sylyk=False):
        self.jak = jak
        self.jeke = jeke
        self.sylyk = sylyk

    def as_args(self):
        return self.jak, self.jeke, self.sylyk

    def __str__(self):
        return "%d жак %s %s" % (self.jak, "жеке" if self.jeke else 'көп', "сылык" if self.sylyk else "")


men = WordAttrs(1, True, False)  # я
sen = WordAttrs(2, True, False)  # ты
al = WordAttrs(3, True, False)  # он / она
biz = WordAttrs(1, False, False)  # мы
siler = WordAttrs(2, False, False)  # вы (множ. число)
alar = WordAttrs(3, False, False)  # они
siz = WordAttrs(2, True, True)  # вы (един. число уважительно)
sizder = WordAttrs(2, False, True)  # вы (множ. число уважительно)
