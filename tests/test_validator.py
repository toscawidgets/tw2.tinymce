from tw2.core.testbase import  ValidatorTest
import tw2.tinymce

class TestDemoWidget(ValidatorTest):
    # place your widget at the TestWidget attribute
    validator = tw2.tinymce.MarkupConverter

    # Initilization args. go here
    to_python_attrs = [{}, {}, {}, {}]
    to_python_params = [
        """No HTML here""",
        """<a href="this is a link">A Link!</a>""",
        """<h1>THIS IS LOUD.</h1><br/>""",
        """<h1>THIS IS LOUD.</h1><br />"""]
    to_python_expected = [
        """No HTML here""",
        """<a href="this is a link">A Link!</a>""",
        """<h1>THIS IS LOUD.</h1>""",
        """<h1>THIS IS LOUD.</h1>"""]
