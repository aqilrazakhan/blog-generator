#!/usr/bin/env python3
"""
Universal Blog Article Image Generator
Generates images for any article using DALL-E 3

Usage: python3 generate_article_images.py <article-folder>
Example: python3 generate_article_images.py 01-my-first-article

Note: The blog-writer skill automatically adds image prompts to ARTICLE_PROMPTS
"""

import sys
import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from openai import OpenAI
import requests

# ============================================================
# IMAGE PROMPTS FOR EACH ARTICLE
# ============================================================
# The blog-writer skill will automatically add entries here.
# Each article gets 5 images with your blog branding.
#
# Format:
# "article-folder-name": {
#     "featured": {
#         "filename": "featured-image.png",
#         "prompt": "Your DALL-E prompt with {BLOG_NAME} watermark...",
#         "section": "Header"
#     },
#     "section1": { ... },
#     "section2": { ... },
#     ... more images
# }
# ============================================================

ARTICLE_PROMPTS = {
    # Prompts will be added here automatically by the blog-writer skill
    # when you create new articles
}


def get_blog_name():
    """Get blog name from environment for reference"""
    return os.getenv("BLOG_NAME", "My Blog")


def generate_image(prompt_data, output_dir, model="dall-e-3", size="1792x1024", quality="standard"):
    """Generate a single image using DALL-E API"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found in .env file!")
        return {"status": "error", "error": "API key not set"}

    client = OpenAI(api_key=api_key)

    filename = prompt_data["filename"]
    prompt = prompt_data["prompt"]
    section = prompt_data.get("section", "Unknown")

    print(f"\n{'='*60}")
    print(f"Generating: {filename}")
    print(f"Section: {section}")
    print(f"{'='*60}")

    try:
        response = client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality=quality,
            n=1
        )

        image_url = response.data[0].url
        image_path = output_dir / filename

        # Download and save image
        image_data = requests.get(image_url, timeout=60).content
        with open(image_path, 'wb') as f:
            f.write(image_data)

        print(f"✅ Success! Saved to: {image_path}")
        return {"status": "success", "path": str(image_path)}

    except Exception as e:
        print(f"❌ Error generating {filename}: {str(e)}")
        return {"status": "error", "error": str(e)}


def main():
    """Main execution function"""
    if len(sys.argv) < 2:
        print("❌ Error: Please provide article folder name")
        print("\nUsage: python3 generate_article_images.py <article-folder>")
        print("Example: python3 generate_article_images.py 01-my-first-article")

        if ARTICLE_PROMPTS:
            print("\nAvailable articles with prompts:")
            for article in ARTICLE_PROMPTS.keys():
                print(f"  - {article}")
        else:
            print("\n📝 No articles configured yet.")
            print("   Use the /blog-writer skill to create an article first.")
            print("   The skill will automatically add image prompts here.")
        sys.exit(1)

    article_folder = sys.argv[1]

    # Check multiple possible locations
    possible_paths = [
        Path(__file__).parent / article_folder,
        Path(__file__).parent.parent / article_folder,
        Path.cwd() / article_folder,
        Path.cwd() / "blog-posts" / article_folder,
    ]

    article_path = None
    for path in possible_paths:
        if path.exists():
            article_path = path
            break

    if not article_path:
        print(f"❌ Error: Article folder not found: {article_folder}")
        print(f"   Searched in: {[str(p) for p in possible_paths]}")
        sys.exit(1)

    # Check if prompts exist for this article
    if article_folder not in ARTICLE_PROMPTS:
        print(f"❌ Error: No image prompts defined for: {article_folder}")

        if ARTICLE_PROMPTS:
            print("\nAvailable articles with prompts:")
            for article in ARTICLE_PROMPTS.keys():
                print(f"  - {article}")
        else:
            print("\n📝 No articles configured yet.")
            print("   The blog-writer skill adds prompts automatically when creating articles.")
        sys.exit(1)

    prompts = ARTICLE_PROMPTS[article_folder]

    # Create images directory
    images_dir = article_path / "images"
    images_dir.mkdir(exist_ok=True)

    print("\n" + "="*60)
    print(f"GENERATING IMAGES FOR: {article_folder}")
    print("="*60)
    print(f"Blog: {get_blog_name()}")
    print(f"Output directory: {images_dir}")
    print(f"Total images to generate: {len(prompts)}")
    print("="*60)

    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("\n❌ ERROR: OPENAI_API_KEY not set!")
        print("Please add it to your .env file:")
        print('OPENAI_API_KEY="sk-proj-your-key-here"')
        sys.exit(1)

    # Generate images
    results = []
    for key, prompt_data in prompts.items():
        result = generate_image(prompt_data, images_dir)
        result["key"] = key
        result["filename"] = prompt_data.get("filename", "unknown.png")
        results.append(result)

    # Save results
    results_file = images_dir / "generation_results.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    # Summary
    successful = sum(1 for r in results if r.get("status") == "success")
    total = len(results)
    cost = successful * 0.08  # $0.08 per standard image

    print("\n" + "="*60)
    print("GENERATION COMPLETE")
    print("="*60)
    print(f"✅ Successful: {successful}/{total}")
    print(f"💰 Estimated cost: ${cost:.2f}")
    print(f"📁 Results saved to: {results_file}")

    if successful < total:
        failed = [r for r in results if r.get("status") != "success"]
        print(f"\n⚠️  {len(failed)} images failed:")
        for f in failed:
            print(f"   - {f.get('filename', 'unknown')}: {f.get('error', 'unknown error')}")
        sys.exit(1)

    print("\n✅ All images generated successfully!")
    print(f"📂 Images saved to: {images_dir}")


if __name__ == "__main__":
    main()
