import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType
from utils import split_nodes_delimiter, text_node_to_html_node


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

    def test_split_nodes_delimiter_single_bold(self):
        node = TextNode("This is another text with **bold** text", TextType.NORMAL_TEXT)

        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT),
            [
                TextNode("This is another text with ", TextType.NORMAL_TEXT, None),
                TextNode("bold", TextType.BOLD_TEXT, None),
                TextNode(" text", TextType.NORMAL_TEXT, None),
            ],
        )

    def test_split_nodes_delimiter_single_italic(self):
        node = TextNode("This is another text with *italic* text", TextType.NORMAL_TEXT)

        self.assertEqual(
            split_nodes_delimiter([node], "*", TextType.ITALIC_TEXT),
            [
                TextNode("This is another text with ", TextType.NORMAL_TEXT, None),
                TextNode("italic", TextType.ITALIC_TEXT, None),
                TextNode(" text", TextType.NORMAL_TEXT, None),
            ],
        )

    def test_split_nodes_delimiter_multiple(self):
        node = TextNode(
            "This is **bold** and this is also **bold**", TextType.NORMAL_TEXT
        )

        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT),
            [
                TextNode("This is ", TextType.NORMAL_TEXT, None),
                TextNode("bold", TextType.BOLD_TEXT, None),
                TextNode(" and this is also ", TextType.NORMAL_TEXT, None),
                TextNode("bold", TextType.BOLD_TEXT, None),
            ],
        )
