import bpy
import numpy as np

# === Socket display settings ===
LABEL      = "XYZ Points"
DRAW_LABEL = "XYZ"
COLOR      = (1, 0.53, 0.25, 1)

class XYZSocket(bpy.types.NodeSocket):
    """XYZSocket mixin class common to input and output sockets"""
    bl_label = LABEL

    def draw(self, context, layout, node, x):
        layout.label(self.name)
        #layout.label(DRAW_LABEL)

    def draw_color(self, context, node):
        return COLOR

class XYZSocketOut(XYZSocket):
    bl_idname = "XYZSocketOut"

    # === Properties ===
    _array = None

    @property
    def array(self):
        return self._array
    @array.setter
    def array(self, value):
        self._array = value

class XYZSocketIn(XYZSocket):
    """Input socket for XYZ data"""
    bl_idname = "XYZSocketIn"


