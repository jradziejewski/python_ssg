import os
import shutil

def copy_static(source_dir="./static", destin_dir="./public", path=""):
    """
    Recursive function that copies all the contents from a source directory to a destination directory
    """

    current_source = os.path.join(source_dir, path)
    current_destination = os.path.join(destin_dir, path)

    if path == "" and os.path.exists(destin_dir):
        shutil.rmtree(destin_dir)
    os.makedirs(destin_dir, exist_ok=True)

    contents = os.listdir(current_source)

    files_to_copy = []
    for content in contents:
        path_to_content = os.path.join(current_source, content)

        if os.path.isfile(path_to_content):
            files_to_copy.append(path_to_content)
        elif os.path.isdir(path_to_content):
            os.mkdir(os.path.join(current_destination, content))
            copy_static(source_dir, destin_dir, path=os.path.join(path, content))


    for file in files_to_copy:
        shutil.copy(file, current_destination)
