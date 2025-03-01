from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    print(f"HELLLLOOOO {old_nodes}")
    if old_nodes.text.count(delimiter) == 2:
        split_node = [x for x in old_nodes.text.split(delimiter) if x != delimiter + x + delimiter]
        print(f"HELLLLOOOO NEWWWW {split_node}")
        
    else:
        raise Exception("Invalid Markdown Syntax: Matching close delimiter missing")
    

