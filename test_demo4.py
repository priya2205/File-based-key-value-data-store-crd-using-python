import unittest
import dataStore as crd
ds = crd.DataStore('demo4')
ds.create('vandu',40)
ds.create('darlene',50,2)
class TestSum(unittest.TestCase):
     
      def test_(self):
            res1 = ds.delete("vandu")
            s = "Successful!, The key vandu is deleted"
            self.assertEqual(res1,s)
      # def test_key_size_error(self):
      #        res2 = ds.create("eriujahhekjfhjhfsjhfdbfjdfkjdfbdjfhkdjeawegadjkadgadjad",802894)
      #        self.assertEqual(res2,"OOPs! The key exceeds more than 32 char, the key must be capped at 32 chars") 

if __name__ == "__main__":
    unittest.main()