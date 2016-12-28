# coding=utf-8
class WordChange(object):
    def __init__(self, feature, index, attrs=None):
        self.feature = feature
        self.attrs = attrs
        self.index = index

    def __unicode__(self):
        return u"%s %s" % (unicode(self.feature), (u"("+unicode(self.attrs)+u")" if self.attrs else u""))

    def __str__(self):
        return self.__unicode__()
