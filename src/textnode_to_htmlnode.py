from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        converted = LeafNode(None, text_node.text)
        return converted
    elif text_node.text_type == TextType.BOLD:
        converted = LeafNode("b", text_node.text)
        return converted
    elif text_node.text_type == TextType.ITALIC:
        converted = LeafNode("i", text_node.text)
        return converted
    elif text_node.text_type == TextType.CODE:
        converted = LeafNode("code", text_node.text)
        return converted
    elif text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise Exception("No Link Properties")
        link_props = {"href": text_node.url}
        converted = LeafNode("a", text_node.text, link_props)
        return converted
    elif text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise Exception("No Image Properties")
        image_props = {"src": text_node.url, "alt": text_node.text}
        converted = LeafNode("img", "", image_props)
        return converted
    else:
        raise Exception("Invalid TextNode TextType")