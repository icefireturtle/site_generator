import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props(self):
        nodehtml = HTMLNode("h1", "bargin bobs diner", None, {"href": "https://www.fake_url.com"})
        result = nodehtml.props_to_html()
        self.assertEqual(result, ' href="https://www.fake_url.com"')

    def test_props2(self):
        nodehtml = HTMLNode("a", "wowow", None, {"href": "https://www.another.com", "target": "_blank"})
        result = nodehtml.props_to_html()
        self.assertEqual(result, ' href="https://www.another.com" target="_blank"')

    def test_props3(self):
        nodehtml = HTMLNode("h4", "cool", None, None)
        result = nodehtml.props_to_html()
        self.assertEqual(result, "")

    def test_error(self):
        nodehtml = HTMLNode("a", "wowow", None, {"href": "https://www.another.com"})
        with self.assertRaises(NotImplementedError):
            nodehtml.to_html()

if __name__ == "__main__":
    unittest.main()