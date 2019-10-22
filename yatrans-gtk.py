#!/home/delvin/.local/bin/python3.8
# -*- coding: utf-8 -*-
import sys
import requests
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Pango
import warnings
warnings.filterwarnings("ignore")
import os
CURRDIR = os.path.dirname(os.path.abspath(__file__))
ICON = os.path.join(CURRDIR, 'yandex-48.xpm')

headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 '
                   'Firefox/14.0.1'),
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':
    'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding':
    'gzip, deflate',
    'Connection':
    'keep-alive',
    'DNT':
    '1'
}
URLDETECT = "https://translate.yandex.net/api/v1.5/tr.json/detect"
URLTRANS = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = "you-API-key"

def clip():
    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_PRIMARY)
    clip = clipboard.wait_for_text()
    return clip

def detect():
    params = {"key": KEY, "text": clip(), "lang": 'ru'}
    respdetect = requests.get(URLDETECT, params=params, headers=headers).json()
    if 'lang' in respdetect.keys():
        respdetect = respdetect
    else:
        respdetect = {'code': 200, 'lang': 'en'}
    langtetect = respdetect["lang"]
    if langtetect != 'ru':
        langout = langtetect + '-ru'
    else:
        langout = 'ru-en'
    return langout

def translate():
    params = {"key": KEY, "text": clip(), "lang": detect()}
    response = requests.get(URLTRANS, params=params, headers=headers).json()
    if 'text' in response.keys():
        response = response
    else:
        response = {'code': 200, 'lang': 'en-ru', 'text': ['the buffer is empty']
        }
    output = ''.join(response["text"])
    return output

class TextViewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=f"Yandex Translator {detect()}")
        self.set_default_size(1000, 350)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.create_textview()
        self.create_toolbar()
        self.key_Esc = Gdk.keyval_from_name("Escape")
        self.connect("key-press-event", self._key)

    def create_toolbar(self):
        toolbar = Gtk.Toolbar()
        self.grid.attach(toolbar, 1, 1, 1, 1)
        new_button = Gtk.ToolButton.new_from_stock(Gtk.STOCK_CLOSE)
        new_button.set_is_important(True)
        toolbar.insert(new_button, 0)
        new_button.connect("clicked", self.on_button_clicked, self.tag_bold)
        new_button.show()

    def on_button_clicked(self, widget, tag):
        Gtk.main_quit()

    def create_textview(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 0, 2, 1)
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text(f"{translate()}")
        scrolledwindow.add(self.textview)
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.tag_bold = self.textbuffer.create_tag("bold",
                                                   weight=Pango.Weight.BOLD)
        self.textview.modify_font(Pango.FontDescription('Menlo Regular 24'))

    def _key(self, widg, event):
        if event.keyval == self.key_Esc:
            Gtk.main_quit()

win = TextViewWindow()
win.connect("destroy", Gtk.main_quit)
win.set_icon_from_file(ICON)
win.show_all()
Gtk.main()
