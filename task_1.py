import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edges = [
    (0, 2, 25),  # Terminal 1 -> Storage 1
    (0, 3, 20),  # Terminal 1 -> Storage 2
    (0, 4, 15),  # Terminal 1 -> Storage 3
    (1, 4, 15),  # Terminal 2 -> Storage 3
    (1, 5, 30),  # Terminal 2 -> Storage 4
    (1, 3, 10),  # Terminal 2 -> Storage 2
    (2, 6, 15),  # Storage 1 -> Store 1
    (2, 7, 10),  # Storage 1 -> Store 2
    (2, 8, 20),  # Storage 1 -> Store 3
    (3, 9, 15),  # Storage 2 -> Store 4
    (3, 10, 10),  # Storage 2 -> Store 5
    (3, 11, 25),  # Storage 2 -> Store 6
    (4, 12, 20),  # Storage 3 -> Store 7
    (4, 13, 15),  # Storage 3 -> Store 8
    (4, 14, 10),  # Storage 3 -> Store 9
    (5, 15, 20),  # Storage 4 -> Store 10
    (5, 16, 10),  # Storage 4 -> Store 11
    (5, 17, 15),  # Storage 4 -> Store 12
    (5, 18, 5),  # Storage 4 -> Store 13
    (5, 19, 10),  # Storage 4 -> Store 14

]

G.add_weighted_edges_from(edges)

pos = {
    0: (1, 2),  # Terminal 1
    1: (5, 2),  # Terminal 2
    2: (2, 3),  # Storage 1
    3: (4, 3),  # Storage 2
    4: (2, 1),  # Storage 3
    5: (4, 1),  # Storage 4
    6: (0, 4),  # Store 1
    7: (1, 4),  # Store 2
    8: (2, 4),  # Store 3
    9: (3, 4),  # Store 4
    10: (4, 4),  # Store 5
    11: (5, 4),  # Store 6
    12: (0, 0),  # Store 7
    13: (1, 0),  # Store 8
    14: (2, 0),  # Store 9
    15: (3, 0),  # Store 10
    16: (4, 0),  # Store 11
    17: (5, 0),  # Store 12
    18: (6, 0),  # Store 13
    19: (7, 0),  # Store 14
}

node_labels = {
    0: 'Terminal 1',
    1: 'Terminal 2',
    2: 'Storage 1',
    3: 'Storage 2',
    4: 'Storage 3',
    5: 'Storage 4',
    6: 'Store 1',
    7: 'Store 2',
    8: 'Store 3',
    9: 'Store 4',
    10: 'Store 5',
    11: 'Store 6',
    12: 'Store 7',
    13: 'Store 8',
    14: 'Store 9',
    15: 'Store 10',
    16: 'Store 11',
    17: 'Store 12',
    18: 'Store 13',
    19: 'Store 14'
}

plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=2000, node_color="skyblue", font_size=8, font_weight="bold", arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
