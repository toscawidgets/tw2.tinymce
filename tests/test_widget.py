from tw2.core.testbase import  WidgetTest
import tw2.tinymce

class TestDemoWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = tw2.tinymce.TinyMCEWidget

    # Initilization args. go here
    attrs = {'id' : 'test_tinymce'}
    params = {}
    expected = """<textarea rows="25" cols="79" id="test_tinymce" name="test_tinymce"></textarea>"""
