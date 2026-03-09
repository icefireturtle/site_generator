from blocktype import BlockType, block_to_block_type
from split_nodes import markdown_to_blocks
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode_to_htmlnode import text_node_to_html_node
from split_nodes import text_to_textnodes
from leafnode import LeafNode

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def markdown_to_html(md):
    blocks = markdown_to_blocks(md)
    block_list = []

    for block in blocks:
        type = block_to_block_type(block)
        
        
        match type:
            case BlockType.PARAGRAPH:
                cleaned_text = " ".join(block.split())
                children = text_to_children(cleaned_text)
                node = ParentNode("p", children)
                block_list.append(node)
            case BlockType.HEADING:
                heading_number = 0
                for char in block:
                    if char == "#":
                        heading_number += 1
                    else:
                        break
                text = block[heading_number + 1:]
                children = text_to_children(text)
                node = ParentNode(f"h{heading_number}", children)
                block_list.append(node)
            case BlockType.CODE:
                code_content = block.lstrip("`").lstrip("\n").rstrip("`")
                code_node = LeafNode("code", code_content)
                node = ParentNode("pre", [code_node])
                block_list.append(node)
            case BlockType.QUOTE:
                lines = block.split("\n")
                stripped_lines = []
                for line in lines:
                    if not line.startswith(">"):
                        raise ValueError("invalid quote block")
                    stripped_lines.append(line.lstrip(">").strip())
                cleaned_text = " ".join(stripped_lines)
                children = text_to_children(cleaned_text)
                node = ParentNode("blockquote", children)
                block_list.append(node)
            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                li_lines = []
                for line in lines:
                    line_content = line[2:]
                    li_lines.append(ParentNode("li", text_to_children(line_content)))
                node = ParentNode("ul", li_lines)
                block_list.append(node)
            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                li_lines = []
                for line in lines:
                    space_index = line.find(" ")
                    line_content = line[space_index + 1:]
                    li_lines.append(ParentNode("li", text_to_children(line_content)))
                node = ParentNode("ol", li_lines)
                block_list.append(node)

    return  ParentNode("div", block_list)