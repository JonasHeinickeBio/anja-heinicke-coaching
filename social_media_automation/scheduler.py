"""
Scheduler for automated social media posts.
"""

import schedule
import time
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import pytz
from .social_media_manager import SocialMediaManager
from .config import Config


class PostScheduler:
    """Scheduler for automated social media posts."""
    
    def __init__(self, config_file: str = "scheduled_posts.json"):
        """
        Initialize post scheduler.
        
        Args:
            config_file: Path to JSON file containing scheduled posts
        """
        self.logger = logging.getLogger(__name__)
        self.config_file = Path(__file__).parent / config_file
        self.manager = SocialMediaManager()
        self.timezone = pytz.timezone(Config.TIMEZONE)
        self.scheduled_posts = []
        
        # Load scheduled posts if config file exists
        if self.config_file.exists():
            self.load_scheduled_posts()
    
    def load_scheduled_posts(self):
        """Load scheduled posts from configuration file."""
        try:
            with open(self.config_file, 'r') as f:
                data = json.load(f)
                self.scheduled_posts = data.get('scheduled_posts', [])
            
            self.logger.info(f"Loaded {len(self.scheduled_posts)} scheduled posts")
            
        except Exception as e:
            self.logger.error(f"Failed to load scheduled posts: {str(e)}")
    
    def save_scheduled_posts(self):
        """Save scheduled posts to configuration file."""
        try:
            data = {'scheduled_posts': self.scheduled_posts}
            
            with open(self.config_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            self.logger.info(f"Saved {len(self.scheduled_posts)} scheduled posts")
            
        except Exception as e:
            self.logger.error(f"Failed to save scheduled posts: {str(e)}")
    
    def add_scheduled_post(self, post_config: Dict[str, Any]):
        """
        Add a new scheduled post.
        
        Args:
            post_config: Dictionary containing post configuration
                - content_type: 'text', 'image', or 'link'
                - schedule: e.g., "09:00" for daily, "Monday 09:00" for weekly
                - platforms: list of platforms or None for all
                - content: dict with content-specific fields
        """
        self.scheduled_posts.append(post_config)
        self.save_scheduled_posts()
        self.logger.info(f"Added scheduled post: {post_config.get('schedule')}")
    
    def remove_scheduled_post(self, index: int):
        """
        Remove a scheduled post by index.
        
        Args:
            index: Index of the post to remove
        """
        if 0 <= index < len(self.scheduled_posts):
            removed = self.scheduled_posts.pop(index)
            self.save_scheduled_posts()
            self.logger.info(f"Removed scheduled post: {removed.get('schedule')}")
        else:
            self.logger.error(f"Invalid index: {index}")
    
    def execute_post(self, post_config: Dict[str, Any]):
        """
        Execute a scheduled post.
        
        Args:
            post_config: Dictionary containing post configuration
        """
        try:
            content_type = post_config.get('content_type')
            platforms = post_config.get('platforms')
            content = post_config.get('content', {})
            
            self.logger.info(f"Executing scheduled post: {content_type} to {platforms or 'all platforms'}")
            
            if content_type == 'text':
                result = self.manager.post_text(
                    text=content.get('text', ''),
                    platforms=platforms
                )
            elif content_type == 'image':
                result = self.manager.post_image(
                    image_path=content.get('image_path', ''),
                    caption=content.get('caption', ''),
                    platforms=platforms
                )
            elif content_type == 'link':
                result = self.manager.post_link(
                    url=content.get('url', ''),
                    text=content.get('text', ''),
                    platforms=platforms
                )
            else:
                self.logger.error(f"Unknown content type: {content_type}")
                return
            
            # Log results
            if result.get('overall_success'):
                self.logger.info("Scheduled post executed successfully")
            else:
                self.logger.warning(f"Scheduled post had errors: {result}")
            
        except Exception as e:
            self.logger.error(f"Failed to execute scheduled post: {str(e)}")
    
    def setup_schedules(self):
        """Setup all scheduled posts with the scheduler."""
        # Day mapping for schedule setup
        day_mapping = {
            'monday': schedule.every().monday,
            'tuesday': schedule.every().tuesday,
            'wednesday': schedule.every().wednesday,
            'thursday': schedule.every().thursday,
            'friday': schedule.every().friday,
            'saturday': schedule.every().saturday,
            'sunday': schedule.every().sunday
        }
        
        for post_config in self.scheduled_posts:
            schedule_str = post_config.get('schedule', '')
            
            # Parse schedule string
            # Format: "HH:MM" for daily, "Day HH:MM" for weekly
            parts = schedule_str.split()
            
            if len(parts) == 1:
                # Daily schedule
                time_str = parts[0]
                schedule.every().day.at(time_str).do(self.execute_post, post_config)
                self.logger.info(f"Scheduled daily post at {time_str}")
                
            elif len(parts) == 2:
                # Weekly schedule
                day, time_str = parts
                day_lower = day.lower()
                
                if day_lower in day_mapping:
                    day_mapping[day_lower].at(time_str).do(self.execute_post, post_config)
                    self.logger.info(f"Scheduled weekly post on {day} at {time_str}")
                else:
                    self.logger.warning(f"Unknown day: {day}. Skipping schedule.")
    
    def run(self):
        """Run the scheduler continuously."""
        self.setup_schedules()
        self.logger.info("Starting scheduler...")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
