# mrps

mrps is a script that quickly and easily displays a markdown file as a presentation. It does ths by creating a temporary reveal.js compatible html file using pandoc, copying the reveal.js directory over then opening the resulting files in a minimal "browser" using PyQt5.

## Prerequsites

- pandoc
- reveal.js
- PyQt5 with PyQt5.qtwebkit (For python3)
- python3

Before using mrps you must first install pandoc and download reveal.js. There is no official meathod for doing this. I installed pandoc using my Linux Distribution's package manager and cloned the reveal.js github repository.

You will also need to have python and PyQt5 installed.

## Initial Configuration

mrps does not know where the pandoc binary or the reveal.js directory are located on your system of if pandoc is in your path. It doesn't try to guess either. Instead, it will use whatever you specify in "~/.config/mrps/mrps.conf".

mrps will not try and create this file with default values either, it is up to you to create this file and populate it with the values you want to use.

### Example ~/.config/mrps/mrps.conf

    [DEFAULT]
    revealjs_path = /home/cnodell/git/reveal.js
    pandoc_path = /usr/bin/pandoc

## Opening a Markdown File as a Presentation

    $ mrps presentation.md

## Temporary Files

When you run mprs on a markdown file it will create a temporary html version of the file. This file will reside in the same directory as the original markdown file. It will also place a copy of the reveal.js directory into this directory. When you close the presentation, these files will be deleted.

## Quality Warning

This is a quick script with no quality control. It does not try to fail gracefully, verify input or avoid overwriting files.
