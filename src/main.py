from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode


def main():
    node = TextNode("This is a test node", TextType.BOLD_TEXT, "https://boot.dev/")
    htmlnode = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(htmlnode.props_to_html())
    print(htmlnode)

    leaf = LeafNode("a", value="Dupa")

    print(leaf.to_html())


main()
