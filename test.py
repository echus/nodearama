from app.model.nodes import POSReadNode, POSViewNode
from app.model import NodeGraph

import os.path

read = POSReadNode()
read.pos_path = os.path.abspath("./data/R04.pos")
read.rng_path = os.path.abspath("./data/R04.rng")

view = POSViewNode()

g = NodeGraph()
g.add_node(read)
g.add_node(view)
g.connect(read, view, 0, 0)

print(g.evaluate())
