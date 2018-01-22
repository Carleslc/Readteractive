Each chapter can link to a many different chapters using the following syntax:

![Option syntax](https://i.imgur.com/uoOfXFT.png)

Replace `Text` with your custom option text. Replace `next` with the chapter id which this link is pointing to.

Readteractive will generate a link to the chapter on your book for every reference following this syntax.

You can use (Markdown -> [markdown]) in `Text`.

You can skip the chapter prefix defined for (custom order -> [chapter-order]) at the moment of writing an option in `next`:

![Prefix skipping](https://i.imgur.com/ZOwB1N0.png)

These options are equivalent.

This prefix skipping only works for digits followed by - or \_.

- (How to style your book -> [style])
- (Return back -> [getting-started])