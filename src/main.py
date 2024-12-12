from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from utils import text_node_to_html_node, split_nodes_delimiter


def main():
    node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
    node2 = TextNode("This is another text with **bold** text", TextType.NORMAL_TEXT)
    node3 = TextNode("This has no delimiters", TextType.NORMAL_TEXT)
    node4 = TextNode("This is **bold** and this is also **bold**", TextType.NORMAL_TEXT)
    new_nodes = split_nodes_delimiter([node2], "**", TextType.BOLD_TEXT)
    new_nodes2 = split_nodes_delimiter([node4], "**", TextType.BOLD_TEXT)

    print(new_nodes)
    print(new_nodes2)


main()
