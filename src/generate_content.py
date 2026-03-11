import os
import time

from pathlib import Path

from markdown_to_html import markdown_to_html

def extract_title(md):
    md_lines = md.split("\n")
    for line in md_lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown file")

def generate_pages(from_path, template_path, dest_path):
    
    dir_list = os.listdir(from_path)
    
    for copy in dir_list:

        copy_path = os.path.join(from_path, copy)
        copy_destination = os.path.join(dest_path, copy)

        is_file = os.path.isfile(copy_path)

        if is_file == True:
            print(f"copying {copy}...")
            copy_extension = Path(copy_destination).with_suffix(".html")
            contents = open(copy_path).read()
            node = markdown_to_html(contents)
            html_content = node.to_html()

            title = extract_title(contents)

            template = open(template_path).read()

            print(f"Generating page from {from_path} to {copy_destination} using template {template_path}")

            with open (copy_extension, "w") as f:
                f.write(template.replace("{{ Title }}", title).replace("{{ Content }}", html_content))

            time.sleep(1)
        else:
            copy_destination = os.path.join(dest_path, copy)
            print(f"creating destination {copy_destination}...")
            os.mkdir(copy_destination)
            generate_pages(copy_path, template_path, copy_destination)