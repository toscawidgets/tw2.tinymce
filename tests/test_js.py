import tw2.core as twc
import tw2.tinymce

from nose.tools import eq_

def request_local_tst():
    global _request_local, _request_id
# if _request_id is None:
# raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setup():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()

def test_js_call():
    w = tw2.tinymce.TinyMCEWidget(id='foobar')
    w.display()

    js_calls = filter(lambda x: "JSFuncCall" in str(x), w.resources)

    assert(len(js_calls) == 1)

    for js_call in js_calls:
        eq_(js_call.src,"""tinyMCE.init({"theme_advanced_toolbar_location": "top", "theme_advanced_toolbar_align": "center", "paste_auto_cleanup_on_paste": true, "language": "en", "paste_convert_headers_to_strong": false, "theme_advanced_resizing": true, "theme_advanced_statusbar_location": "bottom", "paste_strip_class_attributes": "all", "theme": "advanced", "elements": "foobar", "mode": "exact", "plugins": "advimage", "paste_use_dialog": false, "extended_valid_elements": "a[href|target|name]"})""")
