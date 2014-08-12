import bpy

class POSView(bpy.types.Node):
    bl_idname = "POSView"
    bl_label = "POS View"

    def init(self, context):
        self.inputs.new("XYZSocket", "XYZ in")

    def update(self):
        print("POSView.update()")

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.label("Hello World!")
