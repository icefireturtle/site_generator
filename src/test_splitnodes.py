import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_split(self):
        node = TextNode("This is a **bold** text node", TextType.NORMAL)
        result = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(result, [TextNode("This is a ", TextType.NORMAL), TextNode("bold", TextType.BOLD), TextNode(" text node", TextType.NORMAL)])
    
if __name__ == "__main__":
    unittest.main()
