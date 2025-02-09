import unittest

from parentnode import ParentNode
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_basic_parent(self):
        nodehtml = ParentNode("div", [
            LeafNode("p", "Hello"),
            LeafNode("p", "World")
        ])
        result = nodehtml.to_html()
        self.assertEqual(result, "<div><p>Hello</p><p>World</p></div>")

    def test__parent(self):
        nodehtml = ParentNode("p",[LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),],)
        result = nodehtml.to_html()
        self.assertEqual(result, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_error_value(self):
        nodetohtml = ParentNode(None, [LeafNode("p", "dump")], None)
        with self.assertRaisesRegex(ValueError, "Parent Node missing value"):
            nodetohtml.to_html()
    
    def test_error_children(self):
        nodetohtml = ParentNode("P", None, None)
        with self.assertRaisesRegex(ValueError, "Parent Node missing children"):
            nodetohtml.to_html()

if __name__ == "__main__":
    unittest.main()