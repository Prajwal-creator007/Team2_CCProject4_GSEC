import unittest
from app import put_key_value, get_value, delete_key, list_keys

class TestKeyValueStore(unittest.TestCase):
    
    def test_put_key_value(self):
        # Test putting a key-value pair
        result = put_key_value('testkey3', 'testvalue3')
        self.assertEqual(result, "Put testkey3: testvalue3")

    def test_get_value(self):
        # Test getting the value for an existing key
        result = get_value('foo')
        self.assertEqual(result, "Value for foo: bar")

        # Test getting the value for a non-existent key
        result = get_value('nonexistent_key')
        self.assertEqual(result, "Key nonexistent_key not found.")

    def test_delete_key(self):
        # Test deleting an existing key
        result = delete_key('heyy')
        self.assertEqual(result, "Deleted key: heyy")

        # Test deleting a non-existent key
        result = delete_key('nonexistent_key')
        self.assertEqual(result, "Key nonexistent_key not found.")

    def test_list_keys(self):
        # Test listing keys when there are keys present
        result = list_keys()
        self.assertIn("testkey3", result)

        # Test listing keys when there are no keys present
        # This assumes that there are no keys present initially
        # You may need to adjust this based on your actual implementation
        result = list_keys()
        self.assertEqual(result, "No keys found.")

if __name__ == '__main__':
    unittest.main()
