from lxml import etree as ET

class JUnitXML(object):
    def __init__(self, **kwargs):
        self.testsuite = ET.Element('testsuite', attrib=kwargs)

    def add_testcase(self, **kwargs):
        if self.testsuite is None:
            return False
        ET.SubElement(self.testsuite, 'testcase', attrib=kwargs)
        return True

    def output_xml(self, xml_path):
        if self.testsuite is None:
            return False
        tree = ET.ElementTree(self.testsuite)
        tree.write(
            xml_path,
            pretty_print=True,
            xml_declaration=True
        )
        return True

    def set_testsuite_attr(self, **kwargs):
        if self.testsuite is None:
            return False
        for key, val in kwargs.items():
            self.testsuite.set(key, val)
        return True