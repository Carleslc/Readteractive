Clone [this repository](https://github.com/Carleslc/Readteractive) with [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) or download the current version as [zip](https://github.com/Carleslc/Readteractive/releases).

## Install dependencies

Note for **Windows**: It is easier to install these dependencies and run Readteractive with a linux-like shell like [Cygwin](https://www.cygwin.com/install.html).

- [**Python 3**](https://www.python.org/downloads/): Needed to process structure and build Markdown files used to generate your book.
  - Install Python dependencies with: `pip install -r requirements.txt`
- **Make**: Needed to bundle commands and generate your books in any format.
    - Linux: `apt-get install build-essential`
    - Mac OS:
        - (Xcode Utils) `xcode-select --install`
        - Or, using [Homebrew](https://brew.sh): `brew install make`
    - Windows: Install _make_ from Cygwin installer.
- _(HTML, PDF, EPUB)_ [**Pandoc**](https://pandoc.org/installing.html): Needed to generate HTML, PDF and EPUB from Markdown files.
- _(MOBI, Optional)_ [**KindleGen**](https://www.amazon.com/gp/feature.html?docId=1000765211): Needed to generate MOBI from EPUB file.
  - It is included installing [**Kindle Previewer**](https://www.amazon.com/Kindle-Previewer/b?node=21381691011), also used to preview how your MOBI files look in tablet and Kindle devices.
- _(Optional)_ **librsvg**: Convert SVG images for being used inside PDF
    - Linux: `apt-get install librsvg2-bin`
    - Mac OS, using [Homebrew](https://brew.sh): `brew install librsvg`
    - Windows: Install _librsvg2_ from Cygwin installer.

Choose an option:

- (Readteractive Structure -> [structure])
- (CLI: Scaffolding and Graph -> [cli])
- (How to build your book -> [build])
- (How to write your book -> [write])
- (How to style your book -> [style])