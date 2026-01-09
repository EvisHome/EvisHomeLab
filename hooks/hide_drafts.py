import logging
from mkdocs.structure.nav import Page, Section

log = logging.getLogger("mkdocs")

def on_nav(nav, config, files):
    """
    Filter out pages marked as 'draft: true' from the navigation.
    """
    def get_draft_status(page):
        # 1. Trust internal meta if available (e.g. if loaded by another plugin)
        if page.meta and page.meta.get('draft', False) is True:
            return True
            
        # 2. Fallback: Read file manually because on_nav runs before properties are parsed
        try:
            with open(page.file.abs_src_path, 'r', encoding='utf-8') as f:
                # Read first line
                first = f.readline()
                if not first.strip() == '---':
                    return False
                
                # Read block until next '---'
                frontmatter = ""
                for line in f:
                    if line.strip() == '---':
                        break
                    frontmatter += line
                
                # Check for "draft: true" string to avoid heavy YAML import if possible?
                # Or just basic parsing. Safe parsing is better.
                if 'draft: true' in frontmatter:
                     return True
                     
        except Exception as e:
            log.warning(f"Failed to read frontmatter for {page.file.src_path}: {e}")
            
        return False

    def filter_items(items):
        filtered = []
        for item in items:
            if isinstance(item, Page):
                if get_draft_status(item):
                    # log.info(f"Hiding draft from nav: {item.file.src_path}")
                    continue
            elif isinstance(item, Section):
                item.children = filter_items(item.children)
                if not item.children:
                   continue
            
            filtered.append(item)
        return filtered

    nav.items = filter_items(nav.items)
    return nav
