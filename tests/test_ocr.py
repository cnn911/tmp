import unittest
from unittest.mock import Mock, patch, MagicMock
import io
import sys
import os

# Add the parent directory to the path to import ocr module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ocr import Request


class TestOCRRequest(unittest.TestCase):
    """Test suite for the OCR HTTP request handler."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.request_handler = Request(Mock(), ('127.0.0.1', 8888), Mock())
        
    def test_do_GET_response_code(self):
        """Test that GET request returns 200 status code."""
        with patch.object(self.request_handler, 'send_response') as mock_send_response, \
             patch.object(self.request_handler, 'send_header') as mock_send_header, \
             patch.object(self.request_handler, 'end_headers') as mock_end_headers, \
             patch.object(self.request_handler, 'wfile') as mock_wfile:
            
            mock_wfile.write = Mock()
            
            self.request_handler.do_GET()
            
            mock_send_response.assert_called_once_with(200)
            mock_send_header.assert_called_once_with("type", "get")
            mock_end_headers.assert_called_once()
            
    def test_do_GET_response_content(self):
        """Test that GET request returns correct content."""
        with patch.object(self.request_handler, 'send_response'), \
             patch.object(self.request_handler, 'send_header'), \
             patch.object(self.request_handler, 'end_headers'), \
             patch.object(self.request_handler, 'wfile') as mock_wfile:
            
            mock_wfile.write = Mock()
            
            self.request_handler.do_GET()
            
            # Should write "123" as bytes
            mock_wfile.write.assert_called_once_with(b'123')
            
    def test_do_POST_response_code(self):
        """Test that POST request returns 200 status code."""
        mock_rfile = Mock()
        mock_rfile.read.return_value = b'5'
        
        with patch.object(self.request_handler, 'rfile', mock_rfile), \
             patch.object(self.request_handler, 'headers', {'content-length': '1'}), \
             patch.object(self.request_handler, 'send_response') as mock_send_response, \
             patch.object(self.request_handler, 'send_header') as mock_send_header, \
             patch.object(self.request_handler, 'end_headers') as mock_end_headers, \
             patch.object(self.request_handler, 'wfile') as mock_wfile:
            
            mock_wfile.write = Mock()
            
            self.request_handler.do_POST()
            
            mock_send_response.assert_called_once_with(200)
            mock_send_header.assert_called_once_with("type", "post")
            mock_end_headers.assert_called_once()
            
    def test_do_POST_calculation(self):
        """Test that POST request correctly doubles the input value."""
        mock_rfile = Mock()
        mock_rfile.read.return_value = b'7'
        
        with patch.object(self.request_handler, 'rfile', mock_rfile), \
             patch.object(self.request_handler, 'headers', {'content-length': '1'}), \
             patch.object(self.request_handler, 'send_response'), \
             patch.object(self.request_handler, 'send_header'), \
             patch.object(self.request_handler, 'end_headers'), \
             patch.object(self.request_handler, 'wfile') as mock_wfile:
            
            mock_wfile.write = Mock()
            
            self.request_handler.do_POST()
            
            # Should write "14" (7*2) as bytes
            mock_wfile.write.assert_called_once_with(b'14')
            
    def test_do_POST_with_zero(self):
        """Test POST request with zero input."""
        mock_rfile = Mock()
        mock_rfile.read.return_value = b'0'
        
        with patch.object(self.request_handler, 'rfile', mock_rfile), \
             patch.object(self.request_handler, 'headers', {'content-length': '1'}), \
             patch.object(self.request_handler, 'send_response'), \
             patch.object(self.request_handler, 'send_header'), \
             patch.object(self.request_handler, 'end_headers'), \
             patch.object(self.request_handler, 'wfile') as mock_wfile:
            
            mock_wfile.write = Mock()
            
            self.request_handler.do_POST()
            
            # Should write "0" (0*2) as bytes
            mock_wfile.write.assert_called_once_with(b'0')
            
    def test_do_POST_with_negative_number(self):
        """Test POST request with negative input."""
        mock_rfile = Mock()
        mock_rfile.read.return_value = b'-3'
        
        with patch.object(self.request_handler, 'rfile', mock_rfile), \
             patch.object(self.request_handler, 'headers', {'content-length': '2'}), \
             patch.object(self.request_handler, 'send_response'), \
             patch.object(self.request_handler, 'send_header'), \
             patch.object(self.request_handler, 'end_headers'), \
             patch.object(self.request_handler, 'wfile') as mock_wfile:
            
            mock_wfile.write = Mock()
            
            self.request_handler.do_POST()
            
            # Should write "-6" (-3*2) as bytes
            mock_wfile.write.assert_called_once_with(b'-6')
            
    def test_class_attributes(self):
        """Test that class attributes are set correctly."""
        self.assertEqual(Request.timeout, 5)
        self.assertEqual(Request.server_version, 'Apache')


if __name__ == '__main__':
    unittest.main()