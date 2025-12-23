"""
Base class for social media posting functionality.
"""

import logging
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import time


class BasePoster(ABC):
    """Abstract base class for social media posters."""
    
    def __init__(self, platform_name: str):
        """
        Initialize base poster.
        
        Args:
            platform_name: Name of the social media platform
        """
        self.platform_name = platform_name
        self.logger = logging.getLogger(f"{__name__}.{platform_name}")
        self.rate_limit_delay = 2  # Default delay between posts in seconds
    
    @abstractmethod
    def authenticate(self) -> bool:
        """
        Authenticate with the social media platform.
        
        Returns:
            bool: True if authentication successful, False otherwise
        """
        pass
    
    @abstractmethod
    def post_text(self, text: str) -> Dict[str, Any]:
        """
        Post text content to the platform.
        
        Args:
            text: Text content to post
            
        Returns:
            Dict containing post result and metadata
        """
        pass
    
    @abstractmethod
    def post_image(self, image_path: str, caption: str = "") -> Dict[str, Any]:
        """
        Post image with optional caption to the platform.
        
        Args:
            image_path: Path to image file
            caption: Optional caption text
            
        Returns:
            Dict containing post result and metadata
        """
        pass
    
    @abstractmethod
    def post_link(self, url: str, text: str = "") -> Dict[str, Any]:
        """
        Post a link with optional text to the platform.
        
        Args:
            url: URL to share
            text: Optional text to accompany the link
            
        Returns:
            Dict containing post result and metadata
        """
        pass
    
    def apply_rate_limit(self):
        """Apply rate limiting delay."""
        time.sleep(self.rate_limit_delay)
    
    def handle_error(self, error: Exception, operation: str) -> Dict[str, Any]:
        """
        Handle errors in a standardized way.
        
        Args:
            error: The exception that occurred
            operation: Description of the operation that failed
            
        Returns:
            Dict containing error information
        """
        error_msg = f"{self.platform_name} - {operation} failed: {str(error)}"
        self.logger.error(error_msg, exc_info=True)
        
        return {
            'success': False,
            'platform': self.platform_name,
            'error': str(error),
            'operation': operation
        }
    
    def create_success_response(self, post_id: Optional[str] = None, 
                               message: str = "Post created successfully") -> Dict[str, Any]:
        """
        Create a standardized success response.
        
        Args:
            post_id: Optional ID of the created post
            message: Success message
            
        Returns:
            Dict containing success information
        """
        self.logger.info(f"{self.platform_name} - {message}")
        
        response = {
            'success': True,
            'platform': self.platform_name,
            'message': message
        }
        
        if post_id:
            response['post_id'] = post_id
        
        return response
