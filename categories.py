from nodeitems_utils import NodeCategory

class NodearamaCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == "Nodearama"
