If you have all dependencies installed is as easy as executing one command:

```
make BOOK=book-example
```

This will ensure your book and chapters structure is right, check for broken links between chapters and then pack and build your book in different formats:

- HTML
- PDF
- EPUB
- MOBI

The PDF version use [LaTeX](https://en.wikipedia.org/wiki/LaTeX) to get a high-quality typography.

Each chapter will generate a header in the table of contents of the PDF, EPUB and MOBI metadata, and each option will have a clickable link that jumps to the next chapter page.

The HTML version is more dynamic. It only shows the chapters you have followed with a click on a link so story proceeds more interactively over the book. It also works offline (is self-contained).

The MOBI version is useful for Kindle devices.

Furthermore, you can build only the desired format:

```
make html BOOK=book-example
make pdf BOOK=book-example
make epub BOOK=book-example
make mobi BOOK=book-example
```

If you are going to print your book then you should be asking about chapter and page references, because links does not work in paper. You are right. If you do so you will need to have chapter order defined as explained in (chapters order -> [chapter-order]). Then, you can build your book using the variable `PRINTED`:

```
make BOOK=book-example PRINTED=yes
```

This will add the chapter order on each section and all link references will have that number after the option text. Then you can go to the last page where the Table of Contents is located and follow the page of the referenced chapter.

Built files are saved in your book folder:

```
.
├── book-example/
│   └── book-example.html
│   └── book-example.pdf
│   └── book-example.epub
│   └── book-example.mobi
```

- (How to write your book -> [write])
- (Return back -> [getting-started])