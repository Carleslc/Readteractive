#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse, os, re
from book import Book

FORMAT = None

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
    if not value:
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
        cover_string += '<figure>![](%s)</figure>\n' % BOOK.cover
    cover_string += new_page()
    cover_string += new_line()
    return cover_string

def format_description():
    description = re.sub(r'[\t\n]', ' ', BOOK.description)
    return '<p class="description">%s</p>\n' % description

def format_chapter(chapter, format, last=False):
    visibility = 'style="display: none"' if format == 'html' and BOOK.start != chapter.id else ''
    chapter_string = '<div id="chapter_%s"%s>\n\n' % (chapter.id, visibility)
    chapter_string += '# %s\n\n' % chapter.title
    chapter_string += chapter.text
    chapter_string += new_line()
    if not last:
        chapter_string += new_line()
        chapter_string += new_page()
        chapter_string += new_line()
    chapter_string += '</div>\n'
    return chapter_string

def child_formatter(id, text, title):
    return '(<span onclick="show_chapter(\'chapter_%s\')">[**%s**](#%s)</span>)' % (id, text, title)

def generate(format):
    filename = '%s-%s.md' % (BOOK.id, format)
    with BOOK.file(filename, 'w') as book:
        book.write('---\n')
        book.write(front_matter('abstract' if format == 'pdf' else 'description'))
        book.write('\n---\n')
        if format == 'html':
            book.write('<script type="text/javascript" src="show_chapter.js"/>\n')
            chapters = ['"chapter_%s"' % chapter.id for chapter in BOOK.chapters]
            book.write('<script type="text/javascript">chapters([%s])</script>\n' % ','.join(chapters))
        new_line(book)
        if format != 'pdf':
            book.write(format_description())
        if format != 'epub': # epub already have cover image as metadata
            book.write(format_cover())
        for i, chapter in enumerate(BOOK.chapters):
            book.write(format_chapter(chapter, format, last=(i == len(BOOK.chapters) - 1)))
        book.write('\\tableofcontents')

if __name__ == "__main__":
    set_args()

    BOOK = Book(args.book, child_formatter)
    
    generate('html')
    generate('pdf')
    generate('epub')

    print(BOOK.get_links())