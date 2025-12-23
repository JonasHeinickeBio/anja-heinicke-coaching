"""
LinkedIn posting functionality using REST API.
"""

from typing import Dict, Any
import requests
from .base_poster import BasePoster
from .config import Config


class LinkedInPoster(BasePoster):
    """LinkedIn posting implementation using REST API."""
    
    def __init__(self):
        """Initialize LinkedIn poster."""
        super().__init__("LinkedIn")
        self.access_token = Config.LINKEDIN_ACCESS_TOKEN
        self.person_urn = Config.LINKEDIN_PERSON_URN
        self.api_url = "https://api.linkedin.com/v2"
        self.rate_limit_delay = 3
        self.headers = None
    
    def authenticate(self) -> bool:
        """
        Set up authentication headers for LinkedIn API.
        
        Returns:
            bool: True if authentication successful, False otherwise
        """
        try:
            if not self.access_token:
                raise ValueError("LinkedIn access token not configured")
            
            self.headers = {
                'Authorization': f'Bearer {self.access_token}',
                'Content-Type': 'application/json',
                'X-Restli-Protocol-Version': '2.0.0'
            }
            
            # Test authentication by getting user profile
            response = requests.get(
                f"{self.api_url}/me",
                headers=self.headers
            )
            
            if response.status_code == 200:
                self.logger.info("Successfully authenticated with LinkedIn")
                return True
            else:
                raise Exception(f"Authentication failed with status {response.status_code}")
            
        except Exception as e:
            self.logger.error(f"LinkedIn authentication failed: {str(e)}")
            return False
    
    def post_text(self, text: str) -> Dict[str, Any]:
        """
        Post text content to LinkedIn.
        
        Args:
            text: Text content to post
            
        Returns:
            Dict containing post result and metadata
        """
        try:
            if not self.headers:
                if not self.authenticate():
                    return self.handle_error(Exception("Authentication failed"), "post_text")
            
            # Apply rate limiting
            self.apply_rate_limit()
            
            # Prepare post data
            post_data = {
                "author": self.person_urn,
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {
                            "text": text
                        },
                        "shareMediaCategory": "NONE"
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
            }
            
            # Validate person URN is configured
            if not self.person_urn:
                raise ValueError("LinkedIn person URN not configured. Please set LINKEDIN_PERSON_URN in .env file.")
            
            # Post to LinkedIn
            response = requests.post(
                f"{self.api_url}/ugcPosts",
                headers=self.headers,
                json=post_data
            )
            
            if response.status_code in [200, 201]:
                post_id = response.json().get('id', 'unknown')
                return self.create_success_response(
                    post_id=post_id,
                    message=f"Text post created: {text[:50]}..."
                )
            else:
                raise Exception(f"Post failed with status {response.status_code}: {response.text}")
            
        except Exception as e:
            return self.handle_error(e, "post_text")
    
    def post_image(self, image_path: str, caption: str = "") -> Dict[str, Any]:
        """
        Post image with caption to LinkedIn.
        Note: LinkedIn image upload requires multiple API calls and is complex.
        This is a simplified version.
        
        Args:
            image_path: Path to image file
            caption: Caption text for the image
            
        Returns:
            Dict containing post result and metadata
        """
        try:
            # LinkedIn image posting requires:
            # 1. Register upload
            # 2. Upload image binary
            # 3. Create post with image reference
            # This is a simplified error message for now
            
            return self.handle_error(
                Exception("LinkedIn image posting requires complex multi-step process. Use text posts or implement full image upload workflow."),
                "post_image"
            )
            
        except Exception as e:
            return self.handle_error(e, "post_image")
    
    def post_link(self, url: str, text: str = "") -> Dict[str, Any]:
        """
        Post a link with optional text to LinkedIn.
        
        Args:
            url: URL to share
            text: Optional text to accompany the link
            
        Returns:
            Dict containing post result and metadata
        """
        try:
            if not self.headers:
                if not self.authenticate():
                    return self.handle_error(Exception("Authentication failed"), "post_link")
            
            # Apply rate limiting
            self.apply_rate_limit()
            
            # Validate person URN is configured
            if not self.person_urn:
                raise ValueError("LinkedIn person URN not configured. Please set LINKEDIN_PERSON_URN in .env file.")
            
            # Prepare post data with link
            post_data = {
                "author": self.person_urn,
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {
                            "text": text if text else url
                        },
                        "shareMediaCategory": "ARTICLE",
                        "media": [
                            {
                                "status": "READY",
                                "originalUrl": url
                            }
                        ]
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
            }
            
            # Post to LinkedIn
            response = requests.post(
                f"{self.api_url}/ugcPosts",
                headers=self.headers,
                json=post_data
            )
            
            if response.status_code in [200, 201]:
                post_id = response.json().get('id', 'unknown')
                return self.create_success_response(
                    post_id=post_id,
                    message=f"Link posted: {url}"
                )
            else:
                raise Exception(f"Post failed with status {response.status_code}: {response.text}")
            
        except Exception as e:
            return self.handle_error(e, "post_link")
