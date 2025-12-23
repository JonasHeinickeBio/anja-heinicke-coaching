#!/usr/bin/env python3
"""
Example script demonstrating how to use the social media automation system.
"""

import sys
import os

# Add parent directory to path when running from social_media_automation directory
if __name__ == "__main__":
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

from social_media_automation.social_media_manager import SocialMediaManager
from social_media_automation.scheduler import PostScheduler
from social_media_automation.config import Config


def example_manual_post():
    """Example: Manually post to social media platforms."""
    print("=== Manual Posting Example ===\n")
    
    # Check which platforms are configured
    platforms = Config.get_configured_platforms()
    print(f"Configured platforms: {platforms}\n")
    
    if not platforms:
        print("No platforms configured. Please set up credentials in .env file.")
        return
    
    # Initialize manager
    manager = SocialMediaManager()
    
    # Example 1: Post text to all platforms
    print("Posting text to all platforms...")
    result = manager.post_text(
        "Neue Coaching-Angebote verfügbar! 🌟 Kontaktiere mich für weitere Informationen. #Coaching #Selfcare"
    )
    print(f"Result: {result}\n")
    
    # Example 2: Post image to specific platforms
    print("Posting image to Instagram and Facebook...")
    result = manager.post_image(
        image_path="/path/to/image.jpg",
        caption="Entspannung und Selbstfindung in der Natur 🌿 #Retreat #Coaching",
        platforms=['instagram', 'facebook']
    )
    print(f"Result: {result}\n")
    
    # Example 3: Post link to LinkedIn and Facebook
    print("Posting link to LinkedIn and Facebook...")
    result = manager.post_link(
        url="https://anjaheinicke.de/retreat.html",
        text="Entdecke unsere Coaching-Retreats in der Toskana!",
        platforms=['linkedin', 'facebook']
    )
    print(f"Result: {result}\n")


def example_scheduled_posts():
    """Example: Set up scheduled posts."""
    print("=== Scheduled Posts Example ===\n")
    
    # Initialize scheduler
    scheduler = PostScheduler()
    
    # Add a new scheduled post
    print("Adding a new scheduled post...")
    scheduler.add_scheduled_post({
        "content_type": "text",
        "schedule": "Monday 10:00",
        "platforms": ["facebook", "linkedin"],
        "content": {
            "text": "Guten Morgen! Starte die Woche mit positiver Energie! 💪 #Motivation #Coaching"
        }
    })
    
    print("Scheduled posts added. To run the scheduler, use the run_scheduler() function.\n")


def run_scheduler():
    """Run the scheduler continuously."""
    print("=== Starting Scheduler ===\n")
    print("The scheduler will now run continuously and execute posts at scheduled times.")
    print("Press Ctrl+C to stop.\n")
    
    scheduler = PostScheduler()
    
    try:
        scheduler.run()
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


def show_menu():
    """Show interactive menu."""
    print("\n" + "="*50)
    print("Social Media Automation - Example Usage")
    print("="*50)
    print("\n1. Manual posting example")
    print("2. Scheduled posts example")
    print("3. Run scheduler")
    print("4. Show configured platforms")
    print("5. Exit")
    print("\n" + "="*50)


def main():
    """Main function with interactive menu."""
    
    # Check if .env file exists
    from pathlib import Path
    script_dir = Path(__file__).parent
    env_file = script_dir / '.env'
    
    if not env_file.exists():
        print("\n⚠️  WARNING: .env file not found!")
        print("Please copy .env.example to .env and configure your credentials.")
        print(f"Expected location: {env_file}\n")
    
    while True:
        show_menu()
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            example_manual_post()
            input("\nPress Enter to continue...")
        elif choice == '2':
            example_scheduled_posts()
            input("\nPress Enter to continue...")
        elif choice == '3':
            run_scheduler()
        elif choice == '4':
            platforms = Config.get_configured_platforms()
            print(f"\nConfigured platforms: {platforms}")
            if not platforms:
                print("No platforms configured. Please set up credentials in .env file.")
            input("\nPress Enter to continue...")
        elif choice == '5':
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()
