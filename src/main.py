from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from copy_static import copy_static
import os
import shutil
import time
from generate_content import generate_pages

def main():
    node = TextNode("Stuff and things", TextType.ITALIC, "www.made_up_url.com")
    nodehtml = HTMLNode("p", "more stuff and things", None, {"href": "https://www.google.com", "target": "_blank"})
    print(HTMLNode.props_to_html(nodehtml))
    print(f"{node} \n {nodehtml}")


    public = "./public"
    static = "./static"
    content = "./content"

    old_public = os.path.exists(public)

    print(f"Old public exists: {old_public}")
    if old_public == True:
        print(f"removing old dir {public}")
        time.sleep(1)
        shutil.rmtree(public)
        print(f"complete")

    os.mkdir(public)

    copy_static(static, public)

    generate_pages(content, "./template.html", public)

    time.sleep(1)
    print(f"Happy Blank-Day")

if __name__ == "__main__":
    main()