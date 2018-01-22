# Readteractive
Tool for writing and generating interactive books, also known as gamebooks.

## Overview

<!-- MarkdownTOC -->

- [What is a gamebook?](#what-is-a-gamebook)
- [Getting started](#getting-started)
    - [Install dependencies](#install-dependencies)
    - [CLI](#cli)
        - [Features](#features)
    - [Readteractive structure](#readteractive-structure)
        - [Top folder](#top-folder)
        - [Books and chapters folders](#books-and-chapters-folders)
        - [Book metadata](#book-metadata)
        - [Chapter](#chapter)
    - [How to build your book](#how-to-build-your-book)
    - [How to write your book](#how-to-write-your-book)
        - [How to write options](#how-to-write-options)
    - [Styling your book](#styling-your-book)
        - [Markdown](#markdown)
        - [CSS](#css)
        - [PDF](#pdf)
        - [MathML](#mathml)
- [TODO](#todo)

<!-- /MarkdownTOC -->

## What is a gamebook?

A [gamebook](https://en.wikipedia.org/wiki/Gamebook) is a work of printed fiction that allows the reader to participate in the story by making choices. Gamebooks have been influenced by [_Choose Your Own Adventure_ Series](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure) and tabletop role-playing games.

<p align="center"><img src="https://i.imgur.com/DsFtxu8.png"></p>

Production of new gamebooks in the West decreased dramatically during the nineties as choice based stories have moved away from print based media, although the format may be getting a new lease of life on mobile and ebook platforms. Such digital gamebooks are considered [interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction).

## Getting started

Clone this repository with [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) or download the current version as [zip](https://github.com/Carleslc/Readteractive/releases).

### Install dependencies

Note for **Windows**: It is easier to install this dependencies and run Readteractive with a linux-like shell like [Cygwin](https://www.cygwin.com/install.html).

- [**Python 3**](https://www.python.org/downloads/): Needed to process structure and build Markdown files used to generate your book.
- **Make**: Needed to bundle commands and generate your books in any format.
    - Linux: `sudo apt-get install build-essential`
    - Mac OS:
        - (Xcode Utils) `xcode-select --install`
        - Or, using [Homebrew](https://brew.sh): `brew install make`
    - Windows: Install _make_ from Cygwin installer.
- _(PDF, EPUB)_ [**Pandoc**](https://pandoc.org/installing.html): Needed to generate PDF and EPUB from Markdown files.
- _(MOBI)_ [**KindleGen**](https://www.amazon.com/gp/feature.html?docId=1000765211): Needed to generate MOBI for Kindle from EPUB file.
- _(Optional)_ [Kindle Previewer](https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000765261): Needed to preview how your MOBI files looks in tablet and Kindle devices.

### CLI

[![In development](https://img.shields.io/badge/status-in%20development-red.svg)](#todo)
[![CLI repository](https://img.shields.io/badge/CLI-readteractive--generator-blue.svg)](https://github.com/Carleslc/readteractive-generator)

We provide a _command line interface_ to easily generate your project doing **scaffolding**, so you don't need to remember the syntax of each file and you can just **focus on writing**.

It also provides a tool for **visualization** of your book with current chapters and the links between them, so you can have a general overview of the **narrative branches** of your book.

[**Install CLI and boost your productivity with Readteractive!**](https://github.com/Carleslc/readteractive-generator)

#### Features

- Book scaffolding
- Chapter scaffolding
- Book graph visualization

### Readteractive structure

#### Top folder

In the top folder there are the required files for building your books and configure dependencies. _Please, do not edit or move this files to another folder or build will fail._

```
.
├── .git
├── .gitignore
├── book.py
├── chapter.py
├── get_property.py
├── process_book.py
├── pandoc-html.css
├── makefile
├── LICENSE
├── README.md
```

#### Books and chapters folders

Every book and chapter you generate needs to match the following structure:

```
.
├── book-example/
│   └── _meta.yml
│   └── first_chapter/
│       ├── first_chapter.md
│       └── first_chapter.yml
│   └── second_chapter/
│       ├── image.png
│       ├── second_chapter.md
│       └── second_chapter.yml
├── cover.png
├── stylesheet.css
```

This structure and files can be automatically generated using our [CLI](#cli) for your custom book.

Syntax of `.yml` files is based on [YAML](http://www.yaml.org/spec/1.2/spec.html).

Syntax of `.md` files is based on [Markdown](#markdown).

Syntax of `stylesheet.css` file is based on [CSS](#css), but this is optional as explained later.

#### Book metadata

**`_meta.yml`**
```
title: Example _gamebook_
author:
- First Author
- Second Author
start: first_chapter
language: es
cover-image: cover.png
stylesheet: stylesheet.css
description: |
    This is the description of your book.
    Hope you enjoy writting with Readteractive.
```

- (Required) **Title**: The title of your book. You can use [Markdown](#markdown) here using **`**bold**`** and _`_italic_`_.
- (Optional) **Author**: The author of your book, or a list of authors. You can use [Markdown](#markdown) here using **`**bold**`** and _`_italic_`_.
- (Optional) **Starting chapter**: The chapter id (folder) of the first chapter in the book. Defaults to the first alphanumerically chapter.
- (Optional) **Language**: [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) Language Code. Defaults to `en` (English).
- (Optional) **Cover Image**: File of the main image of your book.
- (Optional) **Stylesheet**: The [CSS](#css) stylesheet of your book.
- (Optional) **Description**: The description of your book.

#### Chapter

**`chapter-id.yml`**
```
title: Example _chapter_
```

You can use [Markdown](#markdown) here using **`**bold**`** and _`_italic_`_.

**`chapter-id.md`**

The text of your chapter. You can use [Markdown](#markdown) here.

### How to build your book

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
make clean-md BOOK=book-example # clean intermediate files
```

Built files are saved in your book folder:

```
.
├── book-example/
│   └── book-example.html
│   └── book-example.pdf
│   └── book-example.epub
│   └── book-example.mobi
```

### How to write your book

A gamebook has many chapters with links between them. We refer to a chapter as a step with description in one of your narrative branches.

If you have no previous experience writing gamebooks these are some _tips_:

1. Plan your history. You can make a mind map with each of your narrative branches and which options follow which branch.
2. Define each chapter and write them with Readteractive.
3. Visualize your chapter graph with our [CLI](https://github.com/Carleslc/readteractive-generator) whenever you need to have an overview of your book and ensure each chapter have the links you want.
4. [Build](#how-to-build-your-book) your book from time to time to have a look of how it is looking.

#### How to write options

Each chapter can link to a many different chapters using the following syntax:

```
(Text -> [next])
```

Replace `Text` with your custom option text. Replace `next` with the chapter id which this link is pointing to.

Readteractive will generate a link to the chapter on your book for every reference following this syntax.

You can use [Markdown](#markdown) in `Text`.

### Styling your book

#### Markdown

You can use [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) syntax for styling your chapters. This README file is written entirely in Markdown.

Markdown is simpler than HTML, but if you need to use it, Markdown supports HTML tags.

The example chapter `start.md` provides very useful examples using Markdown.

In order to improve your writting even more you can use a Markdown highlight editor. There are many Markdown editors, some are online like [this](https://stackedit.io/) or [this](https://jbt.github.io/markdown-editor/), and other are desktop applications like [Typeora](https://typora.io/). Code editors like [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/) have markdown plugins too ([Atom package](https://github.com/atom/markdown-preview), [Sublime Text 3 package](https://github.com/SublimeText-Markdown/MarkdownEditing)).

When you build your book, Readteractive will make HTML, PDF and EPUB versions using [Pandoc](https://pandoc.org/installing.html).
Pandoc allows you to do a few more things besides. You can read more about that in the [Pandoc Manual](http://pandoc.org/MANUAL.html).

#### CSS

If you know [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) you can customize the style of the book even more than with markdown and HTML.

For custom CSS of the HTML version edit the file `pandoc-html.css` at the top folder.

With EPUB and MOBI (e-book versions) you can optionally specify a `stylesheet.css` for your e-book in the `_meta.yml` file to have custom styles such font family or size.

If no stylesheet is provided then [this one](https://github.com/jgm/pandoc/blob/master/data/epub.css) is used by default.

_This option is not available for PDF because LaTeX is used_

#### PDF

Although CSS is not available for PDF version because its style is set by [LaTeX](https://en.wikipedia.org/wiki/LaTeX) you can change margins and page breaks.

You can edit margin size in centimeters (`cm`) or inches (`in`) for PDF files in the variable `PDF_MARGIN` at the top of the `makefile`.

You can define an explicit page break using `\newpage` and explicit new line using `\newline` inside your chapter `.md` file.
Unfortunately at the moment this only works for PDF version.

#### MathML

Math equations are rendered using MathML, supported for HTML and PDF but only for some EPUB3 readers and currently gives unrecognised tags on _KindleGen_ converting to MOBI.

## TODO

- Add argument to hide others or keep scroll in HTML.

- Add page number argument for each link (printed gamebooks).

- Human-readable errors (FileNotFoundError, YAML syntax).

- Anchor hyperlinks with target=\_blank

- Fix PDF generation for Tutorial book.

- Check links.

- Yeoman CLI (new book, new chapter, visualize graph links, rename chapter id)

- Additional README in Spanish.
