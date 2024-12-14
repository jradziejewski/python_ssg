import unittest
from textnode import TextNode, TextType
from text_to_textnode_utils import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_links,
    extract_markdown_images,
    text_to_textnodes,
)


class TestUtils(unittest.TestCase):
    def test_text_to_textnodes_no_images_links(self):
        text = "This is **text** with an *italic* word and a `code block`"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.NORMAL_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.NORMAL_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.NORMAL_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
            ],
        )

    def test_text_to_textnodes_images_links(self):
        text = "This is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is an ", TextType.NORMAL_TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.NORMAL_TEXT),
                TextNode("link", TextType.LINKS, "https://boot.dev"),
            ],
        )

    def test_text_to_textnodes_all(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.NORMAL_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.NORMAL_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.NORMAL_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" and an ", TextType.NORMAL_TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.NORMAL_TEXT),
                TextNode("link", TextType.LINKS, "https://boot.dev"),
            ],
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

    def test_extract_markdown_images_single(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"

        self.assertEqual(
            extract_markdown_images(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")],
        )

    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_extract_markdown_links_single(self):
        text = "This is text with a link [to example](https://www.example.com)"

        self.assertEqual(
            extract_markdown_links(text),
            [
                ("to example", "https://www.example.com"),
            ],
        )

    def test_extract_markdown_links_multiple(self):
        text = "This is text with a link [to example](https://www.example.com) and [to youtube](https://www.youtube.com)"

        self.assertEqual(
            extract_markdown_links(text),
            [
                ("to example", "https://www.example.com"),
                ("to youtube", "https://www.youtube.com"),
            ],
        )

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an image ![example image](https://www.example.com/example.img) and another image ![on youtube](https://www.youtube.com/image.png) asdf",
            TextType.NORMAL_TEXT,
        )

        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode(
                    "This is text with an image ",
                    TextType.NORMAL_TEXT,
                ),
                TextNode(
                    "example image",
                    TextType.IMAGES,
                    "https://www.example.com/example.img",
                ),
                TextNode(" and another image ", TextType.NORMAL_TEXT),
                TextNode(
                    "on youtube", TextType.IMAGES, "https://www.youtube.com/image.png"
                ),
                TextNode(" asdf", TextType.NORMAL_TEXT),
            ],
        )

    def test_split_nodes_image_with_link(self):
        node = TextNode(
            "This is text with a link [to example](https://www.example.com) and [to youtube](https://www.youtube.com/@bootdotdev) asdf",
            TextType.NORMAL_TEXT,
        )

        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode(
                    "This is text with a link [to example](https://www.example.com) and [to youtube](https://www.youtube.com/@bootdotdev) asdf",
                    TextType.NORMAL_TEXT,
                )
            ],
        )

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to example](https://www.example.com) and [to youtube](https://www.youtube.com/@bootdotdev) asdf",
            TextType.NORMAL_TEXT,
        )

        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode(
                    "This is text with a link ",
                    TextType.NORMAL_TEXT,
                ),
                TextNode("to example", TextType.LINKS, "https://www.example.com"),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode(
                    "to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"
                ),
                TextNode(" asdf", TextType.NORMAL_TEXT),
            ],
        )

    def test_split_nodes_link_with_image(self):
        node = TextNode(
            "This is text with an image ![example image](https://www.example.com/example.img) and another image ![on youtube](https://www.youtube.com/image.png) asdf",
            TextType.NORMAL_TEXT,
        )

        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode(
                    "This is text with an image ![example image](https://www.example.com/example.img) and another image ![on youtube](https://www.youtube.com/image.png) asdf",
                    TextType.NORMAL_TEXT,
                )
            ],
        )
