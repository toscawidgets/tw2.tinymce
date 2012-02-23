import re
import os

import tw2.core as twc
from pkg_resources import ResourceManager

rm = ResourceManager()

tinymce_dir = twc.DirLink(modname=__name__, filename="static/tiny_mce")
#tinymce_js = twc.JSLink(modname=__name__, filename='static/tinymce.js')
#tinymce_css = twc.CSSLink(modname=__name__, filename='static/tinymce.css')
tinymce_js = twc.JSLink(modname = __name__, 
    filename = 'static/tiny_mce/tiny_mce_src.js',
    init = twc.js_function('tinyMCE.init'))

def _get_available_languages():
    filename_re = re.compile(r'(\w+)\.js')
    langs = []
    locale_dir = rm.resource_filename(__name__, "static/tiny_mce/langs")
    for filename in os.listdir(locale_dir):
        match = filename_re.match(filename)
        if match:
            langs.append(match.groups(0)[0])
    return langs

from formencode.validators import UnicodeString, Validator
from genshi.core import Markup, stripentities

class MarkupConverter(UnicodeString):
    """A validator for TinyMCE widget.

    Will make sure the text that reaches python will be unicode un-xml-escaped 
    HTML content.

    Will also remove any trailing <br />s tinymce sometimes leaves at the end
    of pasted text.
    """
    def __init__(self, **kw):
        UnicodeString.__init__(self, **kw)

    cleaner = re.compile(r'(\s*<br[ ]{0,1}/>\s*)+$').sub
    if_missing=''
    def _to_python(self, value, state=None):
        value = super(MarkupConverter, self)._to_python(value, state)
        if value:
            value = Markup(stripentities(value)).unescape()
            return self.cleaner('', value)

