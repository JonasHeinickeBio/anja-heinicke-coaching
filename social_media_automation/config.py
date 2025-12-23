"""
Configuration module for social media automation.
Loads environment variables and provides configuration settings.
"""

import os
from dotenv import load_dotenv
import logging
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """Configuration class for social media automation."""
    
    # Instagram Configuration
    INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME', '')
    INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD', '')
    
    # Facebook Configuration
    FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')
    FACEBOOK_PAGE_ID = os.getenv('FACEBOOK_PAGE_ID', '')
    
    # LinkedIn Configuration
    LINKEDIN_ACCESS_TOKEN = os.getenv('LINKEDIN_ACCESS_TOKEN', '')
    LINKEDIN_PERSON_URN = os.getenv('LINKEDIN_PERSON_URN', '')
    
    # Scheduling Configuration
    TIMEZONE = os.getenv('TIMEZONE', 'Europe/Berlin')
    POST_SCHEDULE_ENABLED = os.getenv('POST_SCHEDULE_ENABLED', 'false').lower() == 'true'
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'social_media_automation.log')
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        errors = []
        
        if not cls.INSTAGRAM_USERNAME or not cls.INSTAGRAM_PASSWORD:
            errors.append("Instagram credentials not configured")
        
        if not cls.FACEBOOK_ACCESS_TOKEN or not cls.FACEBOOK_PAGE_ID:
            errors.append("Facebook credentials not configured")
        
        if not cls.LINKEDIN_ACCESS_TOKEN:
            errors.append("LinkedIn credentials not configured")
        
        return errors
    
    @classmethod
    def get_configured_platforms(cls):
        """Return list of platforms that are properly configured."""
        platforms = []
        
        if cls.INSTAGRAM_USERNAME and cls.INSTAGRAM_PASSWORD:
            platforms.append('instagram')
        
        if cls.FACEBOOK_ACCESS_TOKEN and cls.FACEBOOK_PAGE_ID:
            platforms.append('facebook')
        
        if cls.LINKEDIN_ACCESS_TOKEN:
            platforms.append('linkedin')
        
        return platforms


def setup_logging():
    """Setup logging configuration."""
    log_level = getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO)
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Config.LOG_FILE),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)
