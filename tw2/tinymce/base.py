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
