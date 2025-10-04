"""
Basic tests for the Research Insights API
Run with: python test_app.py
"""

import unittest
import json
from app import app

class APITestCase(unittest.TestCase):
    """Test cases for API endpoints"""
    
    def setUp(self):
        """Set up test client"""
        self.client = app.test_client()
        self.client.testing = True
        
        # Sample test data
        self.sample_text = """
        This study examines accessibility barriers faced by visually impaired users.
        Our findings reveal significant challenges including inadequate screen reader
        support and missing alternative text for images.
        """
        
    def test_health_endpoint(self):
        """Test the health check endpoint"""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('message', data)
        
    def test_groups_endpoint(self):
        """Test getting available user groups"""
        response = self.client.get('/groups')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('groups', data)
        self.assertIsInstance(data['groups'], list)
        self.assertGreater(len(data['groups']), 0)
        
    def test_categories_endpoint(self):
        """Test getting available categories"""
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('categories', data)
        self.assertIsInstance(data['categories'], list)
        self.assertGreater(len(data['categories']), 0)
        
    def test_analyze_endpoint_success(self):
        """Test successful text analysis"""
        payload = {
            'text': self.sample_text,
            'group': 'People with disabilities',
            'category': 'Accessibility'
        }
        
        response = self.client.post(
            '/analyze',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('issues', data)
        self.assertIsInstance(data['issues'], list)
        self.assertEqual(data['group'], 'People with disabilities')
        self.assertEqual(data['category'], 'Accessibility')
        
    def test_analyze_endpoint_missing_text(self):
        """Test analysis with missing text"""
        payload = {
            'group': 'Elderly',
            'category': 'Mobility'
        }
        
        response = self.client.post(
            '/analyze',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        self.assertIn('error', data)
        
    def test_analyze_endpoint_default_values(self):
        """Test analysis with default group and category"""
        payload = {
            'text': self.sample_text
        }
        
        response = self.client.post(
            '/analyze',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['group'], 'People with disabilities')
        self.assertEqual(data['category'], 'Accessibility')
        
    def test_analyze_paper_endpoint(self):
        """Test comprehensive paper analysis"""
        payload = {
            'text': self.sample_text
        }
        
        response = self.client.post(
            '/analyze-paper',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('analysis', data)
        self.assertIn('user_groups', data['analysis'])
        self.assertIn('problem_domains', data['analysis'])
        self.assertIn('key_challenges', data['analysis'])
        
    def test_invalid_endpoint(self):
        """Test requesting an invalid endpoint"""
        response = self.client.get('/invalid-endpoint')
        self.assertEqual(response.status_code, 404)
        
    def test_cors_headers(self):
        """Test that CORS headers are present"""
        response = self.client.get('/health')
        self.assertIn('Access-Control-Allow-Origin', response.headers)

class SummarizerTestCase(unittest.TestCase):
    """Test cases for summarizer module"""
    
    def setUp(self):
        """Set up test data"""
        self.sample_text = """
        Research indicates that elderly users struggle with small text sizes
        and complex navigation systems on mobile devices.
        """
        
    def test_extract_issues_mock(self):
        """Test mock issue extraction"""
        from summarizer import _extract_issues_mock
        
        issues = _extract_issues_mock(
            self.sample_text,
            'Elderly',
            'Accessibility'
        )
        
        self.assertIsInstance(issues, list)
        self.assertGreater(len(issues), 0)
        
        # Check issue structure
        for issue in issues:
            self.assertIn('title', issue)
            self.assertIn('description', issue)
            self.assertIn('severity', issue)
            
    def test_analyze_paper_mock(self):
        """Test mock paper analysis"""
        from summarizer import _analyze_paper_mock
        
        analysis = _analyze_paper_mock(self.sample_text)
        
        self.assertIn('user_groups', analysis)
        self.assertIn('problem_domains', analysis)
        self.assertIn('key_challenges', analysis)
        self.assertIn('recommendations', analysis)

def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(APITestCase))
    suite.addTests(loader.loadTestsFromTestCase(SummarizerTestCase))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("Test Summary")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
