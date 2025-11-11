#!/usr/bin/env python3
import sys, os, requests
import pandas as pd
import frontmatter
from pathlib import Path
import datetime
from markdownify import markdownify as md

def slugify(s):
    return str(s).strip().lower().replace(' ', '-').replace('/', '-')

def ensure_dir(p):
    Path(p).mkdir(parents=True, exist_ok=True)

def fetch_doc_markdown(doc_link):
    """
    Fetch a Google Doc as HTML and convert to Markdown.
    Doc must be shared 'Anyone with the link: Viewer'.
    """
    if not doc_link or "docs.google.com/document/d/" not in doc_link:
        return ""
    try:
        doc_id = doc_link.split("/d/")[1].split("/")[0]
        export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=html"
        resp = requests.get(export_url, timeout=60)
        if resp.status_code == 200 and resp.text:
            html = resp.text
            # Convert HTML -> Markdown (keeps bold/italics/headings/lists/links, and image <img> to ![]())
            return md(html, strip=['span'])\
                .replace('\r\n', '\n')\
                .strip()
        else:
            print(f"⚠️ Could not fetch HTML for Doc ({resp.status_code})")
            return ""
    except Exception as e:
        print(f"⚠️ Error fetching doc HTML: {e}")
        return ""

def row_to_post(row):
    slug = row.get('slug') or slugify(row.get('title') or '')
    title = row.get('title') or ''
    raw_date = row.get('date') or datetime.date.today().isoformat()
    try:
        date = pd.to_datetime(raw_date).date().isoformat()
    except Exception:
        date = datetime.date.today().isoformat()

    tags = row.get('tags') or ''
    published = str(row.get('published') or '').strip().lower() in ('true', '1', 'yes', 'y')
    thumbnail = row.get('thumbnail') or ''
    doc_link = row.get('doc_link') or ''
    content = row.get('content') or ''

    # Prefer Google Doc content if provided
    if doc_link:
        md_text = fetch_doc_markdown(doc_link)
        if md_text:
            content = md_text

    meta = {
        'title': title,
        'date': date,
        'tags': [t.strip() for t in str(tags).split(',') if t.strip()],
        'published': published,
        'thumbnail': thumbnail
    }
    return slug, meta, content

def main(csv_path, out_dir):
    df = pd.read_csv(csv_path)
    ensure_dir(out_dir)
    wrote = 0
    skipped = 0

    for idx, r in df.fillna('').iterrows():
        slug, meta, content = row_to_post(r)
        if not slug or not meta['title']:
            print(f"⚠️ Skipping row {idx} (missing slug/title)")
            skipped += 1
            continue
        if not meta['published']:
            print(f"⏭️ Skipping {slug} (published is FALSE)")
            skipped += 1
            continue

        date_part = meta['date'][:10] if meta.get('date') else ''
        fname = f"{date_part}-{slug}.md" if date_part else f"{slug}.md"
        p = Path(out_dir) / fname

        post = frontmatter.Post(content, **meta)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        print(f"✅ Wrote {p}")
        wrote += 1

    print(f"\nSummary: wrote {wrote} post(s), skipped {skipped} row(s).")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: csv_to_md.py sheet.csv output_dir")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
