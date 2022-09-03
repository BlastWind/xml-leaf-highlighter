import unittest

from xml_leaf_highlighter.main import extractXMLLeaves

class TestExtractXMLLeaves(unittest.TestCase):

    def test_find_child_uncollapsed_simple(self):
        xml = "<a></a>"
        self.assertEqual(extractXMLLeaves(xml), ["<a></a>"])

    def test_find_child_uncollapsed_nested(self):
        xml = "<b><a></a></b>"
        self.assertEqual(extractXMLLeaves(xml), ["<a></a>"])

    def test_find_multiple_child_uncollapsed_nested(self):
        xml = "<a><b>asdf</b><c>asd</c></a>"
        self.assertEqual(extractXMLLeaves(xml), ["<b>asdf</b>", "<c>asd</c>"])

    def test_find_multiple_child_uncollapsed_nested_two(self):
        xml = "<a><b>asdf<c id='cid'>a</c></b><c>asd</c></a>"
        self.assertEqual(extractXMLLeaves(xml), [
                         "<c id='cid'>a</c>", '<c>asd</c>'])

    def test_find_multiple_child_uncollapsed_nested_three(self):
        xml = "<a><b>asdf<c id='cid'><node>node</node></c></b><c>asd<node></node></c></a>"
        self.assertEqual(extractXMLLeaves(xml), [
                         "<node>node</node>", '<node></node>'])

    def test_find_child_collapsed_simple(self):
        xml = "<a/>"
        self.assertEqual(extractXMLLeaves(xml), ["<a/>"])

    def test_find_child_collapsed_nested(self):
        xml = "<b><a/></b>"
        self.assertEqual(extractXMLLeaves(xml), ["<a/>"])

    def test_find_multiple_child_collapsed(self):
        xml = "<a id='ok'/> <b attr1='asdf' attr2='bzxc'  /> <c/>"
        self.assertEqual(extractXMLLeaves(xml), [
                         "<a id='ok'/>", "<b attr1='asdf' attr2='bzxc'  />", "<c/>"])

    def test_find_multiple_child_collapsed_nested(self):
        xml = "<c><a id='ok'/></c><d><e><b attr1='asdf' attr2='bzxc'  /></e></d><c/>"
        self.assertEqual(extractXMLLeaves(xml), [
                         "<a id='ok'/>", "<b attr1='asdf' attr2='bzxc'  />", "<c/>"])

    def test_find_multiple_child_mixed(self):
        xml = "<a></a><b/><c/>"
        self.assertEqual(extractXMLLeaves(xml), ["<a></a>", "<b/>", "<c/>"])

    def test_find_multiple_child_mixed_nested(self):
        xml = "<e><a></a><b/><c/></e>"
        self.assertEqual(extractXMLLeaves(xml), ["<a></a>", "<b/>", "<c/>"])



if __name__ == '__main__':
    unittest.main()
