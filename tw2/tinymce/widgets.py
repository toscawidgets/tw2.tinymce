import tw2.core as twc
import base 
from tw2.forms import TextArea
import re

class TinyMCEWidget(TextArea):
    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [base.tinymce_js, base.tinymce_dir]
    langs = base._get_available_languages()
    locale = 'en'
    params = ["mce_options", "locale"]
    cols = 79
    rows = 25
    mce_options = {}
    default_options = dict(
        mode = "exact",
        theme = "advanced",
        plugins = "advimage",
        theme_advanced_toolbar_location = "top",
        theme_advanced_toolbar_align = "center",
        theme_advanced_statusbar_location = "bottom",
        extended_valid_elements = "a[href|target|name]",
        theme_advanced_resizing = True,
        paste_use_dialog = False,
        paste_auto_cleanup_on_paste = True,
        paste_convert_headers_to_strong = False,
        paste_strip_class_attributes = "all",
    )
    validator = base.MarkupConverter()
    include_dynamic_js_calls = True

    def prepare(self):
        super(TinyMCEWidget, self).prepare()
        if not hasattr(self, 'id') or 'id' not in self.attrs:
            raise ValueError, 'TinyMCEWidget must be supplied an id'
        options = self.default_options.copy()
        options.update(self.mce_options)
        if self.locale in self.langs:
            options.setdefault('language', self.locale)
        else:
            raise ValueError, "Language file for '%s' not available" % self.locale
            self.locale = 'en'
        if options.setdefault('mode', 'exact') == 'exact':
            options['elements'] = self.attrs['name']
        # Next line creates a javascript call which will be placed at bodybottom
        # to initialize tinyMCE with desired options.
        self.add_call(base.tinymce_js.init(options))
