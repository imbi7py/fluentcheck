import unittest
from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


class TestCollectionsAssertions(unittest.TestCase):

    def test_is_set(self):
        res = Check(set()).is_set()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_set()
            self.fail()
        except CheckError:
            pass

    def test_is_not_set(self):
        res = Check(123).is_not_set()
        self.assertIsInstance(res, Check)
        try:
            Check(set()).is_not_set()
            self.fail()
        except CheckError:
            pass

    def test_is_subset(self):
        s = set([1, 2, 3])
        res = Check(s).is_subset_of(set([1, 2, 3, 4, 5]))
        self.assertIsInstance(res, Check)
        try:
            Check(s).is_subset_of(set([7]))
            self.fail()
        except CheckError:
            pass

    def test_is_not_subset(self):
        s = set([1, 2, 3])
        res = Check(s).is_not_subset_of(set([7]))
        self.assertIsInstance(res, Check)
        try:
            Check(s).is_not_subset_of(set([1, 2, 3, 4, 5]))
            self.fail()
        except CheckError:
            pass

    def test_is_superset(self):
        s = set([1, 2, 3, 4, 5])
        res = Check(s).is_superset_of(set([1, 2, 3]))
        self.assertIsInstance(res, Check)
        try:
            Check(s).is_superset_of(set([7]))
            self.fail()
        except CheckError:
            pass

    def test_is_not_superset(self):
        s = set([1, 2, 3])
        res = Check(s).is_not_superset_of(set([1, 2, 3, 4, 5]))
        self.assertIsInstance(res, Check)
        try:
            Check(s).is_not_superset_of(set([1, 2]))
            self.fail()
        except CheckError:
            pass

    def test_intersects(self):
        s = set([1, 2, 3, 4, 5])
        res = Check(s).intersects(set([1, 2, 3]))
        self.assertIsInstance(res, Check)
        try:
            Check(s).intersects(set([7]))
            self.fail()
        except CheckError:
            pass

    def test_not_intersects(self):
        s = set([1, 2, 3])
        res = Check(s).not_intersects(set([7, 8, 9]))
        self.assertIsInstance(res, Check)
        try:
            Check(s).not_intersects(set([1, 2]))
            self.fail()
        except CheckError:
            pass
