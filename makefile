KINDLEGEN = /Users/carleslc/Downloads/KindleGen_Mac_i386_v2_9/kindlegen

# Change in command with: make BOOK=book-example
BOOK = book-example
DIR = ${BOOK}

PDF_MARGIN = 3cm

LANGUAGE = $(shell python3 get-property.py ${DIR}/_meta.yml language --default en)

COVER_IMAGE = $(shell python3 get-property.py ${DIR}/_meta.yml cover-image)
COVER = $(if ${COVER_IMAGE},--epub-cover-image=${DIR}/${COVER_IMAGE},)

all: clean pdf epub mobi

clean:
	rm -f ${DIR}/${BOOK}.pdf ${BOOK}.epub ${DIR}/${BOOK}.mobi

pdf:
	pandoc --resource-path=${DIR} -V lang=${LANGUAGE} ${DIR}/${BOOK}.md -o ${DIR}/${BOOK}.pdf -V geometry:margin=${PDF_MARGIN}

epub:
	pandoc --resource-path=${DIR} -V lang=${LANGUAGE} ${DIR}/${BOOK}-epub.md -o ${DIR}/${BOOK}.epub ${COVER}

mobi:
	${KINDLEGEN} -locale ${LANGUAGE} ${DIR}/${BOOK}.epub