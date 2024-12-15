from markdown_to_html_node import markdown_to_html_node
from utils import block_to_block_type


def main():
    markdown_document = """# This is a document

It's a shitty document, but we'll use it as example.

- It has some unordered lists.
- They make no sense.
- But it's ok.

1. The
2. Ordered
3. List
4. Is
5. Also
6. Here.

> If a man knows not to which port he sails
> Or something like that, I don't remember
>
> *Seneca probably*

*Some italic* and **bold** text we can find here too!

```python
while True:
    do
```

Here you go with some image: ![some dumb image](https://not-even-an-image.dev/not-image.png)

And, of course, something to test
- a shitty block that
1. should be a paragraph
> but who knows what it's gonna be?
"""
    test = markdown_to_html_node(markdown_document)
    print(test.to_html())

main()
