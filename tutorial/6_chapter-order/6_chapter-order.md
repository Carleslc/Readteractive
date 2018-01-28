It is true that a gamebook does not have a strict order for chapters because users can jump from one to another according to the options they decide to follow, but sometimes is more elegant to have chapters sorted by narrative branch or other order you decide.

Once book is built, the first chapter shown will be the chapter specified in **`_meta.yml`** (if provided). The following chapters are shown in alphabetical order, but you can define your own order giving a numerical prefix to chapter identifiers like in this example:

```
.
├── book-example/
│   └── _meta.yml
│   └── 0-before/
│       ├── 0-before.md
│       └── 0-before.yml
│   └── 1-after/
│       ├── image.png
│       ├── 1-after.md
│       └── 1-after.yml
```

In this example, assuming that no `start` is set inside `_meta.yml`, the first chapter to show up will be `0-before`, followed by `1-after`.

- (How to build your book -> [build])
- (Return back -> [getting-started])