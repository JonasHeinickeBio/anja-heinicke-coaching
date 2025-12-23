"""
Instagram posting functionality using instagrapi.
"""

from typing import Dict, Any
from .base_poster import BasePoster
from .config import Config


class InstagramPoster(BasePoster):
    """Instagram posting implementation using instagrapi."""
    
    def __init__(self):
        """Initialize Instagram poster."""
        super().__init__("Instagram")
        self.client = None
        self.username = Config.INSTAGRAM_USERNAME
        self.password = Config.INSTAGRAM_PASSWORD
        self.rate_limit_delay = 5  # Instagram requires longer delays
    
    def authenticate(self) -> bool:
        """
        Authenticate with Instagram using instagrapi.
        
        Returns:
            bool: True if authentication successful, False otherwise
        """
        try:
            from instagrapi import Client
            
            self.client = Client()
            self.client.login(self.username, self.password)
            self.logger.info(f"Successfully authenticated with Instagram as {self.username}")
            return True
            
        except ImportError:
            self.logger.error("instagrapi library not installed. Install with: pip install instagrapi")
            return False
        except Exception as e:
            self.logger.error(f"Instagram authentication failed: {str(e)}")
            return False
    
    def post_text(self, text: str) -> Dict[str, Any]:
        """
        Post text content to Instagram.
        Note: Instagram doesn't support text-only posts. This will return an error.
        
        Args:
            text: Text content to post
            
        Returns:
            Dict containing post result and metadata
        """
        return self.handle_error(
            Exception("Instagram does not support text-only posts. Use post_image with caption instead."),
            "post_text"
        )
    
    def post_image(self, image_path: str, caption: str = "") -> Dict[str, Any]:
        """
        Post image with caption to Instagram.
        
        Args:
            image_path: Path to image file
            caption: Caption text for the image
            
        Returns:
            Dict containing post result and metadata
        """
        try:
            if not self.client:
                if not self.authenticate():
                    return self.handle_error(Exception("Authentication failed"), "post_image")
            
            # Apply rate limiting
            self.apply_rate_limit()
            
            # Upload photo
            media = self.client.photo_upload(image_path, caption)
            
            return self.create_success_response(
                post_id=str(media.pk),
                message=f"Image posted successfully with caption: {caption[:50]}..."
            )
            
        except Exception as e:
            return self.handle_error(e, "post_image")
    
    def post_link(self, url: str, text: str = "") -> Dict[str, Any]:
        """
        Post a link to Instagram.
        Note: Instagram doesn't support clickable links in posts. 
        Links can only be added to stories or bio.
        
        Args:
            url: URL to share
            text: Optional text to accompany the link
            
        Returns:
            Dict containing post result and metadata
        """
        return self.handle_error(
            Exception("Instagram does not support clickable links in posts. Consider adding to story or bio."),
            "post_link"
        )
    
    def post_story(self, image_path: str, link: str = "") -> Dict[str, Any]:
        """
        Post a story to Instagram with optional link.
        
        Args:
            image_path: Path to image file
            link: Optional link to add to story (requires verified account)
            
        Returns:
            Dict containing post result and metadata
        """
        try:
            if not self.client:
                if not self.authenticate():
                    return self.handle_error(Exception("Authentication failed"), "post_story")
            
            # Apply rate limiting
            self.apply_rate_limit()
            
            # Upload story
            media = self.client.photo_upload_to_story(image_path)
            
            return self.create_success_response(
                post_id=str(media.pk),
                message="Story posted successfully"
            )
            
        except Exception as e:
            return self.handle_error(e, "post_story")
