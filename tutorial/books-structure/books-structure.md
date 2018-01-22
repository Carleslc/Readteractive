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

This structure and files can be automatically generated using our (CLI -> [cli]) for your custom book.

Syntax of `.yml` files is based on [YAML](http://www.yaml.org/spec/1.2/spec.html).

Syntax of `.md` files is based on (Markdown -> [markdown]).

Syntax of `stylesheet.css` file is based on (CSS -> [css]), but this is optional as explained later.

(Readteractive Structure: Book metadata -> [book-metadata])