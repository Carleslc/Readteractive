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
        self.start = property(metadata, 'start', optional=True)
        self.__load_chapters()
        #self.__check_links()

    def __load_chapters(self):
        self.__chapters = dict() # mapping id to chapter
        for id in list(filter(lambda file: isdir(join(self.id, file)), listdir(self.id))):
            id = Chapter.format_id(id)
            self.__chapters[id] = Chapter(self, id)
        for chapter in self.__chapters.values():
            chapter.parse_children() # may require other chapters, so it need to be after filling chapters dict
        # Public list of chapters sorted by id
        not_start = sorted(filter(lambda id: id != self.start, self.__chapters.keys()))
        self.chapters = [self.get_chapter(id) for id in not_start]
        if self.start is None:
            self.start = self.chapters[0]
        else:
            self.chapters = [self.get_chapter(self.start)] + self.chapters
        if len(self.chapters) == 0:
            error('Cannot build a book without any chapter! Ensure you have at least one chapter and it follows the structure defined in README.md')

    def __check_links(self):
        error('TODO')

    def exists_chapter(self, id):
        return id in self.__chapters

    def get_chapter(self, id):
        return self.__chapters[id]

    def get_links(self):
        def children_links(children):
            return ', '.join(children) if len(children) > 0 else '[X]'
        return '\n'.join(['%s -> %s' % (chapter.id, children_links(chapter.children)) for chapter in self.chapters])

    def file(self, book_file, mode='r'):
        return open(join(self.id, book_file), mode)
