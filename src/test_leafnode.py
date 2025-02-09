import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_basic_leaf(self):
        nodehtml = LeafNode(None, "Some text that might be fun")
        result = nodehtml.to_html()
        self.assertEqual(result, "Some text that might be fun")

    def test_basic_paragraph(self):
        nodehtml = LeafNode("p", "World Hi")
        result = nodehtml.to_html()
        self.assertEqual(result, "<p>World Hi</p>")

    def test_link_attributes(self):
        nodehtml = LeafNode("a", "Click Me", {"href": "https://google.com"})
        result = nodehtml.to_html()
        self.assertEqual(result, '<a href="https://google.com">Click Me</a>')

    def test_error(self):
        nodetohtml = LeafNode(None, None, None)
        with self.assertRaises(ValueError):
            nodetohtml.to_html()

if __name__ == "__main__":
    unittest.main()