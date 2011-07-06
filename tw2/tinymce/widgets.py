import tw2.core as twc


class Tinymce(twc.Widget):
    template = "genshi:tw.tinymce.templates.tinymce"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/tinymce.js'),
        twc.CSSLink(modname=__name__, filename='static/tinymce.css'),
    ]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Tinymce, self).prepare()
        # put code here to run just before the widget is displayed
