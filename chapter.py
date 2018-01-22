import yaml
import string, re
from get_property import *
from os import listdir
from os.path import join, isdir, abspath

class Chapter:

    ID_PREFIX = re.compile(r'^\d*[-_]?',re.S)
    NEXT_REGEX = re.compile(r'\(\s*([^\)]*?)\s*->\s*\[\s*(.*?)\s*\]\s*\)',re.S|re.M)

    def __init__(self, book, full_id):
        self.book = book
        self.full_id = full_id
        self.id = Chapter.format_id(full_id)
        metadata_file = self.file(self.full_id + '.yml')
        metadata = yaml.load(metadata_file)
        metadata_file.close()
        self.title = property(metadata, 'title')
        self.text = self.file(self.full_id + '.md').read()

    def parse_children(self):
        def next_replacement(match):
            (next_text, next_id) = match.groups()
            id_no_prefix = Chapter.format_id(next_id)
            if not self.book.exists_chapter(id_no_prefix):
                error('Broken link. Chapter "%s" not found and required in %s at "(%s -> [%s])"' % (next_id, self.id, next_text, next_id))
            self.children.add(id_no_prefix)
            chapter = self.book.get_chapter(id_no_prefix)
            return self.book.child_formatter(chapter.id, next_text, self.__header_markdown_reference(chapter.title))
        self.children = set()
        self.text = re.sub(Chapter.NEXT_REGEX, next_replacement, self.text)

    def __header_markdown_reference(self, text):
        lower_no_punctuation = ''.join([c for c in text if c not in string.punctuation]).strip().lower()
        return re.sub(r'\s', '-', lower_no_punctuation)

    def file(self, chapter_file, mode='r'):
        return self.book.file(join(self.full_id, chapter_file), mode)

    def format_id(id):
        return re.sub(Chapter.ID_PREFIX, '', id)