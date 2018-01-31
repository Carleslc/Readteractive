import yaml
import string, re
from get_property import *
from os import listdir
from os.path import join, isdir, abspath

class Chapter:

    ONLY_ORDER = re.compile(r'^\d+[-_]*$',re.S)
    ID_PREFIX = re.compile(r'^(\d+)[-_]*',re.S)
    NEXT_REGEX = re.compile(r'\(\s*([^\)]*?)\s*->\s*\[\s*(.*?)\s*\]\s*\)',re.S|re.M)

    title_references = set()

    def __init__(self, book, full_id):
        self.book = book
        self.full_id = full_id
        self.order = None
        self.id = self.__extract_id(full_id)
        metadata_file = self.file(self.full_id + '.yml')
        metadata = load(metadata_file)
        metadata_file.close()
        self.title = property(metadata, 'title', metadata_file.name)
        self.__add_title_reference()
        self.text = self.file(self.full_id + '.md').read()

    def __add_title_reference(self):
        before = len(Chapter.title_references)
        self.title_reference = self.header_markdown_reference(self.title)
        Chapter.title_references.add(self.title_reference)
        after = len(Chapter.title_references)
        if before == after:
            error('Chapter titles must be different. Found duplicate: "%s"' % self.title)

    def parse_children(self):
        def next_replacement(match):
            (next_text, next_id) = match.groups()
            id_no_prefix = Chapter.format_id(next_id)
            if not self.book.exists_chapter(id_no_prefix):
                error('Broken link. Chapter "%s" not found and required in %s at "(%s -> [%s])"' % (next_id, self.id, next_text, next_id))
            self.children.add(id_no_prefix)
            chapter = self.book.get_chapter(id_no_prefix)
            return self.book.child_formatter(chapter.id, next_text, chapter.title_reference, chapter.order)
        self.children = set()
        self.text = re.sub(Chapter.NEXT_REGEX, next_replacement, self.text)

    def header_markdown_reference(self, text):
        lower_no_punctuation = ''.join([c for c in text if c not in string.punctuation]).strip().lower()
        return re.sub(r'\s', '-', lower_no_punctuation)

    def __extract_id(self, id):
        def replacement(match):
            self.order = int(match.groups()[0])
            return id if re.match(Chapter.ONLY_ORDER, id) else ''
        return re.sub(Chapter.ID_PREFIX, replacement, id)

    def __lt__(self, other):
        """Order has preference, then alphabetically"""
        if self.order != None:
            return self.order < other.order if other.order != None else True
        else:
            return False if other.order != None else self.id < other.id 

    def file(self, chapter_file, mode='r'):
        return self.book.file(join(self.full_id, chapter_file), mode)

    def format_id(id):
        return None if id == None else re.sub(Chapter.ID_PREFIX, '', id)