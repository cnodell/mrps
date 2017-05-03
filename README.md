# mrps

mrps is a script that quickly and easily displays a markdown file as a presentation. It does this by creating a temporary reveal.js compatible html file, copying the reveal.js directory over then opening the resulting files in a minimal "browser" using PyQt5.

## Prerequisites

- python3
- PyQt5 with PyQt5.qtwebkit (For python3)
- reveal.js

Before using mrps you must first download reveal.js. There is no official method for doing this. I just cloned the reveal.js github repository.

You will also need to have python and PyQt5 installed (including the PyQt5.qtwebkit).

## Initial Configuration

mrps does not know where the reveal.js directory is located on your system. It doesn't try to guess either. Instead, it will use whatever you specify in "~/.config/mrps/mrps.conf".

mrps also needs to know how you want reveal.js configured. This is also specified in the mrps.conf. Details on modifying this can be found at the reveal.js project. mrps just put's your markdown content between the html bits specified under the html_top and html_bottom sections as found in mrps.conf. The resulting html file is the same as you would get if you had hand crafted it using the reveal.js documentation.

mrps comes with a sample mrps.conf file. You should edit it as needed (be sure to verify reveal.js's location) and move it to ~/.config/mrps/ (creating the directories if needed).

### Themes

node.js comes with a few themes by default. These are located in reveal.js/css/theme/. To change the theme just change the line ``` <link rel="stylesheet" href="reveal.js/css/theme/black.css" id="theme"> ``` under 'html_top' in mrps.conf to specify the desired theme. Once done all presentations will use this new theme.

## Separating Slides

mrps looks for '---' surrounded by empty lines to determine where to separate horizontal slides and '--' surrounded by empty lines to separate vertical slides. This is also configurable by editing the ``` <section data-markdown data-separator="^\n---\n$" data-separator-vertical="^\n--\n$"> ``` line under the 'html_top' section of mrps.conf.

I prefer to use just the '---' separator as I seldom need vertical slides and --- is valid markdown (a horizontal rule).

### Example of Slide Separation

```

## Slide 1

This slide has slide 2 after it on the right side (--- separator).

---

## Slide 2

This slide has Slide 2.2 below it (-- separator), Slide 1 to it's left (before it) and Slide 3 to it's right (after it).

--

## Slide 2.2

This slide has Slide 2 above it (-- separator), Slide 1 to it's left (before it) and Slide 3 to it's right (after it).

---

## Slide 3

This slide has slide 2 to it's left (before it).

```

## Opening a Markdown File as a Presentation

    $ python mrps.py presentation.md

## Temporary Files

When you run mrps on a markdown file it will create a temporary html version of the file. This file will reside in the same directory as the original markdown file. It will also place a copy of the reveal.js directory into this directory. When you close the presentation, these files will be deleted.

## Quality Warning

This is a quick script with no quality control. It does not try to fail gracefully, verify input or avoid overwriting files.
