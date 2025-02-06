from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode("Stuff and things", TextType.ITALIC, "www.made_up_url.com")
    nodehtml = HTMLNode("p", "more stuff and things", None, {"href": "https://www.google.com", "target": "_blank"})
    print(HTMLNode.props_to_html(nodehtml))
    print(f"{node} \n {nodehtml}")



    print(f"Happy Blank-Day")

if __name__ == "__main__":
    main()