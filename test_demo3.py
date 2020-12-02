import unittest
import dataStore as crd
ds = crd.DataStore('demo3')
ds.create('vandu',40)
class TestSum(unittest.TestCase):
     
      def test_(self):
            res1 = ds.read("vandu")
            lst = {'value':40,'timetolive':0}
            self.assertEqual(res1,lst)
      # def test_key_size_error(self):
      #        res2 = ds.create("eriujahhekjfhjhfsjhfdbfjdfkjdfbdjfhkdjeawegadjkadgadjad",802894)
      #        self.assertEqual(res2,"OOPs! The key exceeds more than 32 char, the key must be capped at 32 chars") 

if __name__ == "__main__":
    unittest.main()