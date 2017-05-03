#!/usr/bin/env python

import sys
import configparser
import os
import shutil
from PyQt5 import QtWidgets
from PyQt5 import QtWebKitWidgets
from PyQt5 import QtCore

# Read config file

home_dir = os.path.expanduser("~")
conf_path = os.path.join(home_dir, ".config/mrps/mrps.conf")

config = configparser.ConfigParser(delimiters=('='))
config.read(conf_path)

def clean_up():
    os.remove(html_file_full)
    shutil.rmtree(os.path.join(o_file_dir, "reveal.js"))

app = QtWidgets.QApplication(sys.argv)
app.aboutToQuit.connect(clean_up)

if len(sys.argv) == 2:
    o_file_full = os.path.abspath(sys.argv[1])
else:
    o_file_full = QtWidgets.QFileDialog.getOpenFileName()[0]


if o_file_full:
    o_file_dir = os.path.dirname(o_file_full)
    o_file_name = os.path.basename(os.path.normpath(o_file_full))
    o_file_name_bare = os.path.splitext(o_file_name)[0]
    html_file_full = os.path.join(o_file_dir, o_file_name_bare + ".html")

    shutil.copytree(os.path.normpath(config['DEFAULT']['revealjs_path']), os.path.join(o_file_dir, "reveal.js"))
    
    md_file = open(o_file_full, 'r')
    md_content = md_file.read()
    md_file.close()

    f = open(html_file_full, 'w')
    f.write(config['DEFAULT']['html_top'] + '\n\n' +
            md_content + '\n\n' +
            config['DEFAULT']['html_bottom'])
    f.close()



    web = QtWebKitWidgets.QWebView()
    web.load(QtCore.QUrl('file://' + html_file_full))
    web.show()
    sys.exit(app.exec_())
else:
    exit()
