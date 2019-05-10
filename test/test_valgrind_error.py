import os
import unittest
from valgrind.valgrind_error import ValgrindError
from valgrind.valgrind_parser import ValgrindParser

class test_valgrind_error(unittest.TestCase):
    def setUp(self):
        self.valgrind_test_file = os.path.join(os.path.dirname(__file__), 'data/valgrind-test.xml')
        self.junit_test_file = os.path.join(os.path.dirname(__file__), 'data/junit.xml')
        self.parser = ValgrindParser(self.valgrind_test_file)
        self.error_generator = self.parser.get_next_error()
        self.no_error = ValgrindError()

    def tearDown(self):
        pass

    def test_get_testcase_time(self):
        assert self.no_error.get_testcase_time() == ''
        for error in self.error_generator:
            assert error.get_testcase_time() == '0'

    def test_get_testcase_classname(self):
        assert self.no_error.get_testcase_classname() == ''
        for error in self.error_generator:
            assert error.get_testcase_classname() == 'valgrind'

    def test_get_testcase_name(self):
        assert self.no_error.get_testcase_name() == ''
        assert next(self.error_generator).get_testcase_name() == '0x0'
        assert next(self.error_generator).get_testcase_name() == '0x1'

    def test_get_testcase_name_with_seed(self):
        assert self.no_error.get_testcase_name() == ''
        assert next(self.error_generator).get_testcase_name() == '0x0'
        assert next(self.error_generator).get_testcase_name() == '0x1'

    def test_get_failure_type(self):
        assert self.no_error.get_failure_type() == ''
        assert next(self.error_generator).get_failure_type() == 'UninitCondition'
        assert next(self.error_generator).get_failure_type() == 'SyscallParam'

    def test_get_failure_message(self):
        assert self.no_error.get_failure_message() == ''
        assert next(self.error_generator).get_failure_message() == 'Conditional jump or move depends on uninitialised value(s)'
        assert next(self.error_generator).get_failure_message() == 'Syscall param write(buf) points to uninitialised byte(s)'

    def test_get_failure_details(self):
        assert self.no_error.get_failure_details() == ''
        #TODO

    def test_remove_tags(self):
        assert self.no_error.remove_tags('ip') == False
        assert next(self.error_generator).remove_tags('ip') == True
        #TODO

    def test_get_hash(self):
        assert print(self.no_error.get_hash()) != ''
        assert next(self.error_generator).get_hash() == 'Xm+OrwiB2RBaBW9bgd0BWg=='
        assert next(self.error_generator).get_hash() == 'jNJfR35lhiBOXlD/QkJHHA=='