#!/usr/bin/env python3
"""
Universal WordPress Article Uploader
Uploads article and images to WordPress via REST API
"""

import sys
import os
import re
import json
import requests
from pathlib import Path
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from .env
WORDPRESS_SITE = os.getenv("WORDPRESS_SITE", "").rstrip("/")
WP_USERNAME = os.getenv("WORDPRESS_USERNAME")
WP_APP_PASSWORD = os.getenv("WORDPRESS_APP_PASSWORD")
WP_API_BASE = f"{WORDPRESS_SITE}/wp-json/wp/v2"


def get_auth_header():
    """Create authentication header for WordPress REST API"""
    credentials = f"{WP_USERNAME}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {token}"}


def upload_image_to_wordpress(image_path):
    """Upload image to WordPress media library"""
    print(f"\n📤 Uploading: {image_path.name}")

    try:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()

        headers = get_auth_header()
        headers['Content-Disposition'] = f'attachment; filename="{image_path.name}"'
        headers['Content-Type'] = 'image/png'

        response = requests.post(
            f"{WP_API_BASE}/media",
            headers=headers,
            data=img_data,
            timeout=60
        )

        if response.status_code == 201:
            data = response.json()
            print(f"✅ Uploaded: {data['source_url']}")
            return {
                'id': data['id'],
                'url': data['source_url'],
                'filename': image_path.name
            }
        else:
            print(f"❌ Upload failed: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return None

    except Exception as e:
        print(f"❌ Error uploading {image_path.name}: {str(e)}")
        return None


def get_or_create_category(category_name):
    """Get existing category or create new one"""
    headers = get_auth_header()

    # Search for existing category
    response = requests.get(
        f"{WP_API_BASE}/categories",
        headers=headers,
        params={"search": category_name},
        timeout=30
    )

    if response.status_code == 200:
        categories = response.json()
        for cat in categories:
            if cat['name'].lower() == category_name.lower():
                print(f"📁 Found category: {cat['name']} (ID: {cat['id']})")
                return cat['id']

    # Create new category
    response = requests.post(
        f"{WP_API_BASE}/categories",
        headers=headers,
        json={"name": category_name},
        timeout=30
    )

    if response.status_code == 201:
        cat_id = response.json()['id']
        print(f"📁 Created category: {category_name} (ID: {cat_id})")
        return cat_id

    print(f"⚠️  Could not create category: {category_name}")
    return None


def get_or_create_tags(tag_names):
    """Get existing tags or create new ones"""
    headers = get_auth_header()
    tag_ids = []

    for tag_name in tag_names:
        tag_name = tag_name.strip()
        if not tag_name:
            continue

        # Search for existing tag
        response = requests.get(
            f"{WP_API_BASE}/tags",
            headers=headers,
            params={"search": tag_name},
            timeout=30
        )

        if response.status_code == 200:
            tags = response.json()
            found = False
            for tag in tags:
                if tag['name'].lower() == tag_name.lower():
                    tag_ids.append(tag['id'])
                    found = True
                    break

            if found:
                continue

        # Create new tag
        response = requests.post(
            f"{WP_API_BASE}/tags",
            headers=headers,
            json={"name": tag_name},
            timeout=30
        )

        if response.status_code == 201:
            tag_ids.append(response.json()['id'])

    print(f"🏷️  Tags: {len(tag_ids)} tags assigned")
    return tag_ids


def parse_article_metadata(content):
    """Extract metadata from article markdown"""
    metadata = {
        "title": "",
        "category": "",
        "tags": [],
        "seo_title": "",
        "meta_description": ""
    }

    lines = content.split('\n')
    for line in lines[:30]:  # Check first 30 lines
        if line.startswith('# '):
            metadata['title'] = line[2:].strip()
        elif line.startswith('**Category:**'):
            metadata['category'] = line.replace('**Category:**', '').strip()
        elif line.startswith('**Tags:**'):
            tags_str = line.replace('**Tags:**', '').strip()
            metadata['tags'] = [t.strip() for t in tags_str.split(',')]
        elif line.startswith('**SEO Title:**'):
            metadata['seo_title'] = line.replace('**SEO Title:**', '').strip()
        elif line.startswith('**Meta Description:**'):
            metadata['meta_description'] = line.replace('**Meta Description:**', '').strip()

    return metadata


def markdown_to_html(content):
    """Convert markdown to WordPress-compatible HTML"""
    html = content

    # Remove metadata block (everything before first ## or content)
    lines = html.split('\n')
    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('## ') or (line.startswith('![') and i > 10):
            start_idx = i
            break
    html = '\n'.join(lines[start_idx:])

    # Convert headers
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)

    # Convert bold and italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # Convert inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Convert images
    html = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" />', html)

    # Convert links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)

    # Convert code blocks
    html = re.sub(
        r'```(\w+)?\n(.*?)```',
        r'<pre><code class="language-\1">\2</code></pre>',
        html,
        flags=re.DOTALL
    )

    # Convert unordered lists
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*</li>\n?)+', r'<ul>\g<0></ul>', html)

    # Convert numbered lists
    html = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)

    # Convert paragraphs (lines not already tagged)
    lines = html.split('\n')
    result = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('<') and not line.startswith('```'):
            result.append(f'<p>{line}</p>')
        else:
            result.append(line)
    html = '\n'.join(result)

    return html


def create_wordpress_post(title, content, metadata, featured_image_id=None):
    """Create WordPress post as draft"""
    headers = get_auth_header()
    headers['Content-Type'] = 'application/json'

    post_data = {
        "title": metadata.get('seo_title') or title,
        "content": content,
        "status": "draft",
        "excerpt": metadata.get('meta_description', ''),
    }

    # Add category
    if metadata.get('category'):
        cat_id = get_or_create_category(metadata['category'])
        if cat_id:
            post_data['categories'] = [cat_id]

    # Add tags
    if metadata.get('tags'):
        tag_ids = get_or_create_tags(metadata['tags'])
        if tag_ids:
            post_data['tags'] = tag_ids

    # Add featured image
    if featured_image_id:
        post_data['featured_media'] = featured_image_id

    response = requests.post(
        f"{WP_API_BASE}/posts",
        headers=headers,
        json=post_data,
        timeout=60
    )

    if response.status_code == 201:
        post = response.json()
        return {
            "id": post['id'],
            "link": post['link'],
            "edit_link": f"{WORDPRESS_SITE}/wp-admin/post.php?post={post['id']}&action=edit",
            "status": post['status']
        }
    else:
        print(f"❌ Failed to create post: {response.status_code}")
        print(f"   Response: {response.text[:500]}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 upload_article_to_wordpress.py <article-folder>")
        sys.exit(1)

    # Validate configuration
    if not all([WORDPRESS_SITE, WP_USERNAME, WP_APP_PASSWORD]):
        print("❌ ERROR: WordPress credentials not configured!")
        print("\nPlease set in .env file:")
        print("  WORDPRESS_SITE=https://yourblog.com")
        print("  WORDPRESS_USERNAME=your_username")
        print("  WORDPRESS_APP_PASSWORD=your_app_password")
        sys.exit(1)

    article_folder = sys.argv[1]
    article_path = Path(__file__).parent.parent / article_folder

    if not article_path.exists():
        article_path = Path(__file__).parent / article_folder

    if not article_path.exists():
        print(f"❌ Error: Article folder not found: {article_folder}")
        sys.exit(1)

    # Find article file
    article_file = article_path / "article-with-images.md"
    if not article_file.exists():
        article_file = article_path / "article.md"

    if not article_file.exists():
        print(f"❌ Error: No article.md found in {article_folder}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"UPLOADING TO WORDPRESS: {article_folder}")
    print(f"{'='*60}")
    print(f"Site: {WORDPRESS_SITE}")
    print(f"Article: {article_file.name}")

    # Read article content
    with open(article_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse metadata
    metadata = parse_article_metadata(content)
    print(f"\n📄 Title: {metadata['title']}")
    print(f"📁 Category: {metadata['category']}")
    print(f"🏷️  Tags: {', '.join(metadata['tags'][:5])}...")

    # Upload images
    images_dir = article_path / "images"
    uploaded_images = {}
    featured_image_id = None

    if images_dir.exists():
        print(f"\n📷 Uploading images from {images_dir}")
        for img_file in sorted(images_dir.glob("*.png")):
            result = upload_image_to_wordpress(img_file)
            if result:
                uploaded_images[img_file.name] = result
                if "featured" in img_file.name.lower():
                    featured_image_id = result['id']

    # Replace local image paths with WordPress URLs
    for filename, img_data in uploaded_images.items():
        content = content.replace(f"images/{filename}", img_data['url'])
        content = content.replace(f"./images/{filename}", img_data['url'])

    # Convert markdown to HTML
    html_content = markdown_to_html(content)

    # Create post
    print(f"\n📝 Creating WordPress post...")
    result = create_wordpress_post(
        title=metadata['title'],
        content=html_content,
        metadata=metadata,
        featured_image_id=featured_image_id
    )

    if result:
        print(f"\n{'='*60}")
        print(f"✅ POST CREATED SUCCESSFULLY!")
        print(f"{'='*60}")
        print(f"   Post ID: {result['id']}")
        print(f"   Status: {result['status']}")
        print(f"   Edit URL: {result['edit_link']}")
        print(f"\n   Next steps:")
        print(f"   1. Click the Edit URL above")
        print(f"   2. Review content and images")
        print(f"   3. Check Yoast SEO (should be green)")
        print(f"   4. Click 'Publish' when ready")
    else:
        print(f"\n❌ Failed to create post")
        sys.exit(1)


if __name__ == "__main__":
    main()
