from unittest import TestCase
from reset_db import ResetDb

class TestResetDb(TestCase):
    def test_create_id_zhcn(self):
        # testing apakah database tercreate dengan benar

        import os
        myfile = "./test.db"
        reset_db = ResetDb("test.db")
        reset_db.create_id_zhcn()
        ## If file exists, delete it ##
        self.assertTrue(os.path.isfile(myfile))
        reset_db.delete_db()

if __name__ == '__main__':
    unittest.main()


# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

