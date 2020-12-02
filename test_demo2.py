import unittest
import dataStore as crd
ds = crd.DataStore('demo2')
ds.create('priya',20)
class TestSum(unittest.TestCase):
     
      def test_key_not_available(self):
            res1 = ds.read("priya_v")
            self.assertEqual(res1,"Oops ! The key you entered is not available, Please ensure you entered a Valid Key")
      # def test_key_size_error(self):
      #        res2 = ds.create("eriujahhekjfhjhfsjhfdbfjdfkjdfbdjfhkdjeawegadjkadgadjad",802894)
      #        self.assertEqual(res2,"OOPs! The key exceeds more than 32 char, the key must be capped at 32 chars") 

if __name__ == "__main__":
    unittest.main()