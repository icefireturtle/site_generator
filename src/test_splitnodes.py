import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

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

    def test_split_images(self):
        node = TextNode(
            "This is markdown text including an image and url with alt ![image](https://imgur.com/zZZZZZkqd.png) and another ![second image](https://imgur.com/elkZZZZZZzzkqc.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is markdown text including an image and url with alt ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://imgur.com/zZZZZZkqd.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode("second image", TextType.IMAGE, "https://imgur.com/elkZZZZZZzzkqc.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "Here is text with stinky links [google](https://google.com) and more googs [second google](https://google.com)", TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Here is text with stinky links ", TextType.NORMAL),
                TextNode("google", TextType.LINK, "https://google.com"),
                TextNode(" and more googs ", TextType.NORMAL),
                TextNode("second google", TextType.LINK, "https://google.com"),
            ],
            new_nodes,
        )

    def test_split_to_textnodes(self):
        new_nodes = text_to_textnodes("This is some **bold** text with _italics_ and `code` and an image ![image](https://imgur.com/zZZZZZkqd.png) and a link [google](https://google.com)")
        self.assertListEqual(
            [
                TextNode("This is some ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" text with ", TextType.NORMAL),
                TextNode("italics", TextType.ITALIC),
                TextNode(" and ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(" and an image ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://imgur.com/zZZZZZkqd.png"),
                TextNode(" and a link ", TextType.NORMAL),
                TextNode("google", TextType.LINK, "https://google.com"),
            ],
            new_nodes,
        )

    def test_split_to_textnodes(self):
        new_nodes = text_to_textnodes("Here is some _text_ that came with a linked [google](https://google.com) image ![image](https://imgur.com/AAAAAAAAfrqd.png) and some `code` that was **unexpected**")
        self.assertListEqual(
            [
                TextNode("Here is some ", TextType.NORMAL),
                TextNode("text", TextType.ITALIC),
                TextNode(" that came with a linked ", TextType.NORMAL),
                TextNode("google", TextType.LINK, "https://google.com"),
                TextNode(" image ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://imgur.com/AAAAAAAAfrqd.png"),
                TextNode(" and some ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(" that was ", TextType.NORMAL),
                TextNode("unexpected", TextType.BOLD),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
