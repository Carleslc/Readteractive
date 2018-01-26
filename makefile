# Change PDF margin in centimeters (cm) or inches (in)
# Change in command with: make BOOK=book-example PDF_MARGIN=1cm
PDF_MARGIN = 3cm

# Add chapter references for printed books
# Change in command with: make BOOK=book-example PRINTED=yes
PRINTED = no

# Keep all visited chapters available with scrolling in HTML format
# Change in command with: make html BOOK=book-example SCROLL=yes
SCROLL = no

# Change in command with: make BOOK=book-example
BOOK = book-example
DIR = ${BOOK}

# Dependencies
PYTHON = $(shell which python3 2>/dev/null)
PANDOC = $(shell which pandoc 2>/dev/null)
KINDLEGEN = $(shell which kindlegen 2>/dev/null)

.PHONY: all clean check_python check_pandoc check_kindlegen

all: clean html pdf epub mobi

clean:
	rm -f ${DIR}/${BOOK}*

check_python:
	$(if ${PYTHON},,$(error "[ERROR] Python 3 dependency not found (command python3). Install it and try again."))

configure: check_python
	$(eval LANGUAGE := $(shell ${PYTHON} get_property.py ${DIR}/_meta.yml language --default en))
	
	$(eval COVER_IMAGE := $(shell ${PYTHON} get_property.py ${DIR}/_meta.yml cover-image 2>/dev/null))
	$(eval COVER := $(if ${COVER_IMAGE},--epub-cover-image=${DIR}/${COVER_IMAGE},))

	$(eval STYLESHEET := $(shell ${PYTHON} get_property.py ${DIR}/_meta.yml 2>/dev/null))
	$(eval STYLESHEET_OPTION := $(if ${STYLESHEET},--css ${STYLESHEET},))

check_pandoc: check_python
	$(if ${PANDOC},,$(error "[WARNING] Pandoc dependency not found (command pandoc). Skipping PDF, EPUB and MOBI generation."))

check_kindlegen:
	$(if ${KINDLEGEN},,$(error "[WARNING] Kindlegen dependency not found (command kindlegen). Skipping MOBI generation."))

html: check_pandoc
	${PYTHON} process_book.py ${BOOK} html --scroll=${SCROLL}
	${PANDOC} --resource-path=.:${DIR} -V lang=${LANGUAGE} ${DIR}/${BOOK}-html.md -o ${DIR}/${BOOK}.html --css pandoc-html.css --mathml --self-contained
	rm -f ${DIR}/${BOOK}-*.md

pdf: check_pandoc
	$(eval LANGUAGE := $(shell ${PYTHON} get_property.py ${DIR}/_meta.yml language --default en))
	${PYTHON} process_book.py ${BOOK} pdf --printed=${PRINTED}
	${PANDOC} --pdf-engine=xelatex --resource-path=${DIR} -V lang=${LANGUAGE} ${DIR}/${BOOK}-pdf.md -o ${DIR}/${BOOK}.pdf -V geometry:margin=${PDF_MARGIN}
	rm -f ${DIR}/${BOOK}-*.md

epub: check_pandoc
	${PYTHON} process_book.py ${BOOK} epub --printed=${PRINTED}
	${PANDOC} --resource-path=${DIR} -V lang=${LANGUAGE} ${DIR}/${BOOK}-epub.md -o ${DIR}/${BOOK}.epub ${COVER} ${STYLESHEET_OPTION}
	rm -f ${DIR}/${BOOK}-*.md

mobi: epub check_kindlegen
	${KINDLEGEN} -locale ${LANGUAGE} ${DIR}/${BOOK}.epub