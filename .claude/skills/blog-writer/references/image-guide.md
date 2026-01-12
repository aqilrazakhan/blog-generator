# Image Generation Guide

## Required Images

| Image | Dimensions | Purpose |
|-------|-----------|---------|
| `featured-image.png` | 1792x1024 | Social media thumbnail |
| `section-1.png` | 1792x1024 | First section illustration |
| `section-2.png` | 1792x1024 | Second section illustration |
| `section-3.png` | 1792x1024 | Third section illustration |
| `section-4.png` | 1792x1024 | Fourth section illustration |

---

## DALL-E Prompt Template

```
"[Subject/main element] showing [specific details].
Include [specific icons/symbols].
Use [color palette with hex codes].
[Style description: modern, minimalist, professional].
Bottom right corner contains the text '{BLOG_NAME}' in white modern sans-serif font.
No other text or labels.
Horizontal layout 1792x1024."
```

**CRITICAL:** Always include blog branding watermark:
```
Bottom right corner contains the text '{BLOG_NAME}' in white modern sans-serif font.
```

---

## Adding Prompts to Script

Edit `scripts/generate_article_images.py` and add entry to `ARTICLE_PROMPTS`:

```python
ARTICLE_PROMPTS = {
    "01-article-slug": {
        "featured": {
            "filename": "featured-image.png",
            "prompt": "A modern tech dashboard showing AI metrics and analytics. Include neural network nodes, data visualizations, and glowing blue connections. Use blue (#4A90E2), white, and dark gray color scheme. Clean, minimalist, professional design. Bottom right corner contains the text 'Your Blog Name' in white modern sans-serif font. No other text. Horizontal layout 1792x1024.",
            "section": "Header"
        },
        "architecture": {
            "filename": "section-1.png",
            "prompt": "Technical architecture diagram...",
            "section": "Architecture"
        },
        # ... add more images
    }
}
```

---

## Running Image Generation

```bash
cd blog-posts
python3 generate_article_images.py <article-folder>
```

Example:
```bash
python3 generate_article_images.py 01-building-ai-agents
```

---

## Cost

- Standard quality: $0.08 per image
- 5 images per article: **$0.40 total**
- HD quality (optional): $0.16 per image = $0.80 per article

---

## IMAGE-SPECIFICATIONS.md Template

Create this file in each article folder for manual fallback:

```markdown
# Image Specifications for [Article Title]

## 1. Featured Image (featured-image.png)
- **Dimensions:** 1200x630px (optimized for social)
- **Subject:** [Description]
- **Style:** [Style notes]
- **Colors:** [Color palette]
- **Branding:** Include "{BLOG_NAME}" watermark bottom-right

## 2. Section Image 1 (section-1.png)
[Same format...]

## 3. Section Image 2 (section-2.png)
[Same format...]

## 4. Section Image 3 (section-3.png)
[Same format...]

## 5. Section Image 4 (section-4.png)
[Same format...]
```
