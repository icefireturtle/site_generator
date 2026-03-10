import os

from markdown_to_html import markdown_to_html

def extract_title(md):
    md_lines = md.split("\n")
    for line in md_lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown file")

def generate_page(from_path, template_path, dest_path):

    contents = open(from_path).read()
    node = markdown_to_html(contents)
    html_content = node.to_html()

    title = extract_title(contents)
    dir_path = os.path.dirname(dest_path)

    os.makedirs(dir_path, exist_ok=True)

    template = open(template_path).read()

    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")

    with open (dest_path, "w") as f:
        f.write(template.replace("{{ Title }}", title).replace("{{ Content }}", html_content))
