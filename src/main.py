from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from utils import (
    split_nodes_image,
    split_nodes_link,
    text_node_to_html_node,
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)


def main():
    node = TextNode(
        "This is text with an image [to boot dev](https://www.boot.dev/image.img) and [to youtube](https://www.youtube.com/@bootdotdev) asdf",
        TextType.NORMAL_TEXT,
    )

    print(split_nodes_link([node]))


main()
