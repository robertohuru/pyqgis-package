import unittest
from pyqgis_package import __version__


class TestVersion(unittest.TestCase):
    def test_version_format(self):
        parts = __version__.split('.')
        self.assertEqual(len(parts), 3)  # Major.Minor.Patch
        for part in parts:
            self.assertTrue(part.isdigit())
