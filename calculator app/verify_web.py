import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index_page(self):
        """Test that the index page loads."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Calculator', response.data)

    def test_addition(self):
        """Test addition via POST request."""
        response = self.client.post('/', data={'num1': '5', 'num2': '3', 'operation': 'add'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Result:', response.data)
        self.assertIn(b'8', response.data)

    def test_division_by_zero(self):
        """Test division by zero handling."""
        response = self.client.post('/', data={'num1': '5', 'num2': '0', 'operation': 'divide'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cannot divide by zero!', response.data)

    def test_invalid_input(self):
        """Test invalid input handling."""
        response = self.client.post('/', data={'num1': '', 'num2': '3', 'operation': 'add'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please enter both numbers.', response.data)

if __name__ == '__main__':
    unittest.main()
