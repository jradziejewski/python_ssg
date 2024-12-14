from utils import markdown_to_blocks


def main():
    markdown_text = """# This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item
"""
    markdown_text = """

# Heading

Paragraph

"""    
    blocks = markdown_to_blocks(markdown_text)
    print(blocks)

main()
