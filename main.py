import os
import yaml
from datetime import datetime

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

    @env.macro
    def list_articles_grid():
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
                                    # Create relative link
                                    rel_dir = os.path.relpath(root, os.path.join(env.project_dir, 'docs'))
                                    rel_path = f"{rel_dir}/{file}".replace('\\', '/')
                                    # Fix path if it starts with home-lab/articles
                                    # MkDocs URLs are relative to the page calling the macro usually, 
                                    # but let's try to make it relative to docs root or standard mkdocs link
                                    
                                    # Construct article object
                                    article = {
                                        'title': frontmatter.get('title', 'No Title'),
                                        'date': frontmatter.get('date'),
                                        'image': frontmatter.get('image', 'https://via.placeholder.com/300x200'),
                                        'description': frontmatter.get('description', ''),
                                        'url': f"articles/{file.replace('.md', '')}" # Simplified relative link for index.md
                                    }
                                    
                                    # Check if article is in a subdirectory (e.g. motorized-blinds/motorized-blinds.md)
                                    # If so, link might need adjustment. 
                                    # Assuming structure: docs/home-lab/articles/name.md or docs/home-lab/articles/dir/name.md
                                    
                                    # Let's handle the specific pathing relative to home-lab/index.md
                                    # Index is at docs/home-lab/index.md.
                                    # Articles are at docs/home-lab/articles/...
                                    
                                    # Calculate relative path from home-lab/index.md to the article
                                    # If file is at docs/home-lab/articles/foo.md -> link is articles/foo
                                    # If file is at docs/home-lab/articles/foo/bar.md -> link is articles/foo/bar
                                    
                                    rel_path_from_articles = os.path.relpath(file_path, articles_dir)
                                    link_url = f"articles/{rel_path_from_articles.replace('.md', '').replace('\\', '/')}"
                                    article['url'] = link_url
                                    
                                    # Handle image path
                                    # If image is relative to article, e.g. "thumb.jpg" in same dir
                                    # We need to make it relative to index.md
                                    img_path = article['image']
                                    if not img_path.startswith('http'):
                                         # If image is just "thumb.jpg" and article is in "dir", 
                                         # image path from index should be "articles/dir/thumb.jpg"
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

        # Generate HTML Grid
        html = '<div class="grid cards" borderless style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 0px;">\n'
        
        for article in articles:
            html += f'''
  <div class="card">
    <p><a href="{article['url']}">
    <img src="{article['image']}" alt="{article['title']}" style="width:100%; aspect-ratio: 4/3; object-fit: cover; border-radius: 8px 8px 0 0;">
    <div style="padding: 10px;">
      <h3 style="margin: 0; font-size: 1.1em;">{article['title']}</h3>
      <p style="margin-top: 5px; font-size: 0.9em; color: #ccc;">{article['date']}</p>
      <p style="font-size: 0.9em;">{article['description']}</p>
    </div>
    </a></p>
  </div>
'''
        html += '</div>'
        return html
