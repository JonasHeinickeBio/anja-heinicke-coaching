#!/usr/bin/env python3
"""
Validation test script to verify all components work correctly.
"""

import sys
import os

# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

def test_imports():
    """Test that all modules can be imported."""
    print("Testing module imports...")
    
    from social_media_automation.config import Config
    from social_media_automation.base_poster import BasePoster
    from social_media_automation.social_media_manager import SocialMediaManager
    from social_media_automation.instagram_poster import InstagramPoster
    from social_media_automation.facebook_poster import FacebookPoster
    from social_media_automation.linkedin_poster import LinkedInPoster
    from social_media_automation.scheduler import PostScheduler
    
    print("✓ All modules imported successfully")
    return True

def test_manager_initialization():
    """Test SocialMediaManager initialization."""
    print("\nTesting SocialMediaManager initialization...")
    
    from social_media_automation.social_media_manager import SocialMediaManager
    
    manager = SocialMediaManager()
    platforms = manager.get_available_platforms()
    
    print(f"✓ Manager initialized with {len(platforms)} platforms: {platforms}")
    return True

def test_scheduler_initialization():
    """Test PostScheduler initialization."""
    print("\nTesting PostScheduler initialization...")
    
    from social_media_automation.scheduler import PostScheduler
    
    scheduler = PostScheduler()
    posts = scheduler.scheduled_posts
    
    print(f"✓ Scheduler initialized with {len(posts)} scheduled posts")
    
    if posts:
        print("  Scheduled posts:")
        for i, post in enumerate(posts, 1):
            print(f"    {i}. {post.get('content_type')} at {post.get('schedule')}")
    
    return True

def test_config():
    """Test configuration loading."""
    print("\nTesting configuration...")
    
    from social_media_automation.config import Config
    
    platforms = Config.get_configured_platforms()
    print(f"✓ Configuration loaded")
    print(f"  Configured platforms: {platforms if platforms else 'None (credentials not set)'}")
    print(f"  Timezone: {Config.TIMEZONE}")
    print(f"  Log level: {Config.LOG_LEVEL}")
    
    return True

def test_base_poster():
    """Test base poster functionality."""
    print("\nTesting base poster...")
    
    from social_media_automation.instagram_poster import InstagramPoster
    
    # Create poster (without authenticating)
    poster = InstagramPoster()
    
    print(f"✓ Base poster functionality works")
    print(f"  Platform: {poster.platform_name}")
    print(f"  Rate limit delay: {poster.rate_limit_delay}s")
    
    return True

def main():
    """Run all validation tests."""
    print("="*60)
    print("Social Media Automation - Validation Tests")
    print("="*60)
    
    tests = [
        test_imports,
        test_manager_initialization,
        test_scheduler_initialization,
        test_config,
        test_base_poster
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test failed: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60)
    
    if failed == 0:
        print("\n✅ All validation tests passed!")
        print("\nNext steps:")
        print("1. Copy .env.example to .env")
        print("2. Configure your API credentials in .env")
        print("3. Run: python example_usage.py")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
