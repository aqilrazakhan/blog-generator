# Troubleshooting Guide

## Common Issues

### "OPENAI_API_KEY not set"

**Cause:** Environment variable not configured

**Solution:**
```bash
# Check .env file exists
ls -la .env

# Verify format (value should NOT have quotes in actual file)
cat .env

# Correct format in .env:
OPENAI_API_KEY=sk-proj-your-actual-key-here
```

---

### "WordPress authentication failed"

**Cause:** Invalid credentials or URL format

**Solution:**
1. Verify WordPress site URL starts with `https://`
2. Check username is correct (case-sensitive)
3. Ensure app password has **NO SPACES**

```bash
# Wrong (has spaces):
WORDPRESS_APP_PASSWORD=K3ft vMCM HO1v ZIn6 u5N1 ngDx

# Correct (no spaces):
WORDPRESS_APP_PASSWORD=K3ftvMCMHO1vZIn6u5N1ngDx
```

**Getting Application Password:**
1. WordPress Dashboard → Users → Your Profile
2. Scroll to "Application Passwords"
3. Enter name: "Blog Publishing API"
4. Click "Add New Application Password"
5. Copy and remove all spaces

---

### "Module not found"

**Cause:** Python dependencies not installed

**Solution:**
```bash
cd blog-posts
pip install -r requirements.txt

# Or install directly:
pip install openai requests python-dotenv
```

---

### "Images not uploading to WordPress"

**Cause:** Various WordPress restrictions

**Solutions:**
1. Check image file size (usually max 10MB)
2. Verify WordPress allows PNG uploads (Media → Add New)
3. Check WordPress storage quota
4. Ensure REST API is not blocked by security plugins

---

### "No image prompts defined for article"

**Cause:** DALL-E prompts not added to script

**Solution:**
Edit `generate_article_images.py` and add prompts to `ARTICLE_PROMPTS` dictionary:

```python
ARTICLE_PROMPTS = {
    "your-article-folder": {
        "featured": {
            "filename": "featured-image.png",
            "prompt": "Your DALL-E prompt here...",
            "section": "Header"
        }
    }
}
```

---

### "Article folder not found"

**Cause:** Path mismatch

**Solution:**
```bash
# List available article folders
ls blog-posts/

# Use exact folder name
python3 generate_article_images.py 01-exact-folder-name
```

---

## Configuration Checklist

```bash
# .env file should contain:
OPENAI_API_KEY=sk-proj-...
WORDPRESS_SITE=https://yourblog.com
WORDPRESS_USERNAME=your_username
WORDPRESS_APP_PASSWORD=yourapppasswordnospaces
BLOG_NAME=Your Blog Name
BLOG_NICHE=Your Topic Area
```

---

## Testing Credentials

### Test OpenAI API Key:
```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("OpenAI API key is valid!" if client.models.list() else "Invalid key")
```

### Test WordPress Credentials:
```bash
curl -u "username:app_password" https://yourblog.com/wp-json/wp/v2/posts
```

---

## Cost Summary

| Item | Cost |
|------|------|
| Article creation | $0.00 |
| DALL-E images (5) | $0.40 |
| WordPress publishing | $0.00 |
| **Total per article** | **$0.40** |
