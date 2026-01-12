#!/usr/bin/env python3
"""
Universal Blog Article Image Generator
Generates images for any article using DALL-E 3
"""

import sys
import os
import json
from pathlib import Path
from openai import OpenAI
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Image prompts for each article - Claude adds entries here
ARTICLE_PROMPTS = {
    "01-rise-of-agentic-ides": {
        "featured": {
            "filename": "featured-image.png",
            "prompt": "A futuristic IDE interface showing multiple AI agents represented as glowing orbs working in parallel on floating code panels. Neural network connections flow between agents in electric blue and purple. A developer silhouette stands in the center orchestrating the process. Dark theme with colors: dark gray (#1a1a2e), electric blue (#4A90E2), purple (#9B59B6). Modern, professional tech aesthetic. Bottom right corner contains the text 'CodeAgents' in white modern sans-serif font. No other text or labels. Horizontal layout 1792x1024.",
            "section": "Header"
        },
        "evolution": {
            "filename": "section-1.png",
            "prompt": "Visual timeline showing the evolution of AI coding tools from 2021 to 2025. Left side shows a simple keyboard icon for autocomplete, middle shows chat bubbles for conversational AI, right side shows advanced robot/agent icons. Gradient background flowing from dark (#1a1a2e) to electric blue (#4A90E2). Clean infographic style with glowing elements. Arrows showing progression between eras. Bottom right corner contains the text 'CodeAgents' in white modern sans-serif font. No other text or labels. Horizontal layout 1792x1024.",
            "section": "Evolution Timeline"
        },
        "players": {
            "filename": "section-2.png",
            "prompt": "Abstract visualization of four competing AI coding tools as interconnected glowing orbs in a network. Data streams and code particles flow between them in a competitive dance. Colors: blue (#4A90E2), green (#27AE60), purple (#9B59B6), orange (#F39C12). Dark space-like background. Node network aesthetic with energy connections. Modern tech visualization style. Bottom right corner contains the text 'CodeAgents' in white modern sans-serif font. No other text or labels. Horizontal layout 1792x1024.",
            "section": "Key Players"
        },
        "capabilities": {
            "filename": "section-3.png",
            "prompt": "Isometric view of a developer workspace with multiple floating holographic panels showing code editor, terminal with running tests, file tree, and debugging output. AI neural pathways in glowing blue connect all panels showing the agent's understanding. Dark theme with blue (#4A90E2) and green (#27AE60) highlights. Modern tech workspace aesthetic. Bottom right corner contains the text 'CodeAgents' in white modern sans-serif font. No other text or labels. Horizontal layout 1792x1024.",
            "section": "Capabilities"
        },
        "future": {
            "filename": "section-4.png",
            "prompt": "Futuristic concept showing multiple AI agents as abstract geometric crystalline shapes working together around a central glowing project core. A human figure stands as the architect/orchestrator with light emanating from their hands directing the agents. Colors: purple (#9B59B6), blue (#4A90E2), gold (#F5A623), white light effects. Optimistic, inspiring tech vision aesthetic. Bottom right corner contains the text 'CodeAgents' in white modern sans-serif font. No other text or labels. Horizontal layout 1792x1024.",
            "section": "Future Vision"
        }
    }
}


def generate_image(prompt_data, output_dir, model="dall-e-3", size="1792x1024", quality="standard"):
    """Generate a single image using DALL-E API"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    filename = prompt_data["filename"]
    prompt = prompt_data["prompt"]

    print(f"\n{'='*60}")
    print(f"Generating: {filename}")
    print(f"Section: {prompt_data.get('section', 'N/A')}")
    print(f"{'='*60}")

    # Use 1200x630 for featured images (social media optimized)
    if "featured" in filename.lower():
        size = "1792x1024"  # DALL-E doesn't support 1200x630, use landscape

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
    if len(sys.argv) < 2:
        print("Usage: python3 generate_article_images.py <article-folder>")
        print("\nAvailable articles:")
        for article in ARTICLE_PROMPTS.keys():
            print(f"  - {article}")
        sys.exit(1)

    article_folder = sys.argv[1]
    article_path = Path(__file__).parent.parent / article_folder

    # Also check in blog-posts directory
    if not article_path.exists():
        article_path = Path(__file__).parent / article_folder

    if not article_path.exists():
        print(f"❌ Error: Article folder not found: {article_folder}")
        print(f"   Searched: {article_path}")
        sys.exit(1)

    if article_folder not in ARTICLE_PROMPTS:
        print(f"❌ Error: No image prompts defined for: {article_folder}")
        print("\nAvailable articles:")
        for article in ARTICLE_PROMPTS.keys():
            print(f"  - {article}")
        sys.exit(1)

    prompts = ARTICLE_PROMPTS[article_folder]
    images_dir = article_path / "images"
    images_dir.mkdir(exist_ok=True)

    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERROR: OPENAI_API_KEY not set!")
        print("Please set OPENAI_API_KEY in your .env file")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"GENERATING IMAGES FOR: {article_folder}")
    print(f"{'='*60}")
    print(f"Output directory: {images_dir}")
    print(f"Number of images: {len(prompts)}")

    # Generate all images
    results = []
    for key, prompt_data in prompts.items():
        result = generate_image(prompt_data, images_dir)
        result["key"] = key
        results.append(result)

    # Save results
    results_file = images_dir / "generation_results.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    # Summary
    successful = sum(1 for r in results if r["status"] == "success")
    total = len(results)
    cost = successful * 0.08  # $0.08 per standard image

    print(f"\n{'='*60}")
    print(f"GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"✅ Successful: {successful}/{total}")
    print(f"💰 Estimated cost: ${cost:.2f}")
    print(f"📁 Results saved to: {results_file}")

    if successful < total:
        print(f"\n⚠️  {total - successful} images failed. Check errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
