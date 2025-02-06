import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This text node", TextType.BOLD)
        node2 = TextNode("This node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Silly beans", TextType.CODE, "www.fun.com")
        node2 = TextNode("Silly beans", TextType.CODE , "www.fun.com")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This seems a bit interesting", TextType.NORMAL, "www.some_url.com")
        node2 = TextNode("Well well well", TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()