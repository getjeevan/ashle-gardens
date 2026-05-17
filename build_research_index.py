import os
import json
import re
import subprocess
from datetime import datetime

def get_git_last_modified(filepath):
    try:
        # Get the last commit date for the file
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%ai', filepath],
            capture_output=True,
            text=True,
            check=True
        )
        date_str = result.stdout.strip()
        if date_str:
            return datetime.fromisoformat(date_str).strftime('%Y-%m-%d')
    except Exception:
        pass
    # Fallback to filesystem mtime
    return datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d')

def get_domain(filepath):
    path = filepath.lower().replace('\\', '/')
    if '20-regulatory' in path:
        return 'regulatory'
    if 'financials' in path:
        return 'finance'
    if '09-land-documents' in path or 'land-criteria' in path or 'land-' in path:
        return 'land'
    if 'site-research' in path:
        return 'site'
    if '00-vision' in path or 'brand' in path:
        return 'brand'
    if '30-related-businesses' in path or 'research/' in path:
        return 'business'
    return 'business' # Default to business as it's the broadest

def process_md_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

    title = ""
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break

    if not title:
        title = os.path.basename(filepath).replace('.md', '').replace('-', ' ').replace('_', ' ').title()
        # Remove leading numbers like "01 "
        title = re.sub(r'^\d+\s*[-—]\s*', '', title)
        title = re.sub(r'^\d+\s+', '', title)

    # Summary: First 300 chars of content (excluding the title)
    # Remove the title if it's the first line
    clean_content = re.sub(r'^# .*\n?', '', content, count=1).strip()
    # Remove other markdown headers and formatting for summary
    clean_text = re.sub(r'[#*`_]', '', clean_content)
    # Replace newlines with spaces
    clean_text = re.sub(r'\s+', ' ', clean_text)
    summary = clean_text[:300].strip() + ("..." if len(clean_text) > 300 else "")

    last_modified = get_git_last_modified(filepath)
    size_bytes = os.path.getsize(filepath)
    line_count = len(lines)

    # Extract tags (word count as a proxy for size info for now)
    word_count = len(content.split())

    return {
        "filename": os.path.basename(filepath),
        "path": filepath,
        "domain": get_domain(filepath),
        "title": title,
        "summary": summary,
        "line_count": line_count,
        "word_count": word_count,
        "last_modified": last_modified,
        "size_bytes": size_bytes,
        "url": f"https://github.com/getjeevan/ashle-gardens/blob/main/{filepath}"
    }

def main():
    docs = []
    for root, dirs, files in os.walk('docs-raw'):
        for file in files:
            if file.endswith('.md') and file.lower() != 'readme.md':
                filepath = os.path.join(root, file)
                doc_data = process_md_file(filepath)
                if doc_data:
                    docs.append(doc_data)

    # Sort docs by last modified date descending by default
    docs.sort(key=lambda x: x['last_modified'], reverse=True)

    output = {
        "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "total_docs": len(docs),
        "total_words": sum(d['word_count'] for d in docs),
        "domains_covered": len(set(d['domain'] for d in docs)),
        "documents": docs
    }

    with open('research-data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    print(f"Generated research-data.json with {len(docs)} documents.")

if __name__ == "__main__":
    main()
