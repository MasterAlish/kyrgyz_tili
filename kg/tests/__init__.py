# coding=utf-8
import sys
import traceback
from unittest import TestCase

from kg.lang.lang import KyrgyzWord


class KGTestCase(TestCase):
    def assertEqual(self, actual, expected, msg=None):
        try:
            if isinstance(actual, KyrgyzWord):
                actual = unicode(actual)
            super(KGTestCase, self).assertEqual(actual, expected)
        except:
            if msg:
                raise AssertionError(msg.encode("utf-8"))
            else:
                raise AssertionError((u"\n\n'%s' - болуш керек эле, '%s' - болуп калды\n\n" % (expected, actual)).encode("utf-8"))
