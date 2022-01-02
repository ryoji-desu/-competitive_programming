# 1.ファイル名は「test_対象のモジュール名.py」とする
import unittest
from .abc086_a import decide_even_or_odd

class TestBc086A(unittest.TestCase):
 
  def test_decide_even_or_odd(self):
    self.assertEqual(10, decide_even_or_odd(6, 4)) 
 