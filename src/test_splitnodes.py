import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is **bold** text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL)
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
        "This is some more text with **bold** and more **bold**", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is some more text with ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" and more ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
            ],
            new_nodes,
        )
    
    def test_delim_bold_multi(self):
        node = TextNode(
        "There are lots more **bolded words** where this comes from, **boldy**", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("There are lots more ", TextType.NORMAL),
                TextNode("bolded words", TextType.BOLD),
                TextNode(" where this comes from, ", TextType.NORMAL),
                TextNode("boldy", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_italics(self):
        node = TextNode(
            "There is text with **bold** and _italic_", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("There is text with ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )
        
    def test_delim_code(self):
        node = TextNode("This is text with `code block` in it", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" in it", TextType.NORMAL),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
