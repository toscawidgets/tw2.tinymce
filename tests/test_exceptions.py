import tw2.core as twc
import tw2.tinymce

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


def test_exception_no_id():
    w = tw2.tinymce.TinyMCEWidget()
    try:
        print w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'TinyMCEWidget must be supplied an id')

def test_exception_bad_locale():
    w = tw2.tinymce.TinyMCEWidget(id="test", locale="klingon")
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == "Language file for 'klingon' not available")
