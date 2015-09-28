Title: Revealjs with Markdown
Date: 2015-01-07 01:16
Modified: 2015-01-07 01:16
Category: Linux
Tags: linux
Slug: revealjs
Authors: Vengatesh.S
<!-- Summary: Revealjs with Markdown -->

Reveal.js is a framework for creating beautiful presentation using HTML. Reveal.js comes with a broad range of features including nested slides, markdown contents, PDF export, speaker notes and a JavaScript API. It's best viewed in a browser with support for CSS 3D transforms but fallbacks are available to make sure your presentation can still be viewed elsewhere.

####Requirement:
* Reveal.js
* Reveal template
* Pandoc

####Installation:
* Download and Extract the Reveal.js from [here](https://codeload.github.com/hakimel/reveal.js/zip/master)
* Or clone the revealjs repository
```
$ git clone https://github.com/hakimel/reveal.js.git
```
* Download a Reveal template and save it in reveal.js directory. [Reveal template](https://codeload.github.com/vengat92/Revealjs-template/zip/master)
* Then to build reveal.js with markdown you need to install Pandoc.
* Pandoc is used to convert one markup format into another.
* To install Pandoc follow this [tutorial](http://johnmacfarlane.net/pandoc/installing.html)

####Build
* To Build Revealjs with markdown run the following command
```
$ pandoc -t html5 --template=template-revealjs.html --standalone --section-divs --variable theme="beige" --variable transition="default" file.md -o slides.html
```