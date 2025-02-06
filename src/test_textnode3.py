import unittest

from textnode import TextNode, TextType

class TestTexNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Silly beans", TextType.CODE, "www.fun.com")
        node2 = TextNode("Silly beans", TextType.CODE , "www.fun.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()