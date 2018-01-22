[**Install CLI and boost your productivity with Readteractive!**](https://github.com/Carleslc/readteractive-generator)

![In development](https://i.imgur.com/ef60VDz.png)
[![CLI repository](https://i.imgur.com/lMhTTJJ.png)](https://github.com/Carleslc/readteractive-generator)

A [yeoman](http://yeoman.io/learning/index.html) generator for scaffolding [Readteractive](https://github.com/Carleslc/Readteractive) books.

We provide a _command line interface_ to easily generate your project doing **scaffolding**, so you don't need to remember the syntax of each file and you can just **focus on writing**.

The (Readteractive structure -> [structure]) and files can be automatically generated using this CLI for your custom book.

It also provides a tool for **visualization** of your book with current chapters and the links between them, so you can have a general overview of the **narrative branches** of your book.

### Features

- Book scaffolding
- Chapter scaffolding
- Book graph visualization

### Install dependencies

- [Yeoman](http://yeoman.io/learning/index.html): Needed to install readteractive-generator
    - [Npm](https://www.npmjs.com/get-npm): Needed to install Yeoman
        - [Node](https://nodejs.org/en/): Provides Npm

### How to use

- Install Readteractive Generator: `npm install -g readteractive-generator`
- Run: `yo readteractive`

#### Commands

- `yo readteractive` shows a wizard for generate a new book.
- `yo readteractive:chapter` shows a wizard for generate a new chapter.
- `yo readteractive:graph` shows a graph of your book with current chapters and the links between them.

Choose an option:

- (Readteractive Structure -> [structure])
- (Return back -> [getting-started])