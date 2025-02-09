from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent Node missing value")
        if self.children == None:
            raise ValueError("Parent Node missing children")
        html_string = ""
        for child in self.children:
            childnode = child.to_html()
            html_string += childnode
        return f"<{self.tag}>{html_string}</{self.tag}>"