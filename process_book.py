#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse, os
from book import Book

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("book", help="Book to generate, where id is the directory where the book is located")
    args = parser.parse_args()

def write_or_return(s, file=None):
    if file is None:
        return s
    file.write(s)

def new_line(file=None, lines=1):
    return write_or_return(lines * '\n', file)

def new_page(file=None):
    return write_or_return('\\newpage\n', file)

def format_property(key, value):
    if value is None:
        return ''
    value = str(value)
    if '\n' in value:
        lines = value.split('\n')
        value = '|\n'
        for line in lines:
            value += '\t' + line + '\n'
    return '%s: %s' % (key, value)

def front_matter(description_key):
    meta = format_property('title', BOOK.title) + '\n'
    meta += format_property('author', BOOK.author) + '\n'
    meta += format_property('language', BOOK.language) + '\n'
    meta += format_property(description_key, BOOK.description)
    return meta

def format_cover():
    cover_string = ''
    if BOOK.cover:
        cover_string += '![](%s)\n' % BOOK.cover
    cover_string += new_page()
    cover_string += new_line()
    return cover_string

def format_chapter(chapter, last=False):
    chapter_string = '# %s\n\n' % chapter.title
    chapter_string += chapter.text
    chapter_string += new_line()
    if not last:
        chapter_string += new_line()
        chapter_string += new_page()
        chapter_string += new_line()
    return chapter_string

def generate(epub=False):
    filename = BOOK.id + ('-epub' if epub else '') + '.md'
    with BOOK.file(filename, 'w') as book:
        book.write('---\n')
        book.write(front_matter('description' if epub else 'abstract'))
        book.write('---\n')
        new_line(book)
        if not epub: # epub already have cover image as metadata
            book.write(format_cover())
        for i, chapter in enumerate(BOOK.chapters):
            book.write(format_chapter(chapter, last=(i == len(BOOK.chapters) - 1)))

if __name__ == "__main__":
    set_args()

    BOOK = Book(args.book)
    
    generate(epub=False)
    generate(epub=True)

    print(BOOK.get_links())