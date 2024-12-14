from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from utils import (
    split_nodes_image,
    split_nodes_link,
    text_node_to_html_node,
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes,
)


def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    print(text_to_textnodes(text))


main()
