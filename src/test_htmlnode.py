import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(
            node.props_to_html(), 'href="https://www.google.com" target="_blank"'
        )

    def test_repr(self):
        node = HTMLNode(tag="a", value="b", children="c", props={"d"})

        self.assertEqual(node.__repr__(), "HTMLNode(a, b, c, {'d'})")

    def test_props_to_html_if_none(self):
        node = HTMLNode()

        self.assertEqual(node.props_to_html(), "")

    def test_leaf_inherits(self):
        node = LeafNode(tag="a", value="b")

        self.assertEqual(node.__repr__(), "LeafNode(a, b, None, None)")

    def test_leaf_to_html(self):
        node = LeafNode(tag="a", value="b")

        self.assertEqual(node.to_html(), "<a>b</a>")

    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_parent_to_html_with_parent_children(self):
        leaf_1 = LeafNode("b", "bold text")
        leaf_2 = LeafNode(None, "text")
        parent = ParentNode(
            "h1",
            [
                leaf_1,
                leaf_2,
                LeafNode("i", "italic text"),
                ParentNode("h2", [LeafNode("b", "bold"), LeafNode("i", "italic")]),
            ],
        )

        self.assertEqual(
            parent.to_html(),
            "<h1><b>bold text</b>text<i>italic text</i><h2><b>bold</b><i>italic</i></h2></h1>",
        )


if __name__ == "__main__":
    unittest.main()
