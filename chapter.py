import yaml
import string, re
from get_property import *
from os import listdir
from os.path import join, isdir, abspath

class Chapter:

    NEXT_REGEX = re.compile(r'\(\s*([^\)]*?)\s*->\s*\[\s*(.*?)\s*\]\s*\)',re.S|re.M)

    def __init__(self, book, id):
        self.book = book
        self.id = id
        metadata_file = self.file(self.id + '.yml')
        metadata = yaml.load(metadata_file)
        metadata_file.close()
        self.title = property(metadata, 'title')
        self.text = self.file(self.id + '.md').read()

    def parse_children(self):
        def next_replacement(match):
            (next_text, next_id) = match.groups()
            if not self.book.exists_chapter(next_id):
                error('Broken link. Chapter "%s" not found (required in %s.md at ":%s -> %s:")' % (next_id, self.id, next_id, next_text))
            self.children.add(next_id)
            chapter = self.book.get_chapter(next_id)
            return self.book.child_formatter(chapter.id, next_text, self.__header_markdown_reference(chapter.title))
        self.children = set()
        self.text = re.sub(Chapter.NEXT_REGEX, next_replacement, self.text)

    def __header_markdown_reference(self, text):
        lower_no_punctuation = ''.join([c for c in text if c not in string.punctuation]).strip().lower()
        return re.sub(r'\s', '-', lower_no_punctuation)

    def file(self, chapter_file, mode='r'):
        return self.book.file(join(self.id, chapter_file), mode)
