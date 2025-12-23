"""
Main social media manager that coordinates posting across multiple platforms.
"""

from typing import Dict, Any, List, Optional
import logging
from .config import Config, setup_logging
from .instagram_poster import InstagramPoster
from .facebook_poster import FacebookPoster
from .linkedin_poster import LinkedInPoster


class SocialMediaManager:
    """Manages posting to multiple social media platforms."""
    
    def __init__(self, platforms: Optional[List[str]] = None):
        """
        Initialize social media manager.
        
        Args:
            platforms: List of platforms to use. If None, uses all configured platforms.
        """
        self.logger = setup_logging()
        self.posters = {}
        
        # Determine which platforms to initialize
        if platforms is None:
            platforms = Config.get_configured_platforms()
        
        # Initialize posters for specified platforms
        if 'instagram' in platforms:
            self.posters['instagram'] = InstagramPoster()
        
        if 'facebook' in platforms:
            self.posters['facebook'] = FacebookPoster()
        
        if 'linkedin' in platforms:
            self.posters['linkedin'] = LinkedInPoster()
        
        self.logger.info(f"Initialized social media manager with platforms: {list(self.posters.keys())}")
    
    def post_to_all(self, content_type: str, **kwargs) -> Dict[str, Any]:
        """
        Post content to all configured platforms.
        
        Args:
            content_type: Type of content ('text', 'image', 'link')
            **kwargs: Content-specific arguments
            
        Returns:
            Dict containing results from all platforms
        """
        results = {
            'overall_success': True,
            'platforms': {}
        }
        
        for platform_name, poster in self.posters.items():
            try:
                if content_type == 'text':
                    result = poster.post_text(kwargs.get('text', ''))
                elif content_type == 'image':
                    result = poster.post_image(
                        kwargs.get('image_path', ''),
                        kwargs.get('caption', '')
                    )
                elif content_type == 'link':
                    result = poster.post_link(
                        kwargs.get('url', ''),
                        kwargs.get('text', '')
                    )
                else:
                    result = {
                        'success': False,
                        'platform': platform_name,
                        'error': f"Unknown content type: {content_type}"
                    }
                
                results['platforms'][platform_name] = result
                
                if not result.get('success', False):
                    results['overall_success'] = False
                
            except Exception as e:
                self.logger.error(f"Error posting to {platform_name}: {str(e)}")
                results['platforms'][platform_name] = {
                    'success': False,
                    'platform': platform_name,
                    'error': str(e)
                }
                results['overall_success'] = False
        
        return results
    
    def post_text(self, text: str, platforms: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Post text to specified platforms or all platforms.
        
        Args:
            text: Text content to post
            platforms: Optional list of specific platforms to post to
            
        Returns:
            Dict containing results from all platforms
        """
        # Use filtered posters if platforms specified
        posters_to_use = {k: v for k, v in self.posters.items() if k in platforms} if platforms else self.posters
        
        results = {
            'overall_success': True,
            'platforms': {}
        }
        
        for platform_name, poster in posters_to_use.items():
            try:
                result = poster.post_text(text)
                results['platforms'][platform_name] = result
                
                if not result.get('success', False):
                    results['overall_success'] = False
                
            except Exception as e:
                self.logger.error(f"Error posting to {platform_name}: {str(e)}")
                results['platforms'][platform_name] = {
                    'success': False,
                    'platform': platform_name,
                    'error': str(e)
                }
                results['overall_success'] = False
        
        return results
    
    def post_image(self, image_path: str, caption: str = "", 
                   platforms: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Post image with caption to specified platforms or all platforms.
        
        Args:
            image_path: Path to image file
            caption: Caption text for the image
            platforms: Optional list of specific platforms to post to
            
        Returns:
            Dict containing results from all platforms
        """
        # Use filtered posters if platforms specified
        posters_to_use = {k: v for k, v in self.posters.items() if k in platforms} if platforms else self.posters
        
        results = {
            'overall_success': True,
            'platforms': {}
        }
        
        for platform_name, poster in posters_to_use.items():
            try:
                result = poster.post_image(image_path, caption)
                results['platforms'][platform_name] = result
                
                if not result.get('success', False):
                    results['overall_success'] = False
                
            except Exception as e:
                self.logger.error(f"Error posting to {platform_name}: {str(e)}")
                results['platforms'][platform_name] = {
                    'success': False,
                    'platform': platform_name,
                    'error': str(e)
                }
                results['overall_success'] = False
        
        return results
    
    def post_link(self, url: str, text: str = "", 
                  platforms: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Post link with text to specified platforms or all platforms.
        
        Args:
            url: URL to share
            text: Optional text to accompany the link
            platforms: Optional list of specific platforms to post to
            
        Returns:
            Dict containing results from all platforms
        """
        # Use filtered posters if platforms specified
        posters_to_use = {k: v for k, v in self.posters.items() if k in platforms} if platforms else self.posters
        
        results = {
            'overall_success': True,
            'platforms': {}
        }
        
        for platform_name, poster in posters_to_use.items():
            try:
                result = poster.post_link(url, text)
                results['platforms'][platform_name] = result
                
                if not result.get('success', False):
                    results['overall_success'] = False
                
            except Exception as e:
                self.logger.error(f"Error posting to {platform_name}: {str(e)}")
                results['platforms'][platform_name] = {
                    'success': False,
                    'platform': platform_name,
                    'error': str(e)
                }
                results['overall_success'] = False
        
        return results
    
    def get_available_platforms(self) -> List[str]:
        """
        Get list of available platforms.
        
        Returns:
            List of platform names
        """
        return list(self.posters.keys())
