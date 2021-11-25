import unittest
import sys, os
from unittest.mock import patch, Mock

import builder

sys.path.append(os.getcwd())
from builder import *


class Shop_Test_Builder(unittest.TestCase):
    @patch.object(builder.Shop_Builder(), 'milk')
    def test_milk(self, mock_milk):
        mock_milk.return_value = None
        self.assertEqual(Shop_Builder().milk(), None)
