---
title: Example _gamebook_
author: Carleslc
language: es
abstract: |
	This is the description of your book.
	Hope you enjoy writting with Readteractive.
---

![](cover.jpeg)
\newpage

# Example _chapter_

An h1 header
============

This is a chapter link:

- ([**Go to the end**](#game-over))

Paragraphs are separated by a blank line.

2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
look like:

  * this one
  * that one
  * the other one

Note that --- not considering the asterisk --- the actual text
content starts at 4-columns in.

> Block quotes are
> written like so.
>
> They can span multiple paragraphs,
> if you like.

Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
in chapters 12--14"). Three dots ... will be converted to an ellipsis.

An h2 header
------------

Here's a numbered list:

 1. first item
 2. second item
 3. third item

Note again how the actual text starts at 4 columns in (4 characters
from the left side). Here's a code sample:

    # Let me re-iterate ...
    for i in 1 .. 10 { do-something(i) }

As you probably guessed, indented 4 spaces. By the way, instead of
indenting the block, you can use delimited blocks, if you like:

~~~
define foobar() {
    print "Welcome to flavor country!";
}
~~~

(which makes copying & pasting easier). You can optionally mark the
delimited block for Pandoc to syntax highlight it:

~~~python
import time
# Quick, count to ten!
for i in range(10):
    # (but not *too* quick)
    time.sleep(0.5)
    print i
~~~



### An h3 header ###

Now a nested list:

 1. First, get these ingredients:

      * carrots
      * celery
      * lentils

 2. Boil some water.

 3. Dump everything in the pot and follow
    this algorithm:

        find wooden spoon
        uncover pot
        stir
        cover pot
        balance wooden spoon precariously on pot handle
        wait 10 minutes
        goto first step (or shut off burner when done)

    Do not bump wooden spoon or it will fall.

Notice again how text always lines up on 4-space indents (including
that last line which continues item 3 above).

Here's a link to [a website](http://foo.bar), to a [local
doc](local-doc.html), and to a [section heading in the current
doc](#an-h2-header). Here's a footnote [^1].

[^1]: Footnote text goes here.

Tables can look like this:

size  material      color
----  ------------  ------------
9     leather       brown
10    hemp canvas   natural
11    glass         transparent

Table: Shoes, their sizes, and what they're made of

(The above is the caption for the table.) Pandoc also supports
multi-line tables:

--------  -----------------------
keyword   text
--------  -----------------------
red       Sunsets, apples, and
          other red or reddish
          things.

green     Leaves, grass, frogs
          and other things it's
          not easy being.
--------  -----------------------

A horizontal rule follows.

***

Here's a definition list:

apples
  : Good for making applesauce.
oranges
  : Citrus!
tomatoes
  : There's no "e" in tomatoe.

Again, text is indented 4 spaces. (Put a blank line between each
term/definition pair to spread things out more.)

Here's a "line block":

| Line one
|   Line too
| Line tree

and images can be specified like so:

![Peaceful Waterfall](start/waterfall.jpg "Photo by Jeffrey Workman on Unsplash")

Also with a hyperlink:

![Strolling down the canyon](https://images.unsplash.com/photo-1491466424936-e304919aada7?auto=format&fit=crop&w=1949&q=80 "Photo by Jonatan Pie on Unsplash")

Inline math equations go in like so: $\omega = d\phi / dt$. Display
math should get its own line and be put in in double-dollarsigns:

$$I = \int \rho R^{2} dV$$

And note that you can backslash-escape any punctuation characters
which you wish to be displayed literally, ex.: \`foo\`, \*bar\*, etc.

\newpage

# Game over

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque suscipit, enim at interdum pellentesque, augue mi aliquet sapien, et aliquam tortor nunc mattis dui. Pellentesque auctor turpis ac erat congue malesuada. Sed non neque non sapien convallis egestas id vel ligula. Maecenas imperdiet ex id dui lacinia vehicula. Donec id nunc congue, maximus lorem sed, condimentum arcu. Ut commodo ac dolor sed commodo. Proin lectus odio, aliquet pretium accumsan sit amet, vehicula euismod ex. Nam bibendum elementum ligula ut vulputate. Aliquam erat volutpat. Morbi et arcu auctor, rhoncus eros vitae, porta magna. Nulla porttitor est in purus dapibus, vitae malesuada justo imperdiet. Quisque porta erat neque, quis accumsan quam posuere sit amet. Morbi ut est finibus, dignissim nisl id, tristique neque. Cras in finibus magna.

Donec commodo diam ut feugiat rutrum. Etiam placerat massa metus, vitae vehicula felis feugiat vel. Duis ultricies finibus turpis, nec bibendum eros euismod sed. Duis ac nulla non ligula vehicula sollicitudin vitae at diam. Ut euismod enim ac eros suscipit rutrum. Vestibulum lacus dui, ullamcorper sed auctor at, egestas non purus. Curabitur ac tortor neque. Donec nec vehicula purus. In nec nisi vel urna mollis accumsan a pharetra ante. Vestibulum tempor dapibus metus nec mollis. Etiam mollis turpis ut lectus luctus, ac facilisis lorem porta. Nulla eu eros suscipit, pretium magna eget, convallis sapien. Nullam urna lacus, mollis quis lectus quis, euismod faucibus velit. Maecenas eget mattis nuncum.
