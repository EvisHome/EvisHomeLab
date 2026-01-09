import logging
from mkdocs.structure.nav import Page, Section

log = logging.getLogger("mkdocs")

def on_nav(nav, config, files):
    """
    Filter out pages marked as 'draft: true' from the navigation.
    """
    def filter_items(items):
        filtered = []
        for item in items:
            if isinstance(item, Page):
                if item.meta.get('draft', False) is True:
                    # log.info(f"Hiding draft from nav: {item.file.src_path}")
                    continue
            elif isinstance(item, Section):
                # Recursively filter children
                item.children = filter_items(item.children)
                # If section becomes empty, hide it (optional but cleaner)
                if not item.children:
                   continue
            
            filtered.append(item)
        return filtered

    nav.items = filter_items(nav.items)
    return nav
