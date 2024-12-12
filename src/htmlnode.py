class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        if self.props is None:
            return ""

        for key, val in self.props.items():
            result += f'{key}="{val}" '

        return result.rstrip()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError

        if self.tag == None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag must be provided")
        if self.children == None:
            raise ValueError("children must be provided")

        child_str = ""
        for child in self.children:
            child_str += child.to_html()

        return f"<{self.tag}>{child_str}</{self.tag}>"
