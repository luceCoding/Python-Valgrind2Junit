import os
import unittest
from valgrind.valgrind_parser import ValgrindParser
import pytest

class test_valgrind_parser(unittest.TestCase):
    def setUp(self):
        self.valgrind_test_file = os.path.join(os.path.dirname(__file__), 'sample_data/valgrind-test.xml')

    def tearDown(self):
        pass

    def test_get_next_error(self):
        parser = ValgrindParser(self.valgrind_test_file)
        error_generator = parser.get_next_error()
        count = 0
        for error in error_generator:
            count += 1
            assert error is not None
        assert count == 2
        with pytest.raises(StopIteration):
            next(error_generator)
