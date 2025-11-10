#!/usr/bin/env python3
import sys, os, requests
import pandas as pd
import frontmatter
from pathlib import Path
import datetime

def slugify(s):
    return str(s).strip().lower().replace(' ', '-')

def ensure_dir(p):
    Path(p).mkdir(parents=True, exist_ok=True)

def fetch_doc_text(doc_link):
    """Fetch the plain text export from a Google Doc link."""
    if not doc_link or "docs.google.com/document/d/" not in doc_link:
        return ""
    try:
        doc_id = doc_link.split("/d/")[1].split("/")[0]
        export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
        resp = requests.get(export_url)
        if resp.status_code == 200:
            return resp.text.strip()
        else:
            print(f"⚠️ Could not fetch {doc_link} (status {resp.status_code})")
            return ""
    except Exception as e:
        print(f"⚠️ Error fetching doc: {e}")
        return ""

def row_to_post(row):
    slug = row.get('slug') or slugify(row.get('title') or '')
    title = row.get('title') or ''
    date = row.get('date') or datetime.date.today().isoformat()
    tags = row.get('tags') or ''
    content = row.get('content') or ''
    doc_link = row.get('doc_link') or ''
    published = str(row.get('published') or '').strip().lower() in ('true','1','yes','y')

    # If doc_link exists, override content with Google Doc text
    if doc_link:
        doc_text = fetch_doc_text(doc_link)
        if doc_text:
            content = doc_text

    meta = {
        'title': title,
        'date': str(date),
        'tags': [t.strip() for t in str(tags).split(',') if t.strip()],
        'published': published,
        'thumbnail': row.get('thumbnail') or '',
    }

    return slug, meta, content

def main(csv_path, out_dir):
    df = pd.read_csv(csv_path)
    ensure_dir(out_dir)
    for idx, r in df.fillna('').iterrows():
        slug, meta, content = row_to_post(r)
        if not slug:
            print(f"Skipping row {idx} (no slug or title)")
            continue
        if not meta.get('published'):
            print(f"Skipping {slug} (not published)")
            continue
        date_part = meta.get('date', '')[:10]
        fname = f"{date_part}-{slug}.md" if date_part else f"{slug}.md"
        p = Path(out_dir) / fname
        post = frontmatter.Post(content, **meta)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        print("✅ Wrote", p)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: csv_to_md.py sheet.csv output_dir")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
