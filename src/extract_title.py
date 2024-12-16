def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").strip()

    raise Exception("No h1 header found")
