from app.model.nodes import NodeFactory
from app.model import NodeGraph

import os.path

read = NodeFactory.make("POSReadNode")
read.pos_path = os.path.abspath("./data/R04.pos")
read.rng_path = os.path.abspath("./data/R04.rng")

view = NodeFactory.make("POSViewNode")

g = NodeGraph()
g.add_node(read)
g.add_node(view)
g.connect(read, view, 0, 0)

print(g.evaluate())
