import bpy

class NodearamaTree(bpy.types.NodeTree):
    bl_description = "Atom probe analysis nodes"
    bl_icon = "MESH_CYLINDER"
    bl_idname = "Nodearama"
    bl_label = "Nodearama"

    def update(self):
        print("NodeTree.update()")
