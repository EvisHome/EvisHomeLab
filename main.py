import os
import yaml
from datetime import datetime

def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    """

    def get_articles(env):
        articles_dir = os.path.join(env.project_dir, 'docs', 'articles', 'articles')
        articles = []

        # Walk through the articles directory
        for root, dirs, files in os.walk(articles_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    
                    # Read frontmatter
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Simple frontmatter parsing (assuming standard --- format)
                    if content.startswith('---'):
                        try:
                            # Extract YAML frontmatter
                            parts = content.split('---', 2)
                            if len(parts) >= 3:
                                frontmatter = yaml.safe_load(parts[1])
                                if frontmatter and 'date' in frontmatter:
                                    # Construct article object
                                    is_draft = frontmatter.get('draft', False)
                                    # We don't filter drafts here, we let the macros decide
                                    
                                    article = {
                                        'title': frontmatter.get('title', 'No Title'),
                                        'date': frontmatter.get('date'),
                                        'image': frontmatter.get('image', 'https://via.placeholder.com/300x200'),
                                        'description': frontmatter.get('description', ''),
                                        'draft': is_draft,
                                        'highlight': frontmatter.get('highlight', False),
                                        'tags': frontmatter.get('tags', [])
                                    }
                                    
                                    # Link Calculation
                                    rel_path_from_articles = os.path.relpath(file_path, articles_dir)
                                    link_url = f"articles/{rel_path_from_articles.replace('.md', '').replace('\\', '/')}"
                                    article['url'] = link_url
                                    
                                    # Image Path Calculation
                                    img_path = article['image']
                                    if not img_path.startswith('http'):
                                         article_sub_dir = os.path.dirname(rel_path_from_articles)
                                         if article_sub_dir:
                                             article['image'] = f"articles/{article_sub_dir}/{img_path}".replace('\\', '/')
                                         else:
                                             article['image'] = f"articles/{img_path}".replace('\\', '/')

                                    articles.append(article)
                        except Exception as e:
                            print(f"Error parsing {file}: {e}")

        # Sort articles by date descending
        articles.sort(key=lambda x: str(x['date']), reverse=True)
        return articles

    @env.macro
    def list_highlights_grid():
        articles = get_articles(env)
        
        # Filter: Highlights Only, No Drafts
        highlight_articles = [a for a in articles if a['highlight'] and not a['draft']]
        
        # HTML Grid: 3 Columns (Original Style)
        html = '<div class="grid cards" borderless style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 0px;">\n'
        
        for article in highlight_articles:
            tags_html = ''
            if article['tags']:
                for tag in article['tags']:
                    tags_html += f'<span style="display: inline-block; background: #333; color: #fff; padding: 2px 8px; border-radius: 10px; font-size: 0.7em; margin-right: 5px; margin-top: 5px;">{tag}</span>'
            
            html += f'''
  <div class="card">
    <a href="{article['url']}" style="text-decoration: none; color: inherit; display: block;">
    <img src="{article['image']}" alt="{article['title']}" style="width:100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 8px 8px 0 0;">
    <div style="padding: 10px;">
      <h3>{article['title']}</h3>
      <p>{article['description']}</p>
      <div style="margin-top: 8px;">{tags_html}</div>
    </div>
    </a>
  </div>
'''
        html += '</div>'
        return html

    @env.macro
    def list_articles_grid():
        articles = get_articles(env)
        
        # Filter: No Drafts
        display_articles = [a for a in articles if not a['draft']]
        
        # 1. Collect all unique tags (Case Insensitive Merging)
        # Map: lowercase_tag -> Display Tag
        tag_map = {}
        
        for article in display_articles:
            if article['tags']:
                for tag in article['tags']:
                    low_tag = tag.lower().strip()
                    # If not yet recorded, or if the new version looks 'nicer' (has more capitals), update it?
                    # For stability, let's just keep the first one or favor upper case.
                    # Simple heuristic: if existing is all lower, and new has upper, take new.
                    if low_tag not in tag_map:
                        tag_map[low_tag] = tag.strip()
                    else:
                        # Optional: implementation to prefer "Home Assistant" over "home assistant"
                        current_display = tag_map[low_tag]
                        if current_display.islower() and not tag.islower():
                             tag_map[low_tag] = tag.strip()

        # Sort tags by their display name for the UI
        sorted_keys = sorted(tag_map.keys(), key=lambda k: tag_map[k].lower())

        # 2. Build the Filter Cloud HTML
        # Mobile-friendly CSS
        html = '''
<style>
    .article-grid-responsive {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        padding: 0;
    }
    @media screen and (max-width: 1100px) {
        .article-grid-responsive { grid-template-columns: repeat(3, 1fr); }
    }
    @media screen and (max-width: 768px) {
        .article-grid-responsive { grid-template-columns: repeat(2, 1fr); }
    }
    @media screen and (max-width: 480px) {
        .article-grid-responsive { grid-template-columns: 1fr; }
    }
</style>
'''
        html += '<div style="margin-bottom: 20px;">'
        # 'All' button
        html += '<button data-tag="all" onclick="toggleFilter(\'all\')" style="margin-right: 5px; margin-bottom: 5px; padding: 5px 10px; border: 1px solid #444; background: #00C853; color: white; cursor: pointer; border-radius: 15px;">All</button>'
        
        for key in sorted_keys:
            display_name = tag_map[key]
            # data-tag uses the lowercase key for logic
            html += f'<button data-tag="{key}" onclick="toggleFilter(\'{key}\')" style="margin-right: 5px; margin-bottom: 5px; padding: 5px 10px; border: 1px solid #444; background: #252933; color: #ccc; cursor: pointer; border-radius: 15px;">{display_name}</button>'
        html += '</div>'

        # 3. Build the Grid 
        # Removed inline style logic in favor of .article-grid-responsive class
        html += '<div id="article-grid" class="grid cards article-grid-responsive" borderless>\n'
        
        for article in display_articles:
            # Prepare tag string for data attribute (LOWERCASE for logic match)
            if article['tags']:
                # We assume the article tags match the keys in our map (by lowering)
                article_tags_lower = [t.lower().strip() for t in article['tags']]
                article_tags_str = ",".join(article_tags_lower)
            else:
                article_tags_str = ""
            
            # Prepare visual pills (Keep original display)
            tags_html = ''
            if article['tags']:
                for tag in article['tags']:
                    tags_html += f'<span style="display: inline-block; background: #333; color: #fff; padding: 2px 8px; border-radius: 10px; font-size: 0.7em; margin-right: 5px; margin-top: 5px;">{tag}</span>'

            html += f'''
  <div class="card article-card" data-tags="{article_tags_str}">
    <a href="{article['url']}" style="text-decoration: none; color: inherit; display: block;">
    <img src="{article['image']}" alt="{article['title']}" style="width:100%; aspect-ratio: 4/3; object-fit: cover; border-radius: 8px 8px 0 0;">
    <div style="padding: 8px;">
      <h3 style="margin: 0; font-size: 1.0em; line-height: 1.2;">{article['title']}</h3>
      <p style="margin-top: 4px; font-size: 0.8em; color: #aaa;">{article['date']}</p>
      <p style="margin-top: 4px; font-size: 0.85em; line-height: 1.4;">{article['description']}</p>
      <div style="margin-top: 6px;">{tags_html}</div>
    </div>
    </a>
  </div>
'''
        html += '</div>'

        # 4. Inject Client-Side Filtering Script (Multi-Select)
        html += '''
<script>
// State to track selected tags
var activeTags = new Set();

function toggleFilter(tag) {
    const buttons = document.querySelectorAll('button[data-tag]');
    const cards = document.querySelectorAll('.article-card');

    // 1. Update State
    if (tag === 'all') {
        activeTags.clear();
    } else {
        if (activeTags.has(tag)) {
            activeTags.delete(tag);
        } else {
            activeTags.add(tag);
        }
    }

    // 2. Update Buttons UI
    buttons.forEach(btn => {
        const btnTag = btn.getAttribute('data-tag');
        const isActive = activeTags.has(btnTag);
        const isAllActive = activeTags.size === 0 && btnTag === 'all';
        
        if (isActive || isAllActive) {
             btn.style.background = '#00C853'; 
             btn.style.color = '#fff';
        } else {
             // Inactive Style
             btn.style.background = btnTag === 'all' ? '#333' : '#252933';
             btn.style.color = btnTag === 'all' ? '#fff' : '#ccc';
        }
    });

    // 3. Filter Cards (OR Logic: Show if card has ANY of the active tags)
    cards.forEach(card => {
        const cardTags = card.getAttribute('data-tags').split(',');
        
        if (activeTags.size === 0) {
            // Show all if no filter
            card.style.display = 'block';
        } else {
            // Check if card has at least one active tag
            const hasMatch = cardTags.some(t => activeTags.has(t));
            card.style.display = hasMatch ? 'block' : 'none';
        }
    });
}
</script>
'''
        return html
