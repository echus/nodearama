# === Module information ===
bl_info = {
    "name": "Nodearama",
    "author": "Varvara Efremova",
    "version": (0, 0, 1),
    "blender": (2, 7, 0),
    "location": "Nodes > CustomNodesTree > Add user nodes",
    "description": "Node-based Atom Probe data analysis",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Node"}

import bpy
import nodeitems_utils

# === Registration ===
# UI modules
from Nodearama.app.interface import tree, nodes, sockets, categories
# NodeTree category list
from Nodearama.app.interface.categories import categories

def register():
    bpy.utils.register_module(__name__)
    nodeitems_utils.register_node_categories("CUSTOM_CATEGORIES", categories)

def unregister():
    bpy.utils.unregister_module(__name__)
    nodeitems_utils.unregister_node_categories("CUSTOM_CATEGORIES")

if __name__ == "__main__":
    register()
