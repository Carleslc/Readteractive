It is true that a gamebook does not have a strict order for chapters because users can jump from one to another according to the options they decide to follow, but sometimes is more elegant to have chapters sorted by narrative branch or other order you decide.

Once book is built, the first chapter shown will be the chapter specified in **`_meta.yml`** (if provided). The following chapters are shown in alphabetical order, so you can define your own order giving a prefix to chapter identifiers like in this example:

```
.
├── book-example/
│   └── _meta.yml
│   └── 0_before/
│       ├── 0_before.md
│       └── 0_before.yml
│   └── 1_after/
│       ├── image.png
│       ├── 1_after.md
│       └── 1_after.yml
```

In this example, assuming that no `start` is set inside `_meta.yml`, the first chapter to show up will be `0_before`, followed by `1_after`.

- (How to build your book -> [build])
- (Return back -> [getting-started])