from lxml import etree as ET

class JUnitXMLGenerator(object):
    def __init__(self):
        self.testsuite = None

    @staticmethod
    def create_testsuite(self, **kwargs):
        return ET.Element('testsuite', attrib=kwargs)

    @staticmethod
    def create_testcase(self, **kwargs):
        ET.SubElement(self.testsuite, 'testcase', attrib=kwargs)
        return True

    def add_testsuite(self, **kwargs):
        self.testsuite = ET.Element('testsuite', attrib=kwargs)
        return self.testsuite

    def add_testcase(self, **kwargs):
        if self.testsuite is None:
            return None
        ET.SubElement(self.testsuite, 'testcase', attrib=kwargs)
        return self.testsuite

    def output_xml(self, xml_path):
        if self.testsuite is None:
            return False
        tree = ET.ElementTree(self.testsuite)
        tree.write(xml_path,
                   pretty_print=True,
                   xml_declaration=True,
                   encoding='UTF-8')
        return True