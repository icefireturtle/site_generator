from htmlnode import HTMLNode
from util import props_to_html

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        #print("LeafNode init props", props)
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        #print("self.props in to_html:", self.props)
        if self.value == None:
            raise ValueError("Must have a value")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            attributes = props_to_html(self.props) 
            #print("attributes string: ", attributes)
            return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"
        
