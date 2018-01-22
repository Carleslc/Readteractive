PDF_MARGIN = 3cm

# Change in command with: make BOOK=book-example
BOOK = book-example
DIR = ${BOOK}

# Dependencies
PYTHON = $(shell which python3 2>/dev/null)
PANDOC = $(shell which pandoc 2>/dev/null)
KINDLEGEN = $(shell which kindlegen 2>/dev/null)

.PHONY: all clean clean-md check_python check_pandoc check_kindlegen

all: clean markdown html pdf epub clean-md mobi

clean-md:
	rm -f ${DIR}/${BOOK}*.md

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

check_pandoc:
	$(if ${PANDOC},,$(error "[WARNING] Pandoc dependency not found (command pandoc). Skipping PDF, EPUB and MOBI generation."))

check_kindlegen:
	$(if ${KINDLEGEN},,$(error "[WARNING] Kindlegen dependency not found (command kindlegen). Skipping MOBI generation."))

markdown: configure
	${PYTHON} process_book.py ${BOOK}

html: markdown check_pandoc
	${PANDOC} --resource-path=.:${DIR} -V lang=${LANGUAGE} ${DIR}/${BOOK}-html.md -o ${DIR}/${BOOK}.html --css pandoc-html.css --self-contained --mathml

pdf: markdown check_pandoc
	${PANDOC} --pdf-engine=xelatex --resource-path=${DIR} -V lang=${LANGUAGE} ${DIR}/${BOOK}-pdf.md -o ${DIR}/${BOOK}.pdf -V geometry:margin=${PDF_MARGIN}

epub: markdown check_pandoc
	${PANDOC} --pdf-engine=xelatex --resource-path=${DIR} -V lang=${LANGUAGE} ${DIR}/${BOOK}-epub.md -o ${DIR}/${BOOK}.epub ${COVER} ${STYLESHEET_OPTION}

mobi: epub check_kindlegen
	${KINDLEGEN} -locale ${LANGUAGE} ${DIR}/${BOOK}.epub