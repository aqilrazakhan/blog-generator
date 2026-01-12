---
name: blog-writer
description: Write comprehensive, SEO-optimized blog posts with automated image generation and WordPress publishing. Use when user wants to write blog posts, create articles, publish to WordPress, generate blog content, or needs help with blog writing. Supports any blog niche and WordPress site. Triggers include requests like "write a blog post", "create an article about X", "publish to my blog", or "/blog-writer".
---

# Blog Writer & Publisher

Complete blog publishing pipeline: article creation → DALL-E images → WordPress publishing.

## Workflow Overview

1. **Configuration** - Gather credentials and blog settings
2. **Topic Selection** - User provides or Claude suggests topics
3. **Research** - WebSearch for current information
4. **Writing** - Create SEO-optimized article with professional HTML/CSS styling
5. **Image Generation** - Create DALL-E prompts and generate images
6. **WordPress Publishing** - Upload as draft

---

## Step 1: Configuration

Check for existing `.env` file at project root. If missing, use AskUserQuestion to gather:

**Required credentials:**
- `OPENAI_API_KEY` - For DALL-E image generation
- `WORDPRESS_SITE` - WordPress URL (https://...)
- `WORDPRESS_USERNAME` - WordPress login
- `WORDPRESS_APP_PASSWORD` - Application password (no spaces)
- `BLOG_NAME` - For image watermarks
- `BLOG_NICHE` - Topic focus area

**Create .env file:**
```bash
OPENAI_API_KEY=sk-proj-your-key
WORDPRESS_SITE=https://yourblog.com
WORDPRESS_USERNAME=your_username
WORDPRESS_APP_PASSWORD=yourapppassword
BLOG_NAME=Your Blog Name
BLOG_NICHE=Your Topic Area
```

**Create .gitignore:**
```bash
echo ".env" >> .gitignore
```

---

## Step 2: Topic Selection

Use AskUserQuestion:
1. "I have a specific topic" → User provides topic
2. "Suggest topics for my blog" → Propose 5 topics based on BLOG_NICHE
3. "Continue from previous article" → Check existing articles for numbering

---

## Step 3: Research

Use WebSearch to find:
- Latest developments (2025/2026)
- Current framework versions
- Real-world examples
- Industry statistics

Check existing articles (Glob/Grep) to avoid duplication.

---

## Step 4: Article Creation

**Create folder structure:**
```
blog-posts/{NUMBER}-{SLUG}/
├── article.md
├── article-with-images.md
├── IMAGE-SPECIFICATIONS.md
├── README.md
└── images/
```

**Article requirements:**
- 1,500-3,000 words
- SEO title under 60 characters
- Meta description 150-155 characters
- 5+ H2 headings
- 4-6 styled HTML/CSS components (NO Mermaid - WordPress doesn't support it)
- Category and 3-8 tags

**For detailed template:** See [references/article-template.md](references/article-template.md)

**IMPORTANT: Use HTML/CSS instead of Mermaid**

WordPress does not render Mermaid diagrams. Use inline HTML/CSS for visual elements:

**Color scheme:**
- Blue `#4A90E2` - Primary
- Green `#27AE60` - Success
- Orange `#F39C12` - Warning
- Red `#E74C3C` - Error
- Purple `#9B59B6` - Special
- Gold `#F5A623` - Input/Output
- Dark `#1a1a2e` - Background

---

## Step 5: Image Generation

**Create 5 DALL-E prompts:**
1. Featured image (1792x1024)
2. Section images 1-4 (1792x1024)

**CRITICAL:** Include blog branding in every prompt:
```
Bottom right corner contains the text '{BLOG_NAME}' in white modern sans-serif font.
```

**Add prompts to script:**
Edit `.claude/skills/blog-writer/scripts/generate_article_images.py` and add to `ARTICLE_PROMPTS`:

```python
ARTICLE_PROMPTS = {
    "{ARTICLE_FOLDER}": {
        "featured": {
            "filename": "featured-image.png",
            "prompt": "Your detailed prompt... Bottom right corner contains the text '{BLOG_NAME}' in white modern sans-serif font.",
            "section": "Header"
        },
        # ... 4 more images
    }
}
```

**Run generation:**
```bash
pip install -r .claude/skills/blog-writer/scripts/requirements.txt  # First time only
python3 .claude/skills/blog-writer/scripts/generate_article_images.py {ARTICLE_FOLDER}
```

**For detailed image guide:** See [references/image-guide.md](references/image-guide.md)

---

## Step 6: WordPress Publishing

**Prepare article:**
```bash
cp article.md article-with-images.md
```

**Upload to WordPress:**
```bash
python3 .claude/skills/blog-writer/scripts/upload_article_to_wordpress.py {ARTICLE_FOLDER}
```

**What happens:**
1. Uploads images to WordPress Media Library
2. Replaces local paths with WordPress URLs
3. Converts markdown to HTML
4. Creates/assigns category and tags
5. Sets featured image
6. Creates post as **DRAFT**
7. Returns edit URL

---

## Step 7: Delivery

Provide completion summary:

```
Article Complete!

Details:
   - Words: {COUNT}
   - Styled components: {COUNT}
   - Images: 5/5
   - Status: WordPress DRAFT

Files:
   - article.md
   - article-with-images.md
   - images/ (5 DALL-E images)

WordPress Edit URL:
   {EDIT_URL}

Cost: $0.40 (DALL-E images)

Next: Review draft -> Check SEO -> Publish
```

---

## Bundled Resources

### Scripts (`scripts/`)

| Script | Purpose |
|--------|---------|
| `generate_article_images.py` | DALL-E image generation |
| `upload_article_to_wordpress.py` | WordPress REST API upload |
| `requirements.txt` | Python dependencies |

### References (`references/`)

| File | Content |
|------|---------|
| `article-template.md` | Article structure, HTML/CSS components |
| `image-guide.md` | DALL-E prompts and image specs |
| `troubleshooting.md` | Common issues and solutions |

---

## Quick Reference

```bash
# Setup (one time)
cd project-root
# Create .env with credentials (see .env.example)
pip install -r .claude/skills/blog-writer/scripts/requirements.txt

# Create article
/blog-writer

# Generate images
python3 .claude/skills/blog-writer/scripts/generate_article_images.py {FOLDER}

# Publish
python3 .claude/skills/blog-writer/scripts/upload_article_to_wordpress.py {FOLDER}
```

---

## Troubleshooting

**Common issues:** See [references/troubleshooting.md](references/troubleshooting.md)

**Quick fixes:**
- "API key not set" → Check `.env` file exists at project root and has correct format
- "WordPress auth failed" → Remove spaces from app password
- "Module not found" → Run `pip install -r .claude/skills/blog-writer/scripts/requirements.txt`

---

## Quality Checklist

Before delivery, verify:

**Content:**
- [ ] 1,500+ words
- [ ] SEO title < 60 chars
- [ ] Meta description 150-155 chars
- [ ] 5+ H2 headings
- [ ] Category assigned
- [ ] 3-8 tags

**Visuals:**
- [ ] 4-6 styled HTML/CSS components
- [ ] 5 image prompts with blog branding
- [ ] Images generated successfully

**Publishing:**
- [ ] WordPress draft created
- [ ] Edit URL provided
