# coding=utf-8
class WordAttrs(object):
    def __init__(self, jak=1, jeke=True, sylyk=False):
        self.jak = jak
        self.jeke = jeke
        self.sylyk = sylyk

    def as_args(self):
        return self.jak, self.jeke, self.sylyk

    def __unicode__(self):
        return u"%d жак %s %s" % (self.jak, u"жеке" if self.jeke else u'көп', u"сылык" if self.sylyk else u"")

    def __str__(self):
        return self.__unicode__()


men = WordAttrs(1, True, False)
sen = WordAttrs(2, True, False)
al = WordAttrs(3, True, False)
biz = WordAttrs(1, False, False)
siler = WordAttrs(2, False, False)
alar = WordAttrs(3, False, False)
siz = WordAttrs(2, True, True)
sizder = WordAttrs(2, False, True)