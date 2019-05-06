from lxml import etree as ET
from parser.valgrind_error import ValgrindError

class ValgrindParser(object):

    def __init__(self, valgrind_file_name):
        self.valgrind_file_name = valgrind_file_name
        self.root = None
        self.n_errors = None

    def get_next_error(self):
        if self.root is None:
            self.root = ET.parse(self.valgrind_file_name).getroot()
        for error in self.root.findall('error'):
            yield ValgrindError(error)
