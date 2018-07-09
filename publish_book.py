#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import argparse
import base64
import lzma
import os

from book import Book
from publish import publish
from urllib.parse import quote_plus as url_encode

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("book", help="Book to publish, where id is the directory where the book is located. Works only with very small books. For other purposes try to use GitHub pages or other available hosting services.")
    parser.add_argument("--shorten", help="Shorten generated URL with bit.ly", action='store_true')
    parser.add_argument("--bypass", help="Bypass size restriction (not recommended. only for debugging purposes)", action='store_true')
    args = parser.parse_args()

if __name__ == "__main__":
    set_args()

    book = Book(args.book)

    html_file = f"{args.book}/{args.book}.html"
    if not os.path.isfile(html_file):
        print(f"Build your book first with:\nmake html BOOK={args.book} OFFLINE=no")
    else:
        publish(html_file, book.title, args.shorten, args.bypass)