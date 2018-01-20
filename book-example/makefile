LANGUAGE = es
BOOK = book-example
KINDLEGEN = /Users/carleslc/Downloads/KindleGen_Mac_i386_v2_9/kindlegen
PDF_MARGIN = 3cm

all: clean pdf epub mobi

clean:
	rm -f ${BOOK}.pdf ${BOOK}.epub ${BOOK}.mobi

pdf:
	pandoc -V lang=${LANGUAGE} ${BOOK}.md -o ${BOOK}.pdf -V geometry:margin=${PDF_MARGIN}

epub:
	pandoc -V lang=${LANGUAGE} ${BOOK}-epub.md -o ${BOOK}.epub

mobi:
	${KINDLEGEN} -locale ${LANGUAGE} ${BOOK}.epub