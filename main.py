import os
import yaml
from datetime import datetime

def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    """

    def get_articles(env):
        articles_dir = os.path.join(env.project_dir, 'docs', 'home-lab', 'articles')
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
        # Note: We include highlights here too, usually desired. 
        # If user wants to exclude highlights from main list, we can add `and not a['highlight']`
        display_articles = [a for a in articles if not a['draft']]
        
        # HTML Grid: 4 Columns (Compact Style)
        html = '<div class="grid cards" borderless style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; padding: 0px;">\n'
        
        for article in display_articles:
            tags_html = ''
            if article['tags']:
                for tag in article['tags']:
                    tags_html += f'<span style="display: inline-block; background: #333; color: #fff; padding: 2px 8px; border-radius: 10px; font-size: 0.7em; margin-right: 5px; margin-top: 5px;">{tag}</span>'

            html += f'''
  <div class="card">
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
        return html
