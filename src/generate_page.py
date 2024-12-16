from copy_static import copy_static
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, destin_path):
    with open(from_path, "r") as file:
        markdown = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    with open(destin_path, "w") as index_html:
        index_html.write(full_html)
