import bpy
from bpy.props import PointerProperty, StringProperty

# temp testing
import random

class POSRead(bpy.types.Node):
    bl_idname = "POSRead"
    bl_label = "POS Read"

    pos_filename = StringProperty(subtype='FILE_PATH', default="//")
    rng_filename = StringProperty(subtype='FILE_PATH', default="//")

    def init(self, context):
        obs = bpy.context.scene.observable

        self.outputs.new("XYZSocket", "XYZ")
        #self.outputs.new("CustomNodeSocket", "m/c")

        obs.notify_observers("node-init")

    def update(self):
        # Get scene global observable
        obs = bpy.context.scene.observable

        obs.notify_observers("node-update")

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "pos_filename", text="POS")
        col.prop(self, "rng_filename", text="RNG")
