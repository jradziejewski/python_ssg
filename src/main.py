from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from utils import text_node_to_html_node


def main():
    link_node = TextNode("some link", TextType.LINKS, "https://www.google.com/")
    img_node = TextNode("some image", TextType.IMAGES, "https://example.com/image.png")

    print(text_node_to_html_node(link_node))
    print(text_node_to_html_node(img_node))


main()
