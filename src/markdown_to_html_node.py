from htmlnode import ParentNode
from text_to_textnode_utils import text_to_textnodes
from utils import block_to_block_type, markdown_to_blocks, text_node_to_html_node


def markdown_to_html_node(markdown):
    """
    A function that converts a full markdown document into a single parent HTMLNode.

    Parameters:
        markdown (string): A full markdown document.

    Returns:
        (HTMLNode): A parent-node, containing many child HTMLNode objects representing the nested elements.
    """

    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "paragraph":
            children.append(paragraph_to_html_node(block))
        elif block_type == "heading":
            children.append(heading_to_html_node(block))
        elif block_type == "code":
            children.append(code_to_html_node(block))
        elif block_type =="unordered_list":
            children.append(ul_to_html_node(block))
        elif block_type == "ordered_list":
            children.append(ol_to_html_node(block))
        elif block_type == "quote":
            children.append(quote_to_html_node(block))

    return ParentNode("div", children, None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    children = text_to_children(block)
    return ParentNode("p", children)

def ul_to_html_node(block):
    lines = block.split("\n")
    subnodes = []
    for line in lines:
        if line.startswith("*"):
            line = line.lstrip("* ")
        elif line.startswith("-"):
            line = line.lstrip("- ")
        children = text_to_children(line)
        subnodes.append(ParentNode("li", children))

    return ParentNode("ul", subnodes)

def ol_to_html_node(block):
    lines = block.split("\n")
    subnodes = []
    for line in lines:
        line_text = line[3:].strip()
        children = text_to_children(line_text)
        subnodes.append(ParentNode("li", children))

    return ParentNode("ol", subnodes)

def quote_to_html_node(block):
    lines = "\n".join(map(lambda x: x.lstrip(">").strip(), block.split("\n")))


    children = text_to_children(lines)
    quote = ParentNode("blockquote", children)
    return ParentNode("pre", [quote])

def heading_to_html_node(block):
    heading_num = len(block.split(r" ")[0])
    text = block.lstrip("#").strip()
    children = text_to_children(text)
    return ParentNode(f"h{heading_num}", children)

def code_to_html_node(block):
    text = "\n".join(block.split("\n")[1:-1])
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])
