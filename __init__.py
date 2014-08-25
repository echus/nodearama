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

# === MVC setup ===
from Nodearama.app.adapter import Adapter
# NodeTree observable scene global
from Nodearama.app.modules.observe import Observable

# === Blender class registration ===
# UI modules
from Nodearama.app.interface import tree, nodes, sockets, categories
# NodeTree category list
from Nodearama.app.interface.categories import categories

def register():
    bpy.utils.register_module(__name__)
    nodeitems_utils.register_node_categories("CUSTOM_CATEGORIES", categories)
    # Scene global used by NodeTree & Nodes for communication with Adapter
    # Workaround due to NodeTree/Node non-persistent classes
    bpy.types.Scene.observable = Observable()
    # Adapter observes nodetree scene global
    bpy.types.Scene.adapter = Adapter(bpy.types.Scene.observable)
    print("Nodearama registered successfully.")

def unregister():
    bpy.utils.unregister_module(__name__)
    nodeitems_utils.unregister_node_categories("CUSTOM_CATEGORIES")
    del bpy.types.Scene.observable

if __name__ == "__main__":
    register()
