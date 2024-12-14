import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType
from utils import block_to_block_type, markdown_to_blocks, text_node_to_html_node


class TestUtils(unittest.TestCase):
    def test_text_node_to_html_node_for_text(self):
        text_node = TextNode("some text", TextType.NORMAL_TEXT, url=None)

        self.assertEqual(
            text_node_to_html_node(text_node), LeafNode(None, "some text", None)
        )

    def test_text_node_to_html_node_for_img(self):
        img_node = TextNode(
            "some image", TextType.IMAGES, "https://example.com/image.png"
        )

        self.assertEqual(
            text_node_to_html_node(img_node),
            LeafNode(
                "img", "", {"src": "https://example.com/image.png", "alt": "some image"}
            ),
        )

    def test_text_node_to_html_node_for_link(self):
        link_node = TextNode("some link", TextType.LINKS, "https://www.google.com/")

        self.assertEqual(
            text_node_to_html_node(link_node),
            LeafNode("a", "some link", {"href": "https://www.google.com/"}),
        )

    def test_block_to_block_type_code(self):
        block = "```\nthis is code block\n\n```"
        block_2 = "```this is not a code block```"

        self.assertEqual(block_to_block_type(block), "code")
        self.assertEqual(block_to_block_type(block_2), "paragraph")

    def test_block_to_block_type_heading(self):
        block = "# this is heading"
        block_2 = "#######this is not heading"
        block_3 = "##this is also not heading"

        self.assertEqual(block_to_block_type(block), "heading")
        self.assertEqual(block_to_block_type(block_2), "paragraph")
        self.assertEqual(block_to_block_type(block_3), "paragraph")

    def test_block_to_block_type_quote(self):
        block = "> this is quote"
        block_2 = "> this is also\n>some\n>quote"
        block_3 = "> this is\nnot a\n>quote"

        self.assertEqual(block_to_block_type(block), "quote")
        self.assertEqual(block_to_block_type(block_2), "quote")
        self.assertEqual(block_to_block_type(block_3), "paragraph")

    def test_block_to_block_type_ul(self):
        block = "* this is\n* unordered list"
        block_2 = "* this is\n- also a \n* unordered list"
        block_3 = "* this is\nnot a\n- unordered list"

        self.assertEqual(block_to_block_type(block), "unordered_list")
        self.assertEqual(block_to_block_type(block_2), "unordered_list")
        self.assertEqual(block_to_block_type(block_3), "paragraph")

    def test_block_to_block_type_ol(self):
        block = "1. this is\n2. ordered list"
        block_2 = "1. this is\n2. also a \n3. ordered list"
        block_3 = "1. this is\n2. not a\n4. ordered list"

        self.assertEqual(block_to_block_type(block), "ordered_list")
        self.assertEqual(block_to_block_type(block_2), "ordered_list")
        self.assertEqual(block_to_block_type(block_3), "paragraph")

    def test_markdown_to_blocks(self):

        markdown_text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        self.assertEqual(markdown_to_blocks(markdown_text), ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])

    def test_markdown_to_blocks_empty_lines(self):

        markdown_text = """# This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        self.assertEqual(markdown_to_blocks(markdown_text), ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])

    def test_markdown_to_blocks_traling_spaces(self):
        markdown_text = """# Heading

   
Paragraph with spaces before and after   
  
* List"""

        self.assertEqual(markdown_to_blocks(markdown_text), ["# Heading", "Paragraph with spaces before and after", "* List"])

    def test_markdown_to_blocks_trailing_newlines(self):
        markdown_text = """

# Heading

Paragraph

"""

        self.assertEqual(markdown_to_blocks(markdown_text), ["# Heading", "Paragraph"])
