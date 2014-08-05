import bpy

class POSView(bpy.types.Node):
    bl_idname = "POSView"
    bl_label = "POS View"

    def init(self, context):
        self.inputs.new("XYZSocketIn", "XYZ")

    def update(self):
        print("POSView.update: Printing links")
        count = 0
        for link in self.inputs['XYZ'].links:
            print(link)
            count += 1

        if count > 0:
            from_socket = self.inputs['XYZ'].links[0].from_socket
            print("Reading POSView input:", from_socket, from_socket.array)
            for point in from_socket.array:
                print("point", point.value[0], point.value[1], point.value[2])

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.label("Hello World!")
        #print("array", self.inputs['XYZ'].array)
