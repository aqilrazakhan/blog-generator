# Article Template

## Markdown Structure

```markdown
# [SEO Title - Under 60 Characters]

**Category:** [Category Name]
**Tags:** tag1, tag2, tag3, tag4, tag5
**Reading Time:** [X] minutes
**SEO Title:** [Exact title for search engines]
**Meta Description:** [Exactly 150-155 characters with keyword and value prop]

---

![Featured Image](images/featured-image.png)

## Introduction

[Hook the reader with interesting fact, statistic, or question]

[Clear value proposition - what will they learn?]

[Brief overview of article structure]

## [H2 Main Topic 1]

![Section Image](images/section-1.png)

[Content...]

<!-- HTML/CSS styled component here -->

### [H3 Subtopic if needed]

[Content with code examples...]

## [H2 Main Topic 2]

[Continue pattern...]

## Conclusion

[Summarize key takeaways]

[Call to action]

[Further reading suggestions]
```

---

## Content Requirements

| Element | Requirement |
|---------|------------|
| **Length** | 1,500 - 3,000 words |
| **SEO Title** | Under 60 characters with primary keyword |
| **Meta Description** | 150-155 characters |
| **Headings** | 5+ H2 sections |
| **HTML/CSS Components** | 4-6 per article (NO Mermaid) |
| **Images** | 5 (1 featured + 4 section) |
| **Category** | One primary |
| **Tags** | 3-8 relevant |

---

## Writing Guidelines

### Tone & Style
- Present tense for tutorials
- Second person ("you") for direct engagement
- Professional but accessible
- No placeholder text

### Structure
- Short paragraphs (2-4 sentences)
- Bullet points for lists
- Bold important terms on first mention
- Code blocks with syntax highlighting

### SEO
- Primary keyword in title and first H2
- Related keywords in other headings
- Natural keyword density
- Clear value proposition in meta description

---

## HTML/CSS Component Color Scheme

**IMPORTANT:** WordPress does NOT render Mermaid diagrams. Use inline HTML/CSS instead.

```
Blue   (#4A90E2) - Primary/Important elements
Green  (#27AE60) - Success/Positive outcomes
Orange (#F39C12) - Warning/Medium priority
Red    (#E74C3C) - Error/Critical
Purple (#9B59B6) - Special features
Gold   (#F5A623) - Input/Output
Dark   (#1a1a2e) - Background
```

---

## Styled Component Examples

### 1. Timeline/Process Cards

Use for showing evolution, steps, or progression:

```html
<div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 20px 0;">
  <div style="flex: 1; min-width: 200px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white;">
    <h4 style="margin: 0 0 10px 0;">Phase 1: Discovery</h4>
    <p style="margin: 0; font-size: 14px;">Initial research and requirements gathering</p>
  </div>
  <div style="flex: 1; min-width: 200px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 10px; color: white;">
    <h4 style="margin: 0 0 10px 0;">Phase 2: Development</h4>
    <p style="margin: 0; font-size: 14px;">Building the core functionality</p>
  </div>
  <div style="flex: 1; min-width: 200px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 10px; color: white;">
    <h4 style="margin: 0 0 10px 0;">Phase 3: Launch</h4>
    <p style="margin: 0; font-size: 14px;">Deployment and user onboarding</p>
  </div>
</div>
```

### 2. Statistics/Metrics Box

Use for highlighting key numbers:

```html
<div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 20px 0;">
  <div style="flex: 1; min-width: 150px; background: #1a1a2e; padding: 20px; border-radius: 10px; text-align: center; border-left: 4px solid #4A90E2;">
    <div style="font-size: 32px; font-weight: bold; color: #4A90E2;">85%</div>
    <div style="color: #ccc; font-size: 14px;">Productivity Increase</div>
  </div>
  <div style="flex: 1; min-width: 150px; background: #1a1a2e; padding: 20px; border-radius: 10px; text-align: center; border-left: 4px solid #27AE60;">
    <div style="font-size: 32px; font-weight: bold; color: #27AE60;">10x</div>
    <div style="color: #ccc; font-size: 14px;">Faster Development</div>
  </div>
  <div style="flex: 1; min-width: 150px; background: #1a1a2e; padding: 20px; border-radius: 10px; text-align: center; border-left: 4px solid #9B59B6;">
    <div style="font-size: 32px; font-weight: bold; color: #9B59B6;">$2M+</div>
    <div style="color: #ccc; font-size: 14px;">Cost Savings</div>
  </div>
</div>
```

### 3. Comparison Cards

Use for comparing features, tools, or approaches:

```html
<div style="display: flex; flex-wrap: wrap; gap: 20px; margin: 20px 0;">
  <div style="flex: 1; min-width: 280px; background: white; border-radius: 10px; padding: 25px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <h4 style="color: #4A90E2; margin: 0 0 15px 0; border-bottom: 2px solid #4A90E2; padding-bottom: 10px;">Option A</h4>
    <ul style="margin: 0; padding-left: 20px; color: #333;">
      <li>Feature one description</li>
      <li>Feature two description</li>
      <li>Feature three description</li>
    </ul>
  </div>
  <div style="flex: 1; min-width: 280px; background: white; border-radius: 10px; padding: 25px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <h4 style="color: #27AE60; margin: 0 0 15px 0; border-bottom: 2px solid #27AE60; padding-bottom: 10px;">Option B</h4>
    <ul style="margin: 0; padding-left: 20px; color: #333;">
      <li>Different feature one</li>
      <li>Different feature two</li>
      <li>Different feature three</li>
    </ul>
  </div>
</div>
```

### 4. Tool/Feature Cards with Icons

Use for listing tools, features, or capabilities:

```html
<div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 20px 0;">
  <div style="flex: 1; min-width: 200px; background: white; border-radius: 8px; padding: 20px; border-left: 4px solid #4A90E2; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    <h4 style="margin: 0 0 8px 0; color: #333;">Tool Name</h4>
    <p style="margin: 0; color: #666; font-size: 14px;">Brief description of what this tool does</p>
  </div>
  <div style="flex: 1; min-width: 200px; background: white; border-radius: 8px; padding: 20px; border-left: 4px solid #27AE60; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    <h4 style="margin: 0 0 8px 0; color: #333;">Another Tool</h4>
    <p style="margin: 0; color: #666; font-size: 14px;">Description of this tool's purpose</p>
  </div>
</div>
```

### 5. Numbered Process List

Use for step-by-step instructions:

```html
<div style="margin: 20px 0;">
  <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
    <div style="background: #4A90E2; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 15px; flex-shrink: 0;">1</div>
    <div>
      <strong style="color: #333;">Step Title</strong>
      <p style="margin: 5px 0 0 0; color: #666;">Detailed explanation of what to do in this step.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; margin-bottom: 15px;">
    <div style="background: #27AE60; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 15px; flex-shrink: 0;">2</div>
    <div>
      <strong style="color: #333;">Next Step</strong>
      <p style="margin: 5px 0 0 0; color: #666;">Explanation of the next action.</p>
    </div>
  </div>
</div>
```

### 6. Decision/Comparison Table

Use for feature comparisons or decision matrices:

```html
<table style="width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px;">
  <thead>
    <tr style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;">Feature</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd;">Option A</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd;">Option B</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd;">Option C</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #f8f9fa;">
      <td style="padding: 12px; border: 1px solid #ddd;"><strong>Feature 1</strong></td>
      <td style="padding: 12px; text-align: center; border: 1px solid #ddd; color: #27AE60;">Yes</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #ddd; color: #27AE60;">Yes</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #ddd; color: #E74C3C;">No</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #ddd;"><strong>Feature 2</strong></td>
      <td style="padding: 12px; text-align: center; border: 1px solid #ddd; color: #27AE60;">Yes</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #ddd; color: #E74C3C;">No</td>
      <td style="padding: 12px; text-align: center; border: 1px solid #ddd; color: #27AE60;">Yes</td>
    </tr>
  </tbody>
</table>
```

### 7. Call-to-Action Box

Use for highlighting key takeaways or next steps:

```html
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 10px; margin: 30px 0; text-align: center;">
  <h3 style="color: white; margin: 0 0 15px 0;">Ready to Get Started?</h3>
  <p style="color: rgba(255,255,255,0.9); margin: 0 0 20px 0;">Take the next step in your journey.</p>
  <div style="display: inline-block; background: white; color: #667eea; padding: 12px 30px; border-radius: 25px; font-weight: bold;">
    Learn More
  </div>
</div>
```

### 8. Info/Warning Box

Use for important notes or warnings:

```html
<!-- Info Box -->
<div style="background: #e3f2fd; border-left: 4px solid #4A90E2; padding: 15px 20px; margin: 20px 0; border-radius: 0 8px 8px 0;">
  <strong style="color: #4A90E2;">Info:</strong>
  <span style="color: #333;"> Important information the reader should know.</span>
</div>

<!-- Warning Box -->
<div style="background: #fff3e0; border-left: 4px solid #F39C12; padding: 15px 20px; margin: 20px 0; border-radius: 0 8px 8px 0;">
  <strong style="color: #F39C12;">Warning:</strong>
  <span style="color: #333;"> Something to be careful about.</span>
</div>

<!-- Success Box -->
<div style="background: #e8f5e9; border-left: 4px solid #27AE60; padding: 15px 20px; margin: 20px 0; border-radius: 0 8px 8px 0;">
  <strong style="color: #27AE60;">Success:</strong>
  <span style="color: #333;"> Positive outcome or best practice.</span>
</div>
```

---

## Folder Structure Per Article

```
{NUMBER}-{ARTICLE-SLUG}/
├── article.md                # Main article
├── article-with-images.md    # WordPress version
├── IMAGE-SPECIFICATIONS.md   # Image specs
├── README.md                 # Publishing checklist
└── images/
    ├── featured-image.png
    ├── section-1.png
    ├── section-2.png
    ├── section-3.png
    └── section-4.png
```

---

## Component Selection Guide

| Content Type | Recommended Component |
|-------------|----------------------|
| Steps/Phases | Timeline Cards or Numbered Process List |
| Statistics | Statistics/Metrics Box |
| Tool comparison | Comparison Cards or Decision Table |
| Feature list | Tool/Feature Cards |
| Warning/Note | Info/Warning Box |
| Call to action | CTA Box |
| Yes/No comparison | Decision Table with colored Yes/No |
