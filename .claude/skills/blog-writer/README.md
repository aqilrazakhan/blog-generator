# Blog Writer & Publisher Skill

A Claude Code skill that provides a complete automated blog publishing pipeline.

## Features

- **Article Creation** - SEO-optimized content (1,500-3,000 words)
- **Visual Content** - 4-6 styled HTML/CSS components + 5 DALL-E images with branding
- **Image Generation** - Automatic via DALL-E API ($0.40 per article)
- **WordPress Publishing** - Automatic upload as draft
- **Any Niche** - Configurable for any blog topic

---

## Repository Structure

### What's Included (Shareable)

```
blog-generator/
├── .gitignore                          # Protects credentials & articles
├── .env.example                        # Credential template
├── CLAUDE.md                           # Project instructions for Claude
│
├── .claude/
│   └── skills/
│       └── blog-writer/
│           ├── SKILL.md                # Core skill workflow
│           ├── README.md               # This file
│           ├── .env.example            # Credential template
│           ├── scripts/
│           │   ├── generate_article_images.py
│           │   ├── upload_article_to_wordpress.py
│           │   └── requirements.txt
│           └── references/
│               ├── article-template.md
│               ├── image-guide.md
│               └── troubleshooting.md
│
└── blog-posts/
    ├── generate_article_images.py      # DALL-E generator
    ├── upload_article_to_wordpress.py  # WordPress uploader
    ├── requirements.txt                # Python dependencies
    └── .gitkeep                        # Keeps empty folder in git
```

### What's Excluded (Your Assets)

These are **NOT committed** to git - they are your private content:

```
# Protected by .gitignore
.env                                    # Your credentials
.claude/settings.local.json             # Your local permissions
blog-posts/*/                           # All generated articles
├── 01-your-first-article/
├── 02-another-article/
└── ...
```

### Recommended .gitignore

```gitignore
# Credentials (NEVER commit)
.env

# Generated articles (your content assets)
blog-posts/*/

# Local settings
.claude/settings.local.json

# Python cache
__pycache__/
*.pyc

# OS files
.DS_Store
```

---

## Installation

### Option 1: Clone Repository

```bash
git clone https://github.com/yourusername/blog-generator.git
cd blog-generator
```

### Option 2: Copy Skill to Existing Project

```bash
# Copy skill folder to your project
mkdir -p your-project/.claude/skills
cp -r blog-writer your-project/.claude/skills/

# Copy required scripts to blog-posts folder
mkdir -p your-project/blog-posts
cp scripts/generate_article_images.py your-project/blog-posts/
cp scripts/upload_article_to_wordpress.py your-project/blog-posts/
cp scripts/requirements.txt your-project/blog-posts/
```

---

## Setup

### 1. Configure Environment Variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env` with your values:

```bash
OPENAI_API_KEY=sk-proj-your-actual-key
WORDPRESS_SITE=https://yourblog.com
WORDPRESS_USERNAME=your_username
WORDPRESS_APP_PASSWORD=your_app_password_no_spaces
BLOG_NAME=Your Blog Name
BLOG_NICHE=Your Blog Topic
```

### 2. Get WordPress Application Password

1. WordPress Dashboard → Users → Your Profile
2. Scroll to "Application Passwords"
3. Enter name: "Blog Publishing API"
4. Click "Add New Application Password"
5. Copy password and **remove all spaces**

### 3. Get OpenAI API Key

1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Create new secret key
3. Copy the key (starts with `sk-`)

### 4. Install Python Dependencies

```bash
cd blog-posts
pip install -r requirements.txt
```

---

## Usage

```bash
# Start Claude Code in your project
cd blog-generator

# Invoke the skill
/blog-writer
```

The skill will:
1. Ask for your article topic (or suggest topics)
2. Research and write the article
3. Create styled HTML/CSS components (WordPress-compatible)
4. Generate DALL-E images with your branding (~$0.40)
5. Upload to WordPress as draft
6. Provide edit URL for review

---

## Generated Article Structure

After running the skill, each article is created in `blog-posts/`:

```
blog-posts/
└── 01-your-article-slug/
    ├── article.md                      # Main article content
    ├── article-with-images.md          # WordPress-ready version
    ├── IMAGE-SPECIFICATIONS.md         # Image creation specs
    ├── README.md                       # Publishing checklist
    └── images/
        ├── featured-image.png          # Social media thumbnail
        ├── section-1.png               # Section illustrations
        ├── section-2.png
        ├── section-3.png
        ├── section-4.png
        └── generation_results.json     # Image generation log
```

**Note:** Generated articles are excluded from git commits - they are your content assets.

---

## Cost

| Item | Cost |
|------|------|
| Article creation | $0.00 |
| DALL-E images (5) | $0.40 |
| WordPress publishing | $0.00 |
| **Total per article** | **$0.40** |

---

## Troubleshooting

### "OPENAI_API_KEY not set"
- Ensure `.env` file exists in project root
- Check key format: `OPENAI_API_KEY=sk-proj-...`

### "WordPress authentication failed"
- Verify site URL starts with `https://`
- Ensure app password has NO SPACES
- Check username is correct

### "Module not found"
```bash
pip install -r blog-posts/requirements.txt
```

For more solutions, see [references/troubleshooting.md](references/troubleshooting.md).

---

## Configuration Examples

### AI/Tech Blog
```bash
BLOG_NAME=CodeAgents
BLOG_NICHE=AI Coding Assistants & Code Generation Agents
```

### Web Development Blog
```bash
BLOG_NAME=Code Masters
BLOG_NICHE=Web Development & Programming
```

### Digital Marketing Blog
```bash
BLOG_NAME=Marketing Pro
BLOG_NICHE=Digital Marketing & SEO
```

---

## Security

- **Never commit `.env`** - contains your credentials
- Use WordPress Application Passwords (not main password)
- Generated articles are excluded from git by default
- Add `.env` to `.gitignore` immediately after setup

---

## License

MIT License - Use freely for personal or commercial projects.

---

## Contributing

1. Fork the repository
2. Make improvements
3. Test the skill with `/blog-writer`
4. Submit pull request

**Note:** Do not include generated articles in pull requests.
