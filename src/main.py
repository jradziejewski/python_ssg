import os
from copy_static import copy_static
from generate_page import generate_page_recursive

def main():
    print("Copying static files to public...")
    copy_static()

    print("Generating page...")
    generate_page_recursive("content", "template.html", os.path.join("./public"))

    print("Serving page...")
main()
