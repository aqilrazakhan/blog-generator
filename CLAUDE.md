# WordPress Blog Publishing System - Project Guide

## Project Overview

**Platform:** WordPress
**Blog Niche:** [Your Blog Topic] (configured during setup)
**Target Audience:** [Your Target Readers] (configured during setup)
**Automation:** Complete article → WordPress publishing pipeline

> **Note:** This is a generic template. During first use, you'll be prompted to configure your blog name, niche, WordPress URL, and credentials.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Complete Workflow (Article → WordPress)](#complete-workflow)
3. [Content Standards](#content-standards)
4. [Visual Content Creation](#visual-content-creation)
5. [WordPress Publishing](#wordpress-publishing)
6. [Required Credentials](#required-credentials)

---

## Project Structure

```
[PROJECT_ROOT]/
├── CLAUDE.md                           ← This file (Claude's memory)
├── .env                                ← Your credentials (DO NOT COMMIT)
├── .env.example                        ← Credentials template
├── .gitignore                          ← Protects credentials
├── blog-posts/                         ← All articles
│   └── [number]-[article-slug]/       ← Individual articles
│       ├── article.md                  ← Main content
│       ├── article-with-images.md      ← Copy for WordPress
│       ├── IMAGE-SPECIFICATIONS.md     ← Image creation guide
│       ├── README.md                   ← Publishing checklist
│       ├── images/                     ← Generated/created images
│       └── code-examples/              ← Optional code files (for technical blogs)
└── .claude/skills/
    ├── blog-writer/                    ← Article creation skill
    │   ├── SKILL.md                    ← Skill instructions
    │   ├── scripts/                    ← Python scripts
    │   │   ├── generate_article_images.py  ← DALL-E image generator
    │   │   ├── upload_article_to_wordpress.py ← WordPress publisher
    │   │   └── requirements.txt        ← Python dependencies
    │   └── references/                 ← Documentation
    └── skill-creator/                  ← Skill creation helper
```

---

## Complete Workflow

### Step 1: Create Article

**User Action:** Request a blog topic or let skill suggest based on your niche

**Claude Action:**

```bash
# 1. Skill gathers configuration (first time):
- WordPress site URL
- Blog name and niche
- Credentials (stored in .env)

# 2. Claude automatically:
- Researches topic based on your blog niche
- Creates folder: blog-posts/[number]-[slug]/
- Writes article.md (1,500-3,000 words)
- Embeds 4-6 CSS/HTML diagrams
- Adds SEO metadata (title, description, category, tags)
- Creates IMAGE-SPECIFICATIONS.md
- Creates README.md
```

**Output:**
- ✅ `article.md` - Complete article with embedded CSS/HTML diagrams
- ✅ `IMAGE-SPECIFICATIONS.md` - Detailed image specs
- ✅ `README.md` - Publishing checklist
- ✅ Image placeholders embedded in article

---

### Step 2: Add Image Prompts to Generator

**Claude Action:**

```python
# Claude adds DALL-E prompts to .claude/skills/blog-writer/scripts/generate_article_images.py
# Prompts include YOUR blog branding watermark
ARTICLE_PROMPTS = {
    "[number]-[article-slug]": {
        "featured": {
            "filename": "featured-image.png",
            "prompt": "Detailed DALL-E prompt... Bottom right corner contains the text '[YOUR_BLOG_NAME]' in white modern sans-serif font.",
            "section": "Header"
        },
        # ... 4-5 more images with your branding
    }
}
```

**Output:**
- ✅ Image generation prompts added to script
- ✅ All prompts include your blog name watermark

---

### Step 3: Generate Images via DALL-E

**Prerequisite:** OPENAI_API_KEY must be in .env file

```bash
# From project root, generate all images automatically
python3 .claude/skills/blog-writer/scripts/generate_article_images.py [article-folder-name]
```

**Example:**
```bash
python3 .claude/skills/blog-writer/scripts/generate_article_images.py 01-introduction-to-topic
```

**Output:**
- ✅ 5 images generated via DALL-E 3
- ✅ Saved to `images/` folder
- ✅ Cost: ~$0.40 (standard quality)
- ✅ `generation_results.json` with status

**Alternative:** If OPENAI_API_KEY not set, create images manually using `IMAGE-SPECIFICATIONS.md`

---

### Step 4: Prepare for WordPress

**Claude Action:**

```bash
# Copy article to WordPress-ready filename
cp article.md article-with-images.md
```

**Output:**
- ✅ `article-with-images.md` - Ready for upload

---

### Step 5: Publish to WordPress

**Prerequisite:** WordPress credentials must be in .env file

```bash
# .env file contains:
# WORDPRESS_SITE="https://yourblog.com"
# WORDPRESS_USERNAME="your_username"
# WORDPRESS_APP_PASSWORD="your_app_password"

# Publish article
python3 .claude/skills/blog-writer/scripts/upload_article_to_wordpress.py [article-folder-name]
```

**Example:**
```bash
python3 .claude/skills/blog-writer/scripts/upload_article_to_wordpress.py 01-introduction-to-topic
```

**What happens:**
1. ✅ Uploads all 5 images to WordPress Media Library
2. ✅ Replaces local image paths with WordPress URLs
3. ✅ Converts markdown to HTML
4. ✅ Creates/finds category and tags
5. ✅ Creates WordPress post as DRAFT
6. ✅ Returns edit URL for review

**Output:**
```
✅ POST CREATED SUCCESSFULLY!
   Post ID: 123
   Status: draft
   Edit URL: https://yourblog.com/wp-admin/post.php?post=123&action=edit
```

---

## Content Standards

### Article Requirements

| Element | Requirement |
|---------|------------|
| **Length** | 1,500 - 3,000 words minimum |
| **Format** | Markdown with H1 → H2 → H3 hierarchy |
| **Code Examples** | Language appropriate to your niche (Python, JavaScript, etc.) |
| **CSS/HTML Diagrams** | 4-6 per article |
| **Static Images** | 5 images (1 featured + 4 section) with your blog branding |
| **SEO Title** | Under 60 characters |
| **Meta Description** | 150-155 characters |
| **Category** | One primary (based on your niche) |
| **Tags** | 3-8 relevant tags |

### Writing Style

- **Tone:** Professional but accessible (customizable per niche)
- **Tense:** Present tense for tutorials, past tense for case studies
- **Voice:** Second person ("you") for tutorials, third person for explanatory content
- **Examples:** Real-world, production-ready (no toy examples)
- **Current Information:** Always reference latest versions (2025/2026)

### Content Distribution (Customizable)

Adapt based on your blog niche:

**For Technical Blogs:**
- 40% Tutorials
- 25% Tool Comparisons
- 20% Best Practices
- 10% Case Studies
- 5% News & Updates

**For Business Blogs:**
- 40% How-to Guides
- 25% Industry Analysis
- 20% Case Studies
- 10% Expert Interviews
- 5% News & Trends

**For Lifestyle Blogs:**
- 40% How-to Guides
- 25% Personal Stories
- 20% Product Reviews
- 10% Tips & Tricks
- 5% Trends

> **Note:** Skill adapts content to YOUR blog niche automatically

---

## Visual Content Creation

### CSS/HTML Diagrams (Automatic)

**Claude creates 4-6 diagrams per article using inline CSS/HTML:**

These diagrams are created with pure HTML and inline CSS styles, ensuring:
- Full WordPress compatibility (no plugin dependencies)
- Consistent rendering across all browsers
- No external JavaScript required
- Mobile-responsive design

**Example Diagram Structure:**
```html
<div style="display: flex; align-items: center; justify-content: center; gap: 20px; padding: 20px; background: #f8f9fa; border-radius: 8px;">
  <div style="padding: 15px 25px; background: #4A90E2; color: white; border-radius: 6px; font-weight: bold;">Step 1</div>
  <div style="font-size: 24px; color: #666;">→</div>
  <div style="padding: 15px 25px; background: #27AE60; color: white; border-radius: 6px; font-weight: bold;">Step 2</div>
  <div style="font-size: 24px; color: #666;">→</div>
  <div style="padding: 15px 25px; background: #9B59B6; color: white; border-radius: 6px; font-weight: bold;">Result</div>
</div>
```

**Standard Colors:**
- Blue `#4A90E2` - Primary/Important
- Green `#27AE60` - Success/Positive
- Orange `#F39C12` - Warning/Medium
- Red `#E74C3C` - Error/Critical
- Purple `#9B59B6` - Special features
- Gold `#F5A623` - Input/Output
- Light Gray `#f8f9fa` - Background containers

### Static Images (Generated via DALL-E)

**Required Images:**

| Image | Dimensions | Purpose |
|-------|-----------|---------|
| `featured-image.png` | 1200x630px | Social media thumbnail (REQUIRED) |
| `section-image-1.png` | 1792x1024px | First main section illustration |
| `section-image-2.png` | 1792x1024px | Second main section illustration |
| `section-image-3.png` | 1792x1024px | Third main section illustration |
| `section-image-4.png` | 1792x1024px | Fourth main section illustration |

**Image Branding:**
All images automatically include YOUR blog name as watermark:
- Position: Bottom right corner
- Text: "[YOUR_BLOG_NAME]" (from configuration)
- Style: White modern sans-serif font
- Always included in DALL-E prompts

**Generation Methods:**

1. **Automatic (DALL-E 3) - Recommended:**
   ```bash
   # Credentials from .env file
   python3 .claude/skills/blog-writer/scripts/generate_article_images.py [folder-name]
   ```

2. **Manual (if OPENAI_API_KEY not available):**
   - Use IMAGE-SPECIFICATIONS.md guide
   - Tools: Canva, DALL-E web, Figma
   - Save with exact filenames to `images/` folder
   - Add your blog watermark manually

---

## WordPress Publishing

### Prerequisites

#### 1. WordPress Application Password

**How to get it:**
1. WordPress Dashboard → Users → Profile
2. Scroll to "Application Passwords"
3. Enter name: "Blog Publishing API"
4. Click "Add New Application Password"
5. Copy the generated password (format: `xxxx xxxx xxxx xxxx xxxx xxxx`)
6. **Remove spaces:** `xxxxxxxxxxxxxxxxxxxxxx`

**Where to set it:**
```bash
# In .env file (at project root):
WORDPRESS_SITE="https://yourblog.com"
WORDPRESS_USERNAME="your_username"
WORDPRESS_APP_PASSWORD="xxxxxxxxxxxxxxxxxxxxxx"
BLOG_NAME="Your Blog Name"
BLOG_NICHE="Your Blog Topic"
```

**Security:**
```bash
# Add to .gitignore to protect credentials
echo ".env" >> .gitignore
```

#### 2. OpenAI API Key (for image generation)

**How to get it:**
1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Click "Create new secret key"
3. Name it: "Blog Image Generation"
4. Copy the key (starts with `sk-`)

**Where to set it:**
```bash
# Add to .env file:
OPENAI_API_KEY="sk-proj-your-key-here"
```

### Publishing Process

**Command:**
```bash
python3 .claude/skills/blog-writer/scripts/upload_article_to_wordpress.py [article-folder]
```

**What it does:**
1. ✅ Reads credentials from .env file
2. ✅ Uploads images to WordPress Media Library
3. ✅ Replaces image paths with WordPress URLs
4. ✅ Converts markdown to HTML
5. ✅ Creates/assigns category and tags
6. ✅ Sets featured image
7. ✅ Creates post as DRAFT

**After publishing:**
1. Click the edit URL provided
2. Review content and images
3. Check Yoast SEO (should be green)
4. Click "Publish" when ready

---

## Required Credentials

### Summary Table

| Credential | Purpose | Where to Get | Where to Set |
|-----------|---------|-------------|-------------|
| **OPENAI_API_KEY** | Generate images via DALL-E | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) | `.env` file in project root |
| **WORDPRESS_SITE** | Your WordPress URL | Your blog URL (e.g., https://yourblog.com) | `.env` file in project root |
| **WORDPRESS_USERNAME** | WordPress authentication | Your WordPress login username | `.env` file in project root |
| **WORDPRESS_APP_PASSWORD** | WordPress REST API access | WordPress → Profile → Application Passwords | `.env` file in project root |
| **BLOG_NAME** | Image watermark branding | Your blog name (e.g., "Tech Insights") | `.env` file in project root |
| **BLOG_NICHE** | Content topic focus | Your blog topic (e.g., "Web Development") | `.env` file in project root |

### Example .env File

```bash
# .env file (DO NOT COMMIT TO GIT)
OPENAI_API_KEY="sk-proj-your-actual-key-here"
WORDPRESS_SITE="https://yourblog.com"
WORDPRESS_USERNAME="your_wordpress_username"
WORDPRESS_APP_PASSWORD="your_app_password_no_spaces"
BLOG_NAME="Your Blog Name"
BLOG_NICHE="Your Blog Topic"
```

### Security Best Practices

```bash
# Create .gitignore to protect credentials
cat > .gitignore << 'EOF'
.env
*.pyc
__pycache__/
*.log
.DS_Store
EOF
```

### Cost Estimates

**DALL-E 3 Image Generation:**
- Standard quality (1792x1024): $0.08 per image
- 5 images per article: **$0.40 per article**
- HD quality (optional): $0.16 per image = $0.80 per article

---

## Quality Checklist

Before delivering article, verify:

**Content:**
- [ ] 1,500-3,000 words
- [ ] SEO title < 60 characters
- [ ] Meta description 150-155 characters
- [ ] 5+ H2/H3 headings
- [ ] Category assigned (based on your niche)
- [ ] 3-8 tags
- [ ] No placeholder text
- [ ] Content matches your blog niche
- [ ] Tone appropriate for your audience

**Visuals:**
- [ ] 4-6 CSS/HTML diagrams embedded
- [ ] 5 image prompts added to `.claude/skills/blog-writer/scripts/generate_article_images.py`
- [ ] All image prompts include YOUR blog name watermark
- [ ] IMAGE-SPECIFICATIONS.md created
- [ ] Image placeholders embedded with markdown syntax
- [ ] README.md created

**Publishing:**
- [ ] Images generated (DALL-E or manual)
- [ ] `article-with-images.md` created
- [ ] .env file configured with credentials
- [ ] Published to WordPress as draft
- [ ] Edit URL provided to user

---

## Quick Reference Commands

```bash
# 1. INITIAL SETUP (one-time)
# Copy and edit .env.example to create .env
cp .env.example .env
# Edit .env with your credentials

# Protect credentials (already in .gitignore)
echo ".env" >> .gitignore

# Install dependencies
pip install -r .claude/skills/blog-writer/scripts/requirements.txt

# 2. CREATE ARTICLE
# Use the blog-writer skill
/blog-writer

# 3. GENERATE IMAGES
python3 .claude/skills/blog-writer/scripts/generate_article_images.py [folder-name]

# 4. PUBLISH TO WORDPRESS
python3 .claude/skills/blog-writer/scripts/upload_article_to_wordpress.py [folder-name]

# 5. VIEW RESULTS
# Click the edit URL provided in terminal output
```

---

## Customization Guide

### For Different Blog Niches

**Technical/Programming Blogs:**
- Focus on code examples, tutorials, comparisons
- Use diagrams for architecture, workflows, data flow
- Include GitHub links, documentation references
- Target audience: developers, engineers

**Business/Marketing Blogs:**
- Focus on strategies, case studies, ROI analysis
- Use diagrams for funnels, processes, frameworks
- Include statistics, industry data, expert quotes
- Target audience: marketers, business owners

**Lifestyle/Personal Blogs:**
- Focus on personal stories, tips, reviews
- Use diagrams for timelines, comparisons, checklists
- Include personal photos, product images, infographics
- Target audience: general readers, enthusiasts

**Educational/Tutorial Blogs:**
- Focus on step-by-step guides, explanations
- Use diagrams for concepts, processes, hierarchies
- Include quizzes, exercises, further reading
- Target audience: students, learners

> **Note:** The blog-writer skill automatically adapts to YOUR configured niche

---

## Troubleshooting

### Common Issues

**"OPENAI_API_KEY not set"**
- Check `.env` file exists in project root
- Verify key format in .env: `OPENAI_API_KEY="sk-proj-..."`
- Don't use quotes inside the value

**"WordPress authentication failed"**
- Verify WordPress URL starts with https://
- Check username is correct (case-sensitive)
- Ensure app password has NO SPACES
- Test credentials manually in WordPress

**"Module not found"**
- Install dependencies: `pip install -r .claude/skills/blog-writer/scripts/requirements.txt`

**Images not uploading**
- Check image file sizes (usually max 10MB per image)
- Verify WordPress allows PNG uploads
- Check WordPress storage quota

**Wrong blog niche in articles**
- Update `BLOG_NICHE` in .env file
- Restart Claude Code session
- Skill will adapt to new niche

---

## Version History

- **2025-01-07 (Generic Version):** Made fully configurable
  - Removed all hardcoded blog-specific content
  - Added configuration system for any blog
  - Made niche-agnostic with automatic adaptation
  - Added .env credential management
  - Added security best practices
  - Support for any WordPress site

- **Previous versions:** Project-specific (not for distribution)

---

## Important Notes

### For Users Setting Up This System:

1. **First Use:** The blog-writer skill will prompt you for all configuration
2. **Credentials:** Store in `.env` file, never commit to git
3. **Customization:** System adapts to YOUR blog niche automatically
4. **Cost:** ~$0.40 per article for DALL-E images
5. **Time:** ~15-30 minutes from topic to published draft

### For Claude Code:

This file serves as your memory for the blog project. When creating articles:
- Always use configuration from `.env` file
- Adapt content to the user's configured `BLOG_NICHE`
- Include `BLOG_NAME` watermark in all image prompts
- Use `WORDPRESS_SITE` for all WordPress URLs
- Never hardcode credentials or project-specific details

---

**Note:** This is a generic template. After first use, update with your specific configuration details if desired.
