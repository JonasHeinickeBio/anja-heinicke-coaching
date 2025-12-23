"""
Facebook posting functionality using facebook-sdk.
"""

from typing import Dict, Any
from .base_poster import BasePoster
from .config import Config


class FacebookPoster(BasePoster):
    """Facebook posting implementation using facebook-sdk."""
    
    def __init__(self):
        """Initialize Facebook poster."""
        super().__init__("Facebook")
        self.graph = None
        self.access_token = Config.FACEBOOK_ACCESS_TOKEN
        self.page_id = Config.FACEBOOK_PAGE_ID
        self.rate_limit_delay = 3
    
    def authenticate(self) -> bool:
        """
        Authenticate with Facebook using access token.
        
        Returns:
            bool: True if authentication successful, False otherwise
        """
        try:
            import facebook
            
            self.graph = facebook.GraphAPI(access_token=self.access_token, version="3.1")
            
            # Test authentication by getting page info
            self.graph.get_object(id=self.page_id)
            self.logger.info(f"Successfully authenticated with Facebook page {self.page_id}")
            return True
            
        except ImportError:
            self.logger.error("facebook-sdk library not installed. Install with: pip install facebook-sdk")
            return False
        except Exception as e:
            self.logger.error(f"Facebook authentication failed: {str(e)}")
            return False
    
    def post_text(self, text: str) -> Dict[str, Any]:
        """
        Post text content to Facebook page.
        
        Args:
            text: Text content to post
            
        Returns:
            Dict containing post result and metadata
        """
        try:
            if not self.graph:
                if not self.authenticate():
                    return self.handle_error(Exception("Authentication failed"), "post_text")
            
            # Apply rate limiting
            self.apply_rate_limit()
            
            # Post to page
            response = self.graph.put_object(
                parent_object=self.page_id,
                connection_name="feed",
                message=text
            )
            
            return self.create_success_response(
                post_id=response.get('id'),
                message=f"Text post created: {text[:50]}..."
            )
            
        except Exception as e:
            return self.handle_error(e, "post_text")
    
    def post_image(self, image_path: str, caption: str = "") -> Dict[str, Any]:
        """
        Post image with caption to Facebook page.
        
        Args:
            image_path: Path to image file
            caption: Caption text for the image
            
        Returns:
            Dict containing post result and metadata
        """
        try:
            if not self.graph:
                if not self.authenticate():
                    return self.handle_error(Exception("Authentication failed"), "post_image")
            
            # Apply rate limiting
            self.apply_rate_limit()
            
            # Post photo to page
            with open(image_path, 'rb') as image_file:
                response = self.graph.put_photo(
                    image=image_file,
                    album_path=f"{self.page_id}/photos",
                    message=caption
                )
            
            return self.create_success_response(
                post_id=response.get('id'),
                message=f"Image posted with caption: {caption[:50]}..."
            )
            
        except Exception as e:
            return self.handle_error(e, "post_image")
    
    def post_link(self, url: str, text: str = "") -> Dict[str, Any]:
        """
        Post a link with optional text to Facebook page.
        
        Args:
            url: URL to share
            text: Optional text to accompany the link
            
        Returns:
            Dict containing post result and metadata
        """
        try:
            if not self.graph:
                if not self.authenticate():
                    return self.handle_error(Exception("Authentication failed"), "post_link")
            
            # Apply rate limiting
            self.apply_rate_limit()
            
            # Post link to page
            response = self.graph.put_object(
                parent_object=self.page_id,
                connection_name="feed",
                message=text,
                link=url
            )
            
            return self.create_success_response(
                post_id=response.get('id'),
                message=f"Link posted: {url}"
            )
            
        except Exception as e:
            return self.handle_error(e, "post_link")
