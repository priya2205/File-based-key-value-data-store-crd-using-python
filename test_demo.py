import unittest
import dataStore as crd
ds = crd.DataStore('fifth')
ds.create('priya',20)
     
      
class Test2(unittest.TestCase):
       def test_list(self):
            res = ds.create("!priya_v",40)
            self.assertEqual(res,"OOPs! Your Key Name is Invalid, Key name can contain numbers(0-9) and alphabets(a-z A-Z) but no special characters")
if __name__ == "__main__":
    unittest.main()