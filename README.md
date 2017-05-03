# mrps

mrps is a script that quickly and easily displays a markdown file as a presentation. It does ths by creating a temporary reveal.js compatible html file, copying the reveal.js directory over then opening the resulting files in a minimal "browser" using PyQt5.

## Prerequsites

- python3
- PyQt5 with PyQt5.qtwebkit (For python3)
- reveal.js

Before using mrps you must first download reveal.js. There is no official meathod for doing this. I just cloned the reveal.js github repository.

You will also need to have python and PyQt5 installed (including the PyQt5.qtwebkit).

## Initial Configuration

mrps does not know where the reveal.js directory is located on your system. It doesn't try to guess either. Instead, it will use whatever you specify in "~/.config/mrps/mrps.conf".

mrps also needs to know how you want reveal.js configured. This is also specified in the mrps.conf. Details on modifying this can befound at the reveal.js project.

mrps comes with a simple mrps.conf file. You will need to edit it to match your system and move it to ~/.config/mrps/ (creating the directories if needed).

### Themes

node.js comes with a few themes by default. These are located in reveal.js/css/theme/. To change the theme ust change the line ``` <link rel="stylesheet" href="reveal.js/css/theme/black.css" id="theme"> ``` under 'html_top' in mrps.conf to specify the desited theme.

## Seperating Slides

mrps looks for '---' surrounded by empty lines to determine where to seperate horizontal slides and '--' surrounded by empty lines to seperate verticle slides. This is also configurable by editing the ``` <section data-markdown data-separator="^\n---\n$" data-separator-vertical="^\n--\n$"> ``` line under the 'html_top' section of mrps.conf.

### Example of Slide Seperation

```

## Demo 1

Slide 1.1

--

## Demo 2

Slide 1.2

---

## Demo 2

Slide 2

```

## Opening a Markdown File as a Presentation

    $ python mrps.py presentation.md

## Temporary Files

When you run mprs on a markdown file it will create a temporary html version of the file. This file will reside in the same directory as the original markdown file. It will also place a copy of the reveal.js directory into this directory. When you close the presentation, these files will be deleted.

## Quality Warning

This is a quick script with no quality control. It does not try to fail gracefully, verify input or avoid overwriting files.
