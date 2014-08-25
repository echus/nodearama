import bpy

class NodearamaTree(bpy.types.NodeTree):
    bl_description = "Atom probe analysis nodes"
    bl_icon = "MESH_CYLINDER"
    bl_idname = "Nodearama"
    bl_label = "Nodearama"

    def update(self):
        # Scene global observable for communicating with Adapter
        obs = bpy.context.scene.observable

        obs.notify_observers("nodetree-update")
