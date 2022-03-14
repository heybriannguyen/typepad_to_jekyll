#!/usr/bin/env python3

from datetime import datetime
import sys


# Makes markdown files for each post in the import file
def make_posts(import_file):
    # Flag to write post's body
    canWrite = False
    f_name = ""
    f_matter = {
        "AUTHOR": "",
        "TITLE": "",
        "STATUS": "",
        "DATE": "",
        "BASENAME": "",
    }
    categories = []
    body = """"""

    with open(import_file, "r") as f_r:
        for line in f_r:
            if line.startswith(tuple(f_matter)):
                f_matter[line.split(": ")[0]] = line.split(": ")[1].strip("\n")
            elif line.startswith("CATEGORY:"):
                categories.append(line.split("CATEGORY: ")[1].strip("\n"))
            elif line.startswith("BODY:"):
                f_name = write_f_name(f_matter)
                write_f_matter(f_name, f_matter, categories)
                canWrite = True
            elif line == "-----\n":
                # Skip ----- line at the EOF
                continue
            elif line.startswith("EXTENDED BODY:"):
                canWrite = False
                write_body(body, f_name)
                # Prepares loop for new post and its categories
                body = """"""
                categories.clear()
            elif canWrite:
                body += line


# Writes the filename
def write_f_name(f_matter):
    return (
        f"""{f_matter['DATE'][6:10]}"""  # Year
        + f"""-{f_matter['DATE'][:2]}"""  # Month
        + f"""-{f_matter['DATE'][3:5]}"""  # Day
        + f"""-{f_matter['BASENAME']}.md"""  # Filename
    )


# Writes at the top of the Markdown file
def write_f_matter(f_name, f_matter, categories):
    with open(f_name, "w") as f_w:
        f_w.write(
            f"""---\n"""
            + f"""layout: post\n"""
            + f"""author: {f_matter['AUTHOR']}\n"""
            + f"""title: {f_matter['TITLE']}\n"""
            + f"""status: {f_matter['STATUS']}\n"""
            + f"""categories: {categories}\n"""
            + f"""date: {f_name[:10]}\n"""
            + f"""---\n\n"""
        )


# Writes the body
def write_body(body, f_name):
    with open(f_name, "a") as f_w:
        f_w.write(body)


if __name__ == "__main__":
    start_time = datetime.now()
    make_posts(str(sys.argv[1]))
    print(datetime.now() - start_time)
