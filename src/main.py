from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    leaf_1 = LeafNode("b", "bold text")
    leaf_2 = LeafNode(None, "text")
    parent = ParentNode(
        "h1",
        [
            leaf_1,
            leaf_2,
            LeafNode("i", "italic text"),
            ParentNode("h2", [LeafNode("b", "bold"), LeafNode("i", "italic")]),
        ],
    )

    print(parent.to_html())


main()
