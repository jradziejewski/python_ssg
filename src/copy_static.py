import os
import shutil

SOURCE_DIR = "./static"
DESTIN_DIR = "./public"

def copy_static(path=""):
    """
    Recursive function that copies all the contents from a source directory to a destination directory
    """

    current_source = os.path.join(SOURCE_DIR, path)
    current_destination = os.path.join(DESTIN_DIR, path)

    if path == "" and os.path.exists(DESTIN_DIR):
        shutil.rmtree(DESTIN_DIR)
    os.makedirs(DESTIN_DIR, exist_ok=True)

    contents = os.listdir(current_source)

    files_to_copy = []
    for content in contents:
        path_to_content = os.path.join(current_source, content)

        if os.path.isfile(path_to_content):
            files_to_copy.append(path_to_content)
        elif os.path.isdir(path_to_content):
            os.mkdir(os.path.join(current_destination, content))
            copy_static(os.path.join(path, content))


    for file in files_to_copy:
        shutil.copy(file, current_destination)
