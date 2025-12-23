# Social Media Automation for Anja Heinicke Coaching

This directory contains a complete social media automation system for posting to Instagram, Facebook, and LinkedIn. The system supports both manual and scheduled automated posting.

## Features

- ✅ Multi-platform support (Instagram, Facebook, LinkedIn)
- ✅ Automated scheduled posting
- ✅ Manual posting with simple API
- ✅ Secure credential management via .env
- ✅ Rate limiting and error handling
- ✅ Comprehensive logging
- ✅ Post scheduling with cron-like syntax

## Installation

### 1. Install Python Dependencies

```bash
cd social_media_automation
pip install -r requirements.txt
```

### 2. Configure Credentials

Copy the example environment file and add your credentials:

```bash
cp .env.example .env
```

Edit `.env` and add your API credentials:

```bash
# Instagram Credentials
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password

# Facebook/Meta Credentials
FACEBOOK_ACCESS_TOKEN=your_facebook_access_token
FACEBOOK_PAGE_ID=your_facebook_page_id

# LinkedIn Credentials
LINKEDIN_ACCESS_TOKEN=your_linkedin_access_token
LINKEDIN_PERSON_URN=your_linkedin_person_urn
```

## Getting API Credentials

### Instagram
- Instagram uses username/password authentication via the `instagrapi` library
- Use your regular Instagram account credentials
- **Note**: Consider using a dedicated business account for automation

### Facebook
1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Create an app and get your **Page Access Token**
3. Find your **Page ID** in your Facebook Page settings

### LinkedIn
1. Go to [LinkedIn Developers](https://www.linkedin.com/developers/)
2. Create an app and request OAuth access
3. Get your **Access Token** and **Person URN**

## Usage

### Interactive Example Script

Run the example script for an interactive menu:

```bash
cd social_media_automation
python example_usage.py
```

### Manual Posting (Python API)

```python
from social_media_automation.social_media_manager import SocialMediaManager

# Initialize manager
manager = SocialMediaManager()

# Post text to all platforms
manager.post_text("Hello from the coaching platform! 🌟")

# Post image with caption to specific platforms
manager.post_image(
    image_path="/path/to/image.jpg",
    caption="Beautiful retreat location 🌿",
    platforms=['instagram', 'facebook']
)

# Post link
manager.post_link(
    url="https://anjaheinicke.de/retreat.html",
    text="Check out our retreat offerings!",
    platforms=['facebook', 'linkedin']
)
```

### Scheduled Automated Posting

#### Configure Scheduled Posts

Edit `scheduled_posts.json` to define your automated posts:

```json
{
  "scheduled_posts": [
    {
      "content_type": "text",
      "schedule": "Monday 09:00",
      "platforms": ["facebook", "linkedin"],
      "content": {
        "text": "Start your week with positive energy! 💪"
      }
    },
    {
      "content_type": "image",
      "schedule": "Wednesday 15:00",
      "platforms": ["instagram", "facebook"],
      "content": {
        "image_path": "/path/to/image.jpg",
        "caption": "Midweek inspiration 🌟"
      }
    }
  ]
}
```

#### Run the Scheduler

Start the scheduler to run automated posts:

```python
from social_media_automation.scheduler import PostScheduler

scheduler = PostScheduler()
scheduler.run()  # Runs continuously
```

Or use the example script:

```bash
python example_usage.py
# Select option 3: Run scheduler
```

## Schedule Format

- **Daily**: `"HH:MM"` - e.g., `"09:00"` posts daily at 9 AM
- **Weekly**: `"Day HH:MM"` - e.g., `"Monday 09:00"` posts every Monday at 9 AM

Supported days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

## Platform-Specific Notes

### Instagram
- **Text-only posts**: Not supported (use post_image with caption)
- **Links**: Not clickable in posts (use bio or stories)
- **Stories**: Available via `InstagramPoster.post_story()`
- **Rate limiting**: 5-second delay between posts

### Facebook
- **All content types supported**: text, images, links
- **Page posting**: Posts to your Facebook Page, not personal profile
- **Rate limiting**: 3-second delay between posts

### LinkedIn
- **Text and links**: Fully supported
- **Images**: Requires complex multi-step upload (simplified in current version)
- **Rate limiting**: 3-second delay between posts

## Error Handling

The system includes comprehensive error handling:

- Authentication failures are logged and reported
- Rate limiting is automatically applied
- Failed posts return detailed error information
- Logs are written to `social_media_automation.log`

## Logging

Logs are written to both console and file:

```bash
# View logs
tail -f social_media_automation.log
```

Configure logging in `.env`:

```bash
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
LOG_FILE=social_media_automation.log
```

## Security Best Practices

1. **Never commit `.env` file** - It's already in `.gitignore`
2. **Use strong passwords** - Especially for Instagram accounts
3. **Rotate tokens regularly** - Update API tokens periodically
4. **Monitor usage** - Check logs for unauthorized access
5. **Use dedicated accounts** - Consider separate accounts for automation
6. **Review platform policies** - Ensure compliance with each platform's automation policies

## Compliance & Platform Policies

⚠️ **Important**: Always comply with platform policies:

- **Instagram**: Review [Instagram Platform Policy](https://www.facebook.com/help/instagram/477434105621119)
- **Facebook**: Review [Facebook Platform Policy](https://developers.facebook.com/docs/development/release/policy-updates)
- **LinkedIn**: Review [LinkedIn API Terms of Use](https://legal.linkedin.com/api-terms-of-use)

Excessive automation may result in account suspension. Use responsibly.

## Troubleshooting

### Authentication Fails
- Check credentials in `.env` file
- Verify API tokens haven't expired
- Check if 2FA is enabled (may need app-specific passwords)

### Posts Not Appearing
- Check platform rate limits
- Verify account permissions
- Review logs for error messages

### Scheduler Not Running
- Ensure `POST_SCHEDULE_ENABLED=true` in `.env`
- Check timezone setting matches your location
- Verify scheduled_posts.json format is correct

## Production Deployment

### Using Cron (Linux/macOS)

Add to crontab to run scheduler on system startup:

```bash
@reboot cd /path/to/social_media_automation && python example_usage.py
```

### Using systemd (Linux)

Create a systemd service for continuous operation:

```ini
[Unit]
Description=Social Media Automation Scheduler
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/social_media_automation
ExecStart=/usr/bin/python3 example_usage.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### Using Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "example_usage.py"]
```

## File Structure

```
social_media_automation/
├── __init__.py                 # Package initialization
├── base_poster.py              # Abstract base class for posters
├── config.py                   # Configuration and environment management
├── facebook_poster.py          # Facebook posting implementation
├── instagram_poster.py         # Instagram posting implementation
├── linkedin_poster.py          # LinkedIn posting implementation
├── social_media_manager.py     # Main manager coordinating all platforms
├── scheduler.py                # Automated post scheduling
├── example_usage.py            # Example usage and interactive menu
├── requirements.txt            # Python dependencies
├── .env.example                # Example environment configuration
├── scheduled_posts.json        # Scheduled post configuration
└── README.md                   # This file
```

## Support

For questions or issues:
1. Check logs for error messages
2. Review platform-specific documentation
3. Ensure credentials are correctly configured
4. Verify API rate limits haven't been exceeded

## License

This software is provided for the Anja Heinicke Coaching website. Use responsibly and in compliance with all platform policies.
