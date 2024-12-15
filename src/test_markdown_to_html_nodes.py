import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdowToHtmlNodes(unittest.TestCase):
    def test_big_document(self):
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
        expected_output = """<div><h1>This is a document</h1><p>It's a shitty document, but we'll use it as example.</p><ul><li>It has some unordered lists.</li><li>They make no sense.</li><li>But it's ok.</li></ul><ol><li>The</li><li>Ordered</li><li>List</li><li>Is</li><li>Also</li><li>Here.</li></ol><pre><blockquote> If a man knows not to which port he sails
 Or something like that, I don't remember

 <i>Seneca probably</i></blockquote></pre><p><i>Some italic</i> and <b>bold</b> text we can find here too!</p><pre><code>while True:
    do</code></pre><p>Here you go with some image: <img></img></p><p>And, of course, something to test
- a shitty block that
1. should be a paragraph
> but who knows what it's gonna be?</p></div>"""
        self.assertEqual(markdown_to_html_node(markdown_document).to_html(), expected_output)

if __name__ == "__main__":
    unittest.main()
