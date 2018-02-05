# Begin: Python 2/3 compatibility header small
# Get Python 3 functionality:
from __future__ import\
    absolute_import, print_function, division, unicode_literals
from future.utils import raise_with_traceback, raise_from
# catch exception with: except Exception as e
from builtins import range, map, zip, filter
from io import open
import six
# End: Python 2/3 compatability header small


###############################################################################
###############################################################################
###############################################################################


# todo:fix relative imports:
#from ...utils.tests import dryrun

from innvestigate.utils.tests import dryrun

from innvestigate.analyzer import *


###############################################################################
###############################################################################
###############################################################################


class TestBaselineLRPZ(dryrun.AnalyzerTestCase):

    def _method(self, model):
        return BaselineLRPZ(model)


###############################################################################
###############################################################################
###############################################################################


class TestLRPZ(dryrun.AnalyzerTestCase):

    def _method(self, model):
        return LRPZ(model)


class TestLRPWSquare(dryrun.AnalyzerTestCase):

    def _method(self, model):
        return LRPWSquare(model)


class TestLRPFlat(dryrun.AnalyzerTestCase):

    def _method(self, model):
        return LRPFlat(model)


class TestLRPZ__equal_BaselineLRPZ(dryrun.EqualAnalyzerTestCase):

    def _method1(self, model):
        return BaselineLRPZ(model)

    def _method2(self, model):
        return LRPZ(model)


class TestLRPEpsilon(dryrun.AnalyzerTestCase):

    def _method(self, model):
        return LRPEpsilon(model)


class TestLRPA1B1(dryrun.AnalyzerTestCase):

    def _method(self, model):
        return LRPA1B1(model)


class TestLRPBoxed(dryrun.AnalyzerTestCase):

    def _method(self, model):
        return LRPBoxed(model)
