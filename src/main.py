import os
from copy_static import copy_static
from generate_page import generate_page

def main():
    print("Copying static files to public")
    copy_static()

    print("Generating page")
    generate_page("content/index.md", "template.html", os.path.join("./public", "index.html"))

main()
