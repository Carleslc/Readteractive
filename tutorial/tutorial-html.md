---
title: Readteractive
author: Carleslc
language: en
description: Tool for writing and generating interactive books, also known as gamebooks.
---
<script type="text/javascript" src="show_chapter.js"/>
<script type="text/javascript">chapters(["chapter_start","chapter_book-metadata","chapter_books-structure","chapter_build","chapter_chapter-structure","chapter_cli","chapter_css","chapter_getting-started","chapter_markdown","chapter_math","chapter_options","chapter_pdf","chapter_structure","chapter_style","chapter_tips","chapter_write"])</script>

<p class="description">Tool for writing and generating interactive books, also known as gamebooks.</p>
<figure>![](adventure_time.png)</figure>
\newpage

<div id="chapter_start">

# What is a gamebook?

A [gamebook](https://en.wikipedia.org/wiki/Gamebook) is a work of printed fiction that allows the reader to participate in the story by making choices. Gamebooks have been influenced by [_Choose Your Own Adventure_ Series](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure) and tabletop role-playing games.

Production of new gamebooks in the West decreased dramatically during the nineties as choice based stories have moved away from print based media, although the format may be getting a new lease of life on mobile and ebook platforms. Such digital gamebooks are considered [interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction).

(<span onclick="show_chapter('chapter_getting-started')">[**Getting Started**](#getting-started)</span>)

\newpage

</div>
<div id="chapter_book-metadata"style="display: none">

# Book metadata

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

- (Required) **Title**: The title of your book. You can use (<span onclick="show_chapter('chapter_markdown')">[**Markdown**](#markdown-and-pandoc)</span>) here using **`**bold**`** and _`_italic_`_.
- (Optional) **Author**: The author of your book, or a list of authors. You can use (<span onclick="show_chapter('chapter_markdown')">[**Markdown**](#markdown-and-pandoc)</span>) here using **`**bold**`** and _`_italic_`_.
- (Optional) **Starting chapter**: The chapter id (folder) of the first chapter in the book. Defaults to the first alphanumerically chapter.
- (Optional) **Language**: [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) Language Code. Defaults to `en` (English).
- (Optional) **Cover Image**: File of the main image of your book.
- (Optional) **Stylesheet**: The (<span onclick="show_chapter('chapter_css')">[**CSS**](#css)</span>) stylesheet of your book.
- (Optional) **Description**: The description of your book.

(<span onclick="show_chapter('chapter_chapter-structure')">[**Readteractive Structure: Chapter**](#chapter-structure)</span>)

\newpage

</div>
<div id="chapter_books-structure"style="display: none">

# Books and chapters folders

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

This structure and files can be automatically generated using our (<span onclick="show_chapter('chapter_cli')">[**CLI**](#scaffolding)</span>) for your custom book.

Syntax of `.yml` files is based on [YAML](http://www.yaml.org/spec/1.2/spec.html).

Syntax of `.md` files is based on (<span onclick="show_chapter('chapter_markdown')">[**Markdown**](#markdown-and-pandoc)</span>).

Syntax of `stylesheet.css` file is based on (<span onclick="show_chapter('chapter_css')">[**CSS**](#css)</span>), but this is optional as explained later.

(<span onclick="show_chapter('chapter_book-metadata')">[**Readteractive Structure: Book metadata**](#book-metadata)</span>)

\newpage

</div>
<div id="chapter_build"style="display: none">

# How to build your book

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

- (<span onclick="show_chapter('chapter_write')">[**How to write your book**](#how-to-write-your-book)</span>)
- (<span onclick="show_chapter('chapter_getting-started')">[**Return back**](#getting-started)</span>)

\newpage

</div>
<div id="chapter_chapter-structure"style="display: none">

# Chapter Structure

**`chapter-id.yml`**
```
title: Example _chapter_
```

You can use (<span onclick="show_chapter('chapter_markdown')">[**Markdown**](#markdown-and-pandoc)</span>) here using **`**bold**`** and _`_italic_`_.

**`chapter-id.md`**

The text of your chapter. You can use (<span onclick="show_chapter('chapter_markdown')">[**Markdown**](#markdown-and-pandoc)</span>) here.

(<span onclick="show_chapter('chapter_build')">[**How to build your book**](#how-to-build-your-book)</span>)
(<span onclick="show_chapter('chapter_getting-started')">[**Return back**](#getting-started)</span>)

\newpage

</div>
<div id="chapter_cli"style="display: none">

# Scaffolding

[![In development](https://img.shields.io/badge/status-in%20development-red.svg)](#todo)
[![CLI repository](https://img.shields.io/badge/CLI-readteractive--generator-blue.svg)](https://github.com/Carleslc/readteractive-generator)

We provide a _command line interface_ to easily generate your project doing **scaffolding**, so you don't need to remember the syntax of each file and you can just **focus on writing**.

It also provides a tool for **visualization** of your book with current chapters and the links between them, so you can have a general overview of the **narrative branches** of your book.

[**Install CLI and boost your productivity with Readteractive!**](https://github.com/Carleslc/readteractive-generator)

#### Features

- Book scaffolding
- Chapter scaffolding
- Book graph visualization

Choose an option:

- (<span onclick="show_chapter('chapter_structure')">[**Readteractive Structure**](#readteractive-structure)</span>)
- (<span onclick="show_chapter('chapter_getting-started')">[**Return back**](#getting-started)</span>)

\newpage

</div>
<div id="chapter_css"style="display: none">

# CSS

If you know [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) you can customize the style of the book even more than with markdown and HTML.

For custom CSS of the HTML version edit the file `pandoc-html.css` at the top folder.

With EPUB and MOBI (e-book versions) you can optionally specify a `stylesheet.css` for your e-book in the `_meta.yml` file to have custom styles such font family or size.

If no stylesheet is provided then [this one](https://github.com/jgm/pandoc/blob/master/data/epub.css) is used by default.

_This option is not available for PDF because LaTeX is used_

(<span onclick="show_chapter('chapter_style')">[**I want to know more about styles**](#how-to-style-your-book)</span>)

\newpage

</div>
<div id="chapter_getting-started"style="display: none">

# Getting Started

Clone this repository with [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) or download the current version as [zip](https://github.com/Carleslc/Readteractive/releases).

## Install dependencies

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

Choose an option:

- (<span onclick="show_chapter('chapter_cli')">[**CLI**](#scaffolding)</span>)
- (<span onclick="show_chapter('chapter_structure')">[**Readteractive Structure**](#readteractive-structure)</span>)
- (<span onclick="show_chapter('chapter_build')">[**How to build your book**](#how-to-build-your-book)</span>)
- (<span onclick="show_chapter('chapter_write')">[**How to write your book**](#how-to-write-your-book)</span>)
- (<span onclick="show_chapter('chapter_style')">[**How to style your book**](#how-to-style-your-book)</span>)

\newpage

</div>
<div id="chapter_markdown"style="display: none">

# Markdown and Pandoc

You can use [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) syntax for styling your chapters. This README file is written entirely in Markdown.

Markdown is simpler than HTML, but if you need to use it, Markdown supports HTML tags.

The example chapter `start.md` provides very useful examples using Markdown.

In order to improve your writting even more you can use a Markdown highlight editor. There are many Markdown editors, some are online like [this](https://stackedit.io/) or [this](https://jbt.github.io/markdown-editor/), and other are desktop applications like [Typeora](https://typora.io/). Code editors like [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/) have markdown plugins too ([Atom package](https://github.com/atom/markdown-preview), [Sublime Text 3 package](https://github.com/SublimeText-Markdown/MarkdownEditing)).

When you build your book, Readteractive will make HTML, PDF and EPUB versions using [Pandoc](https://pandoc.org/installing.html).
Pandoc allows you to do a few more things besides. You can read more about that in the [Pandoc Manual](http://pandoc.org/MANUAL.html).

(<span onclick="show_chapter('chapter_style')">[**I want to know more about styles**](#how-to-style-your-book)</span>)

\newpage

</div>
<div id="chapter_math"style="display: none">

# MathML

$$E = mc^2$$

Math equations are rendered using MathML, supported for HTML and PDF but only for some EPUB3 readers and currently gives unrecognised tags on _KindleGen_ converting to MOBI.

(<span onclick="show_chapter('chapter_style')">[**I want to know more about styles**](#how-to-style-your-book)</span>)

\newpage

</div>
<div id="chapter_options"style="display: none">

# How to write options

Each chapter can link to a many different chapters using the following syntax:

![Option syntax](https://i.imgur.com/eYrcPM9.png)

Replace `Text` with your custom option text. Replace `next` with the chapter id which this link is pointing to.

Readteractive will generate a link to the chapter on your book for every reference following this syntax.

You can use (<span onclick="show_chapter('chapter_markdown')">[**Markdown**](#markdown-and-pandoc)</span>) in `Text`.

(<span onclick="show_chapter('chapter_style')">[**How to style your book**](#how-to-style-your-book)</span>)
(<span onclick="show_chapter('chapter_getting-started')">[**Return back**](#getting-started)</span>)

\newpage

</div>
<div id="chapter_pdf"style="display: none">

# PDF

Although CSS is not available for PDF version because its style is set by [LaTeX](https://en.wikipedia.org/wiki/LaTeX) you can change margins and page breaks.

You can edit margin size in centimeters (`cm`) or inches (`in`) for PDF files in the variable `PDF_MARGIN` at the top of the `makefile`.

You can define an explicit page break using `\newpage` and explicit new line using `\newline` inside your chapter `.md` file.
Unfortunately at the moment this only works for PDF version.

(<span onclick="show_chapter('chapter_style')">[**I want to know more about styles**](#how-to-style-your-book)</span>)

\newpage

</div>
<div id="chapter_structure"style="display: none">

# Readteractive Structure

Let's have a look to how folders and files are organized.

# Top folder

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

(<span onclick="show_chapter('chapter_books-structure')">[**Readteractive Structure: Books and chapters folders**](#books-and-chapters-folders)</span>)

\newpage

</div>
<div id="chapter_style"style="display: none">

# How to style your book

Choose an option:

- (<span onclick="show_chapter('chapter_markdown')">[**Boost your writing with Markdown**](#markdown-and-pandoc)</span>)
- (<span onclick="show_chapter('chapter_css')">[**The art of a stylesheet**](#css)</span>)
- (<span onclick="show_chapter('chapter_pdf')">[**What about PDF style?**](#pdf)</span>)
- (<span onclick="show_chapter('chapter_math')">[**I like numbers and formulas**](#mathml)</span>)

_(<span onclick="show_chapter('chapter_getting-started')">[**I am no longer interested in styling**](#getting-started)</span>)__

\newpage

</div>
<div id="chapter_tips"style="display: none">

# Some tips for new interactive writers

If you have no previous experience writing gamebooks these are some _tips_:

1. Plan your history. You can make a mind map with each of your narrative branches and which options follow which branch.
2. Define each chapter and write them with Readteractive.
3. Visualize your chapter graph with our (<span onclick="show_chapter('chapter_cli')">[**CLI**](#scaffolding)</span>) whenever you need to have an overview of your book and ensure each chapter have the links you want.
4. (<span onclick="show_chapter('chapter_build')">[**Build**](#how-to-build-your-book)</span>) your book from time to time to have a look of how it is looking.

(<span onclick="show_chapter('chapter_options')">[**How to write options**](#how-to-write-options)</span>)

\newpage

</div>
<div id="chapter_write"style="display: none">

# How to write your book

A gamebook has many chapters with links between them. We refer to a chapter as a step with description in one of your narrative branches.

Do you have previous experience writing _gamebooks_?

- (<span onclick="show_chapter('chapter_options')">[**Yes**](#how-to-write-options)</span>)
- (<span onclick="show_chapter('chapter_tips')">[**No**](#some-tips-for-new-interactive-writers)</span>)
</div>
