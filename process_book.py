#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse, re
from book import Book

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("book", help="Book to generate, where id is the directory where the book is located")
    parser.add_argument("format", help="Format to build the book")
    parser.add_argument("--printed", help="Add chapter number references for printed books", default='no')
    parser.add_argument("--scroll", help="Set scrolling instead section replacement for online books", default='no')
    args = parser.parse_args()

    args.printed = yes_no(args.printed)
    args.scroll = yes_no(args.scroll)

def yes_no(arg):
    return arg == 'yes'

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

def format_github_corner():
    if not BOOK.github:
        return ''
    return (
        '<a href="%s" class="github-corner" aria-label="Fork me on GitHub">'
        '<svg width="80" height="80" viewBox="0 0 250 250" style="fill:#aa0000; color:#fff; position: fixed; top: 0; border: 0; right: 0; z-index: 100;" aria-hidden="true">'
        '<path d="M0,0 L115,115 L130,115 L142,130 L250,250 L250,0 Z"></path>'
        '<path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>'
        '<path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path>'
        '</svg></a>'
        '<style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}'
        '@keyframes octocat-wave{0%%,100%%{transform:rotate(0)}20%%,60%%{transform:rotate(-25deg)}40%%,80%%{transform:rotate(10deg)}}'
        '@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style>\n'
    ) % BOOK.github

def format_description():
    description = re.sub(r'[\t\n]', ' ', BOOK.description)
    return '<p class="description">%s</p>\n' % description

def format_chapter(chapter, format, last=False):
    visibility = 'style="display: none"' if format == 'html' and BOOK.start != chapter.id else ''
    chapter_string = '<div id="chapter_%s"%s>\n\n' % (chapter.id, visibility)
    page = '[%s] ' % chapter.order if args.printed and chapter.order != None else ''
    chapter_string += '# %s%s\n\n' % (page, chapter.title)
    chapter_string += chapter.text
    chapter_string += new_line()
    if not last:
        chapter_string += new_line()
        chapter_string += new_page()
        chapter_string += new_line()
    chapter_string += '</div>\n'
    return chapter_string

def child_formatter(id, text, title, order):
    page = ' [%s]' % order if args.printed and order != None else ''
    scroll = str(args.scroll).lower()
    return '(<span onclick="show_chapter(\'chapter_%s\', %s)">[**%s**%s](#%s)</span>)' % (id, scroll, text, page, title)

def build(format):
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
        if format == 'html':
            book.write(format_github_corner())
        for i, chapter in enumerate(BOOK.chapters):
            book.write(format_chapter(chapter, format, last=(i == len(BOOK.chapters) - 1)))
        new_page(book)
        book.write('\\tableofcontents')

if __name__ == "__main__":
    set_args()

    BOOK = Book(args.book, child_formatter)
    
    build(args.format)

    print(BOOK.get_links())