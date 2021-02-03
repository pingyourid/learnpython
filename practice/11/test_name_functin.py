import unittest
from name_function import get_full_name

class NameTestCase(unittest.TestCase):
    def test_get_full_name(self):
        result = get_full_name('zhang', 'bin')
        self.assertEqual(result, 'Zhang Bin')

    def test_get_full_name_three(self):
        result = get_full_name('zhang', 'bin', 'wen')
        self.assertEqual(result, 'Zhang Wen Bin')

if __name__ == '__main__':
    unittest.main()



# 前面了解过，py文件被导入（import）时，解释器就会自动执行里面代码，可以用if __name__ == '__main__':区分是被导入还是被执行的