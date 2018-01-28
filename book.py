from chapter import *

class Book:

    METADATA_FILE = '_meta.yml'

    def __init__(self, id, child_formatter):
        self.id = id
        self.child_formatter = child_formatter
        metadata_file = self.file(Book.METADATA_FILE)
        metadata = load(metadata_file)
        self.title = property(metadata, 'title', metadata_file.name)
        self.author = property(metadata, 'author', metadata_file.name, optional=True)
        self.language = property(metadata, 'language', metadata_file.name, optional=True, default='en')
        self.description = property(metadata, 'description', metadata_file.name, optional=True, default='')
        self.cover = property(metadata, 'cover-image', metadata_file.name, optional=True)
        self.start = Chapter.format_id(property(metadata, 'start', metadata_file.name, optional=True))
        metadata_file.close()
        self.__load_chapters()
        self.__check_links()

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
        if len(self.chapters) == 0:
            error('Cannot build a book without any chapter! Ensure you have at least one chapter and it follows the structure defined in README.md')
        if self.start is None:
            self.start = self.chapters[0]
        else:
            self.chapters = [self.get_chapter(self.start)] + self.chapters

    def __check_links(self):
        # TODO: no self-references, no impossible chapters to reach
        return

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
