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
        self.outputs.new("XYZSocketOut", "XYZ")
        #self.outputs.new("CustomNodeSocket", "m/c")

    def update(self):
        point = random.randint(-20, 20)
        print("update(): Adding random point to POSRead out socket", point)
        new_point = self.outputs['XYZ'].array.add()
        new_point.value = (point, point, point)

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "pos_filename", text="POS")
        col.prop(self, "rng_filename", text="RNG")
