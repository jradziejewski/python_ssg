from htmlnode import LeafNode
from textnode import TextNode, TextType


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


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            result.append(node)
            continue

        remaining_text = node.text
        while True:
            opening = remaining_text.find(delimiter)
            if opening == -1:
                if len(remaining_text) != 0:
                    result.append(TextNode(remaining_text, TextType.NORMAL_TEXT))
                break

            closing = remaining_text.find(delimiter, opening + len(delimiter))
            if closing == -1:
                raise Exception("no matching delimiter")

            before = remaining_text[:opening]
            middle = remaining_text[opening + len(delimiter) : closing]
            after = remaining_text[closing + len(delimiter) :]

            if before:
                result.append(TextNode(before, TextType.NORMAL_TEXT))
            if middle:
                result.append(TextNode(middle, text_type))

            remaining_text = after
    return result
