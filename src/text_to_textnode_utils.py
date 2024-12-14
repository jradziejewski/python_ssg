import re
from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL_TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


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


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            result.append(node)
            continue
        images = extract_markdown_images(node.text)
        remaining_section = node.text

        if not images:
            result.append(TextNode(node.text, TextType.NORMAL_TEXT))

        for image in images:
            img_md = f"![{image[0]}]({image[1]})"
            sections = remaining_section.split(img_md, maxsplit=1)
            before = sections[0]
            after = sections[1]

            if before != "":
                result.append(TextNode(before, TextType.NORMAL_TEXT))
            result.append(TextNode(image[0], TextType.IMAGES, image[1]))

            remaining_section = after

        if len(images) != 0 and remaining_section != "":
            result.append(TextNode(remaining_section, TextType.NORMAL_TEXT))

    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            result.append(node)
            continue
        links = extract_markdown_links(node.text)
        remaining_section = node.text

        if not links:
            result.append(TextNode(node.text, TextType.NORMAL_TEXT))

        for link in links:
            link_md = f"[{link[0]}]({link[1]})"
            sections = remaining_section.split(link_md, maxsplit=1)
            before = sections[0]
            after = sections[1]

            if before != "":
                result.append(TextNode(before, TextType.NORMAL_TEXT))
            result.append(TextNode(link[0], TextType.LINKS, link[1]))

            remaining_section = after

        if len(links) != 0 and remaining_section != "":
            result.append(TextNode(remaining_section, TextType.NORMAL_TEXT))

    return result


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
