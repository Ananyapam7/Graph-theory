from networkx import *
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

my_graph = nx.Graph()

my_graph.add_node(1)

my_graph.add_node(2)

my_graph.add_node(3)

my_graph.add_edge(1,2)

print (nx.info(my_graph))
print (nx.number_of_nodes(my_graph))
print (nx.is_directed(my_graph))

nx.draw(my_graph)
