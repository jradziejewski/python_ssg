import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType
from utils import markdown_to_blocks, text_node_to_html_node


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
