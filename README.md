# anja-heinicke-coaching
Systemische Therapeutin, Supervisorin &amp; Coach mit Schwerpunkt auf Coaching in der Natur und Kleinstgruppen-Retreats. Ich begleite Frauen in der Lebensmitte bei Burnout, Selfcare, Grenzen ziehen und Neuorientierung. Neben online Einzelcoachings biete ich 5-tägige Retreats in einem kleinen toskanischen Dorf an.

## Social Media Automation

This repository includes an automated social media posting system for promoting coaching content, retreats, and updates across multiple platforms.

### Features
- ✅ **Multi-platform support**: Instagram, Facebook, LinkedIn
- ✅ **Automated scheduling**: Schedule posts in advance
- ✅ **Manual posting**: Post immediately via Python API
- ✅ **Secure credential management**: Uses `.env` for secrets
- ✅ **Rate limiting & error handling**: Built-in safety features
- ✅ **Comprehensive logging**: Track all posting activity

### Quick Start

1. **Install dependencies**:
   ```bash
   cd social_media_automation
   pip install -r requirements.txt
   ```

2. **Configure credentials**:
   ```bash
   cp social_media_automation/.env.example social_media_automation/.env
   # Edit .env with your API credentials
   ```

3. **Run example script**:
   ```bash
   cd social_media_automation
   python example_usage.py
   ```

For detailed documentation, see [social_media_automation/README.md](social_media_automation/README.md).
