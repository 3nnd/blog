# coding: utf-8

import os
import re
import operator

POSTS_DIR = "articles"
README_FILENAME = "./README.md"


def gen_catalog():
    r = re.compile(r"(\d{4}_\d{2}_\d{2})-.+\..+")  # e.g. 2014_06_17-use_cron.rst, 2014_06_17-use_cron.md

    catalog = []
    for filename in os.listdir(POSTS_DIR):
        result = r.match(filename)
        if result:
            date = result.group(1).replace("_", "/")
            with open(os.path.join(POSTS_DIR, filename)) as f:
                title = f.readline().strip()
                if filename.split(".")[-1] == "md":
                    title = title.lstrip("# ")
            catalog.append((title, date, filename))

    catalog = sorted(catalog, key=operator.itemgetter(2), reverse=True)  # sort by filename, in a reverse order

    with open(README_FILENAME, "r+") as f:
        # clear all the contents in file
        f.truncate()

        # write title, aboutme
        f.write("# Jiajun's Blog\n\n")
        f.write("会当凌绝顶，一览众山小。\n\n")
        f.write("## 关于我\n")
        f.write(
            "[点我]({posts_dir}/aboutme.md)\n\n".format(
                posts_dir=POSTS_DIR,
            )
        )
        f.write("## 目录\n\n")

        # write catalog
        for item in catalog:
            title, date, filename = item
            f.write(
                "- {date} - [{title}]({posts_dir}/{filename})\n".format(
                    date=date,
                    title=title,
                    posts_dir=POSTS_DIR,
                    filename=filename,
                )
            )

        # append LICENSE
        f.write("\n")
        f.write("--------------------------------------------\n\n")
        f.write("[CC-BY](http://opendefinition.org/licenses/cc-by/)\n")


if __name__ == "__main__":
    gen_catalog()
