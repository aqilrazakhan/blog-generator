# Blog Generator

Automated WordPress blog publishing system with AI-generated images and SEO optimization.

## Features

- **Article Creation** - SEO-optimized blog posts with CSS/HTML diagrams
- **Image Generation** - DALL-E 3 powered images with custom branding
- **WordPress Publishing** - One-command upload to WordPress as draft
- **Multi-Niche Support** - Configurable for any blog topic

## Quick Start

### 1. Setup Credentials

```bash
cp .env.example .env
# Edit .env with your credentials
```

Required credentials:
- `OPENAI_API_KEY` - For DALL-E image generation
- `WORDPRESS_SITE` - Your WordPress URL
- `WORDPRESS_USERNAME` - WordPress login
- `WORDPRESS_APP_PASSWORD` - Application password ([how to get](https://wordpress.com/support/security/two-step-authentication/application-specific-passwords/))
- `BLOG_NAME` - For image watermarks
- `BLOG_NICHE` - Your blog topic

### 2. Install Dependencies

```bash
pip install -r .claude/skills/blog-writer/scripts/requirements.txt
```

### 3. Create Article

```bash
# Using Claude Code
/blog-writer
```

### 4. Generate Images

```bash
python3 .claude/skills/blog-writer/scripts/generate_article_images.py [article-folder]
```

### 5. Publish to WordPress

```bash
python3 .claude/skills/blog-writer/scripts/upload_article_to_wordpress.py [article-folder]
```

## Project Structure

```
blog-generator/
├── .env.example                 # Credentials template
├── CLAUDE.md                    # Claude Code instructions
├── blog-posts/                  # Generated articles
│   └── [article-folder]/
│       ├── article.md
│       ├── article-with-images.md
│       └── images/
└── .claude/skills/
    ├── blog-writer/             # Main skill
    │   ├── SKILL.md
    │   ├── scripts/
    │   │   ├── generate_article_images.py
    │   │   ├── upload_article_to_wordpress.py
    │   │   └── requirements.txt
    │   └── references/
    └── skill-creator/           # Skill creation helper
```

## Cost

- DALL-E 3 images: ~$0.40 per article (5 images)

## Requirements

- Python 3.8+
- OpenAI API key
- WordPress site with REST API enabled
- Claude Code CLI

## License

MIT
