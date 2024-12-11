from textnode import TextNode, TextType


def main():
    node = TextNode("This is a test node", TextType.BOLD_TEXT, "https://boot.dev/")
    print(node)


main()
