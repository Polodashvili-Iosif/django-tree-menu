from typing import Any, Dict, List, Optional

from django import template
from django.template import Context

from ..models import Menu, MenuItem

register = template.Library()


def find_active_item(
    items: List[MenuItem], current_path: str
) -> Optional[MenuItem]:
    for item in items:
        url = item.get_url()
        if url and not url.startswith('/'):
            url = '/' + url
        if url == current_path:
            return item
    return None


def build_tree(
    all_items: List[MenuItem],
    active_item: Optional[MenuItem]
) -> List[MenuItem]:
    id_map = {}
    tree = []
    for item in all_items:
        item.tree_children = []
        item.active = False
        item.expanded = False
        id_map[item.id] = item

    for item in all_items:
        if item.parent_id:
            parent = id_map.get(item.parent_id)
            if parent:
                parent.tree_children.append(item)
        else:
            tree.append(item)

    current = active_item
    current.active = True
    while current:
        current.expanded = True
        current = id_map.get(current.parent_id)

    return tree


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context: Context, menu_name: str) -> Dict[str, Any]:
    request = context.get('request')
    current_path = request.path if request else '/'

    try:
        menu = Menu.objects.prefetch_related('items').get(title=menu_name)
    except Menu.DoesNotExist:
        return {'menu_items': []}

    all_items = menu.items.all()
    active_item = find_active_item(all_items, current_path)
    tree = build_tree(all_items, active_item)

    return {'menu_items': tree}
