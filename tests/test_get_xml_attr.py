import unittest

from main import getXMLNodeAttributeValue


class TestGetXMLAttr(unittest.TestCase):
    def test_get_bound_attr_on_collapsed_node(self):
        self.assertEqual(getXMLNodeAttributeValue(
            '<a bound="[0,0]"/>', "bound"), "[0,0]")

    def test_get_bound_attr_on_collapsed_node_spaced(self):
        self.assertEqual(getXMLNodeAttributeValue(
            '<a  bound="[0,0]" />', "bound"), "[0,0]")

    def test_get_bound_attr_on_uncollapsed_node(self):
        self.assertEqual(getXMLNodeAttributeValue(
            '<a bound="[1,1]"></a>', "bound"), "[1,1]")

    def test_get_bound_attr_on_uncollapsed_node_spaced(self):
        self.assertEqual(getXMLNodeAttributeValue(
            '<a  bound="[1,1]" >< /  a>', "bound"), "[1,1]")

    def test_get_bound_attr_when_there_are_none(self):
        self.assertEqual(getXMLNodeAttributeValue(
            '<a  foo="haha" >< /  a>', "bound"), "")


if __name__ == '__main__':
    unittest.main()
