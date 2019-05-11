import hashlib
import base64

class ValgrindError(object):
    def __init__(self, xml_error=None):
        self.xml_error = xml_error
        self.failure_type = None
        self.failure_message = None
        self.stack = None

    def get_testcase_time(self):
        if self.xml_error is None:
            return ''
        return '0'

    def get_testcase_classname(self, classname=None):
        if self.xml_error is None:
            return ''
        if classname is None:
            return 'valgrind'
        return classname

    def get_testcase_name(self, seed=None):
        if self.xml_error is None:
            return ''
        if seed is None:
            return self.xml_error.find('unique').text
        hash_str = self.get_hash(seed)
        return ' '.join([self.get_failure_type(), hash_str])

    def get_failure_type(self): # kind tag in valgrind
        if self.failure_type is not None:
            return self.failure_type
        if self.xml_error is None:
            return ''
        kind_tag = self.xml_error.find('kind')
        if kind_tag is not None:
            self.failure_type = kind_tag.text
            return self.failure_type
        return ''

    def get_failure_message(self): # what tag in valgrind
        if self.failure_message is not None:
            return self.failure_message
        if self.xml_error is None:
            return ''
        what_tag = self.xml_error.find('what')
        if what_tag is not None:
            self.failure_type = what_tag.text
            return self.failure_type
        return ''

    def get_failure_details(self): # stack tag in valgrind
        if self.stack is not None:
            return self.stack
        if self.xml_error is None:
            return ''
        stack_tag = self.xml_error.find('stack')
        if stack_tag is not None:
            self.stack = ' '.join(x.text for x in stack_tag.iter())
            return self.stack
        return ''

    def remove_tags(self, tag_to_remove):
        if self.xml_error is None:
            return False
        parent_child = list()
        for parent in self.xml_error.getiterator():
            for child in parent:
                if child.tag == tag_to_remove:
                    parent_child.append((parent, child))
        for parent, child in parent_child:
            parent.remove(child)
        return True if len(parent_child) else False

    def get_hash(self, input=''):
        self.remove_tags('ip')
        kind_str = self.get_failure_type()
        what_str = self.get_failure_message()
        stack_str = self.get_failure_details()
        str_to_hash = input + kind_str + what_str + stack_str
        md5_str = hashlib.md5(str_to_hash.encode('utf-8')).digest()
        base64_str = base64.b64encode(md5_str)
        return str(base64_str)[2:-1]