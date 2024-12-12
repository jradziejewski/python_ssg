import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")

    def test_repr(self):
        node = HTMLNode(tag="a", value="b", children="c", props={"d"})

        self.assertEqual(node.__repr__(), "HTMLNode(a, b, c, {\'d\'})")

    def test_props_to_html_if_none(self):
        node = HTMLNode()

        self.assertEqual(node.props_to_html(), "")

    def test_leaf_inherits(self):
        node = LeafNode(tag="a", value="b")

        self.assertEqual(node.__repr__(), "LeafNode(a, b, None, None)")

    def test_leaf_to_html(self):
        node = LeafNode(tag="a", value="b")

        self.assertEqual(node.to_html(), "<a>b</a>")

if __name__ == "__main__":
    unittest.main()

