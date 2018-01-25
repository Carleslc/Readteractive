from chapter import *

class Book:

    METADATA_FILE = '_meta.yml'

    def __init__(self, id, child_formatter):
        self.id = id
        self.child_formatter = child_formatter
        metadata_file = self.file(Book.METADATA_FILE)
        metadata = yaml.load(metadata_file)
        metadata_file.close()
        self.title = property(metadata, 'title')
        self.author = property(metadata, 'author', optional=True)
        self.language = property(metadata, 'language', optional=True, default='en')
        self.description = property(metadata, 'description', optional=True, default='')
        self.cover = property(metadata, 'cover-image', optional=True)
        self.start = Chapter.format_id(property(metadata, 'start', optional=True))
        self.__load_chapters()
        #self.__check_links()

    def __load_chapters(self):
        self.__full_ids = []
        self.__chapters = dict() # mapping id to chapter
        for full_id in list(filter(lambda file: isdir(join(self.id, file)), listdir(self.id))):
            chapter = Chapter(self, full_id)
            self.__full_ids.append(full_id)
            self.__chapters[chapter.id] = chapter
        for chapter in self.__chapters.values():
            chapter.parse_children() # may require other chapters, so it need to be after filling chapters dict
        # Public list of chapters sorted by id
        not_start = filter(lambda id: Chapter.format_id(id) != self.start, self.__full_ids)
        self.chapters = sorted([self.get_chapter(id) for id in not_start])
        if self.start is None:
            self.start = self.chapters[0]
        else:
            self.chapters = [self.get_chapter(self.start)] + self.chapters
        if len(self.chapters) == 0:
            error('Cannot build a book without any chapter! Ensure you have at least one chapter and it follows the structure defined in README.md')

    def __check_links(self):
        error('TODO')

    def exists_chapter(self, id):
        return Chapter.format_id(id) in self.__chapters

    def get_chapter(self, id):
        return self.__chapters[Chapter.format_id(id)]

    def get_links(self):
        def children_links(children):
            return ', '.join(children) if len(children) > 0 else '[X]'
        return '\n'.join(['%s -> %s' % (chapter.id, children_links(chapter.children)) for chapter in self.chapters])

    def file(self, book_file, mode='r'):
        path = join(self.id, book_file)
        try:
            return open(path, mode)
        except FileNotFoundError:
            error('%s not found' % path)
