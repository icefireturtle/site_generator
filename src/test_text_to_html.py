import unittest

from textnode_to_htmlnode import text_node_to_html_node
from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestTexttoHTML(unittest.TestCase):

    def normal_conversion_test(self):
        node = TextNode("This is cool", TextType.NORMAL)
        result = text_node_to_html_node(node)
        self.assertEqual(result.value, "This is cool")
    
    def bold_conversion_test(self):
        node = TextNode("This is BOLD", TextType.BOLD)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "b")
        self.assertEqual(result.value, "This is BOLD")
        
    def italic_conversion_test(self):
        node = TextNode("This is ITALIC", TextType.ITALIC)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "i")
        self.assertEqual(result.value, "This is ITALIC")
        
    def code_conversion_test(self):
        node = TextNode("This is CODE", TextType.CODE)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "code")
        self.assertEqual(result.value, "This is CODE")
        
    def link_conversion_test(self):
        node = TextNode("This is LINK", TextType.LINK, "https://google.com")
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "a")
        self.assertEqual(result.value, "This is LINK")
        self.assertEqual(result.props, {"href": "https://google.com"})
        
    def image_conversion_test(self):
        node = TextNode("This is IMAGE", TextType.IMAGE, "https://google.com")
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "img")
        self.assertEqual(result.value, "")
        self.assertEqual(result.props, {"src": "https://google.com", "alt": "This is IMAGE"})
        
    def error_bad_value_test(self):
        node = TextNode("This is ERROR", "SUPER")
        with self.assertRaisesRegex(Exception, "Invalid TextNode TextType"): text_node_to_html_node(node)

    def error_with_none_test(self):
        node = TextNode("This is ERROR", None)
        with self.assertRaisesRegex(Exception, "Invalid TextNode TextType"): text_node_to_html_node(node)

    def error_with_invalid_type_test(self):
        node = TextNode("This is ERROR", 999)
        with self.assertRaisesRegex(Exception, "Invalid TextNode TextType"): text_node_to_html_node(node)

    def missing_image_props_test(self):
        node = TextNode("", TextType.IMAGE, None)
        with self.assertRaises(Exception): text_node_to_html_node(node)

    def bold_missing_props_test(self):
        node = TextNode("Bold Node", TextType.BOLD)
        result = text_node_to_html_node(node)
        self.assertFalse(hasattr(result, 'props'))  # props shouldn't exist for BOLD nodes

if __name__ == "__main__":
    unittest.main()