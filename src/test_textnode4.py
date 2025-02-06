import unittest

from textnode import TextNode, TextType

class TestTexNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This seems a bit interesting", TextType.NORMAL, "www.some_url.com")
        node2 = TextNode("Well well well", TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()