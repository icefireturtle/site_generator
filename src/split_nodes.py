from textnode import TextNode, TextType
from regex import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        section = old_node.text.split(delimiter)

        if len(section) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        
        for i in range(len(section)):
            if section[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(section[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(section[i], text_type))

        new_nodes.extend(split_nodes)
        
    return new_nodes    

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:

        extract = list(extract_markdown_images(old_node.text))
        
        if not extract:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text

        for image_alt, image_link in extract:
            section = text.split(f"![{image_alt}]({image_link})", 1)
            
            if section[0]:
                new_nodes.append(TextNode(section[0], old_node.text_type))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

            if len(section) > 1:
                text = section[1]
            else:
                text = ""
        
        if text:
            new_nodes.append(TextNode(text, old_node.text_type))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:

        extract = list(extract_markdown_links(old_node.text))
        
        if not extract:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text

        for link_text, link_url in extract:
            section = text.split(f"[{link_text}]({link_url})", 1)
            
            if section[0]:
                new_nodes.append(TextNode(section[0], old_node.text_type))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            if len(section) > 1:
                text = section[1]
            else:
                text = ""
        
        if text:
            new_nodes.append(TextNode(text, old_node.text_type))

    return new_nodes