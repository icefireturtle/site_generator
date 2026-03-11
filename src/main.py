from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from copy_static import copy_static
import os
import shutil
import time
import sys
from generate_content import generate_pages

def main():

    base_path = "/"

    if len(sys.argv) > 1:
        base_path = sys.argv[1]
        
    #public = "./public"
    docs = "./docs"
    static = "./static"
    content = "./content"

    #old_public = os.path.exists(public)
    old_docs = os.path.exists(docs)

    print(f"Old docs exists: {old_docs}")
    if old_docs == True:
        print(f"removing old dir {docs}")
        time.sleep(1)
        shutil.rmtree(docs)
        print(f"complete")

    os.mkdir(docs)

    copy_static(static, docs)

    generate_pages(content, "./template.html", docs, base_path)

    time.sleep(1)
    print(f"Happy Blank-Day")

if __name__ == "__main__":
    main()