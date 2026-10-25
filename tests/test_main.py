import unittest
from main import analyze
class TextTests(unittest.TestCase):
    def test_analyze(self):
        r=analyze(" hello   world\nagain ")
        self.assertEqual(r["words"],3); self.assertEqual(r["normalized"],"hello world again"); self.assertEqual(r["lines"],2)
if __name__=="__main__": unittest.main()
