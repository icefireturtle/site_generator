from textnode import TextNode, TextType

def main():
    node = TextNode("Stuff and things", TextType.ITALIC, "www.made_up_url.com")
    print(node)

    print(f"Happy Blank-Day")

if __name__ == "__main__":
    main()