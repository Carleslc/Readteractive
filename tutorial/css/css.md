If you know [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) you can customize the style of the book even more than with markdown and HTML.

For custom CSS of the HTML version edit the file `pandoc-html.css` at the top folder.

With EPUB and MOBI (e-book versions) you can optionally specify a `stylesheet.css` for your e-book in the `_meta.yml` file to have custom styles such font family or size.

If no stylesheet is provided then [this one](https://github.com/jgm/pandoc/blob/master/data/epub.css) is used by default.

_This option is not available for PDF because LaTeX is used_

(I want to know more about styles -> [style])