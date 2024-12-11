import unittest

from textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("test", TextType.BOLD_TEXT, "url")
        node2 = TextNode("test", TextType.BOLD_TEXT, "url")

        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("test", TextType.ITALIC_TEXT, "url")

        self.assertEqual(node.__repr__(), "TextNode(test, italic, url)")

    def test_diff(self):
        node = TextNode("test", TextType.BOLD_TEXT, "url")
        node2 = TextNode("test", TextType.BOLD_TEXT, "different url")

        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
