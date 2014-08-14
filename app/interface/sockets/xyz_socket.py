import bpy
import numpy as np

# === Socket display settings ===
LABEL      = "XYZ Points"
DRAW_LABEL = "XYZ"
COLOR      = (1, 0.53, 0.25, 1)

# === Socket interface ===
class XYZSocket(bpy.types.NodeSocket):
    bl_label = LABEL

    # === Properties ===
    value = bpy.props.FloatVectorProperty()

    def draw(self, context, layout, node, x):
        layout.label(self.name)
        #layout.label(DRAW_LABEL)

    def draw_color(self, context, node):
        return COLOR
