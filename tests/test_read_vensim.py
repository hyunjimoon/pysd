from unittest import TestCase


class TestRead_vensim(TestCase):
    def test_read_vensim(self):
        import pysd
        print pysd.__file__
        pysd.read_vensim('./test-models/tests/subscript_3d_arrays/test_subscript_3d_arrays.mdl')


    def test_read_vensim(self):
        import pysd
        print pysd.__file__
        model = pysd.read_vensim('./test-models/tests/abs/test_abs.mdl')
        print model.run()

