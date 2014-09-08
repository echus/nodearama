from nodeitems_utils import NodeCategory, NodeItem

# === Category class def ===
class NodearamaCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == "Nodearama"

# === Category list def ===
categories = [NodearamaCategory("ANALYSIS", "Analysis",
                items = [NodeItem("POSReadNode"),
                         NodeItem("POSViewNode"),
                         #NodeItem("POSSplit"),
                         #NodeItem("Vox"),
                         #NodeItem("Isosurf"),
                         #NodeItem("Division"),
                         ]),
        ]
