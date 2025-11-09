#!/usr/bin/env python3
import sys, os
import pandas as pd
import frontmatter
from pathlib import Path
import datetime

def slugify(s):
    """Convert title to URL-safe slug"""
    return str(s).strip().lower().replace(' ', '-').replace('/', '-')

def ensure_dir(p):
    """Make sure output folder exists"""
    Path(p).mkdir(parents=True, exist_ok=True)

def row_to_post(row):
    slug = row.get('slug') or slugify(row.get('title') or '')
    title = row.get('title') or ''
    raw_date = row.get('date') or datetime.date.today()
    try:
        date = pd.to_datetime(raw_date).date().isoformat()
    except Exception:
        date = str(datetime.date.today())

    tags = row.get('tags') or ''
    content = row.get('content') or ''
    published = str(row.get('published') or '').strip().lower() in ('true','1','yes','y')

    meta = {
        'title': title,
        'date': date,
        'tags': [t.strip() for t in str(tags).split(',') if t.strip()],
        'published': published
    }
    return slug, meta, content

def main(csv_path, out_dir):
    """Convert Google Sheet CSV to Markdown posts"""
    print(f"📥 Reading CSV from: {csv_path}")
    df = pd.read_csv(csv_path)
    ensure_dir(out_dir)

    for idx, r in df.fillna('').iterrows():
        slug, meta, content = row_to_post(r)
        if not slug:
            print(f"⚠️ Skipping row {idx} (no slug or title)")
            continue

        date_part = meta.get('date', '')[:10]
        fname = f"{date_part}-{slug}.md" if date_part else f"{slug}.md"
        p = Path(out_dir) / fname

        post = frontmatter.Post(content, **meta)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        print(f"✅ Wrote {p}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: csv_to_md.py sheet.csv output_dir")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
