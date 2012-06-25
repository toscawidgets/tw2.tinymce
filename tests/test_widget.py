#! coding: utf-8
from tw2.core.testbase import  WidgetTest
import tw2.tinymce
import tw2.core.templating as templating
import tw2.core.middleware as tmw

from nose import SkipTest

class TestDemoWidget(WidgetTest):
    """ Test basic rendering. """

    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = tw2.tinymce.TinyMCEWidget

    # Initilization args. go here
    attrs = {'id' : 'test_tinymce'}
    params = {}
    expected = """<textarea rows="25" cols="79" id="test_tinymce" name="test_tinymce"></textarea>"""


class TestDemoWidgetUnicodery(WidgetTest):
    """ Test that the widget can be rendered with non-ascii values. """

    engines = ['mako', 'genshi']
    # place your widget at the TestWidget attribute
    widget = tw2.tinymce.TinyMCEWidget

    # Initilization args. go here
    attrs = {
        'id' : 'test_tinymce',
        'value': u'ä',
    }
    params = {}
    expected = u"""<textarea rows="25" cols="79" id="test_tinymce" name="test_tinymce">ä</textarea>"""

    def _check_rendering_vs_expected(self, engine, attrs, params, expected):
        """ Override this only to use sieve instead of strainer. """
        if self.engines and engine not in self.engines:
            raise SkipTest("%r not in engines %r" % (engine, self.engines))
        _request_id = None
        templating.engine_name_cache = {}
        mw = tmw.make_middleware(None, preferred_rendering_engines=[engine])
        self.request(1, mw)
        try:
            r = self.widget(_no_autoid=True, **attrs).display(**params)
        except ValueError, e:
            if str(e).startswith("Could not find engine name"):
                raise SkipTest("No template for engine %r" % engine)
            else:
                raise

        # reset the cache as not to affect other tests
        import sieve.operators
        sieve.operators.assert_eq_xml(r, expected, wrapped=self.wrap)
