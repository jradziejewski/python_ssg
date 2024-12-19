import os
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

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)

    for content in contents:
        path_to_content = os.path.join(dir_path_content, content)
        if os.path.isfile(path_to_content):
            generate_page(path_to_content, template_path, os.path.join(dest_dir_path, "index.html"))
            
        elif os.path.isdir(path_to_content):
            os.mkdir(os.path.join(dest_dir_path, content))
            generate_page_recursive(path_to_content, template_path, os.path.join(dest_dir_path, content))
