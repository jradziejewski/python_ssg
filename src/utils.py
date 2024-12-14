import re
from htmlnode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise TypeError("text node type is invalid")

def markdown_to_blocks(markdown):
    """
    A function that takes raw Markdown string and returns a list of "block" strings.

    Parameters:
        markdown (string): raw Markdown string representing a full document

    Returns:
        (list): a list of "block" strings
    """

    return list(filter(lambda x: x != "", map(lambda x: x.strip(), re.split(r"\n\s*\n", markdown))))
