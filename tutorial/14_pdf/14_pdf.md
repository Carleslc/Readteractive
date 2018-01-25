Although CSS is not available for PDF version because its style is set by [LaTeX](https://en.wikipedia.org/wiki/LaTeX) you can change margins and page breaks.

You can edit margin size in centimeters (`cm`) or inches (`in`) for PDF files setting the variable `PDF_MARGIN`:

```
make pdf BOOK=book-example PDF_MARGIN=1cm
```

You can define an explicit page break using `\newpage` and explicit new line using `\newline` inside your chapter `.md` file.
Unfortunately at the moment this only works for PDF version.

(I want to know more about styles -> [style])