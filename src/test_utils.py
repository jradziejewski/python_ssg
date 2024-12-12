import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType
from utils import text_node_to_html_node


class TestUtils(unittest.TestCase):
    def test_text_node_to_html_node_for_text(self):
        text_node = TextNode(
            "some text", TextType.NORMAL_TEXT, url=None
        )

        self.assertEqual(text_node_to_html_node(text_node), LeafNode(None, "some text", None))

    def test_text_node_to_html_node_for_img(self):
        img_node = TextNode(
            "some image", TextType.IMAGES, "https://example.com/image.png"
        )

        self.assertEqual(
            text_node_to_html_node(img_node),
            LeafNode("img", "", {'src': 'https://example.com/image.png', 'alt': 'some image'})
        )

    def test_text_node_to_html_node_for_link(self):
        link_node = TextNode("some link", TextType.LINKS, "https://www.google.com/")

        self.assertEqual(
            text_node_to_html_node(link_node),
            LeafNode("a", "some link", {"href": "https://www.google.com/"}),
        )
