#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import base64
import lzma

from urllib.parse import quote_plus as url_encode

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("html", help="HTML file to publish")
    parser.add_argument("--name", help="Page name", default='')
    parser.add_argument("--shorten", help="Shorten generated URL with bit.ly", action='store_true')
    parser.add_argument("--bypass", help="Bypass size restriction (not recommended. only for debugging purposes)", action='store_true')
    args = parser.parse_args()

def publish(html_file, name='', short=False, bypass=False):
    name = url_encode(name)

    try:
        with open(html_file, 'r') as f:
            html = f.read()
    except (FileNotFoundError, IsADirectoryError) as e:
        print(e)
        exit()

    data = base64.b64encode(lzma.compress(bytes(html, encoding="utf-8"), format=lzma.FORMAT_ALONE, preset=9))

    url = f"https://itty.bitty.site/#{name}/{data.decode('utf-8')}"
    size = len(bytes(url, encoding="utf-8"))

    if size > 2048 and not bypass:
        print("Size too big to be published at https://itty.bitty.site/ (Maximum allowed: 2048 bytes)")
    elif short:
        from shorten import shorten
        print(shorten(url))
    else:
        print(url)
    print(f"{size} Bytes")

if __name__ == "__main__":
    set_args()

    publish(args.html, args.name, args.shorten, args.bypass)