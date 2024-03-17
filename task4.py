import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap_array):
    """
    Функція для побудови бінарного дерева з масиву бінарної купи.
    :param heap_array: Масив, що представляє бінарну купу.
    :return: Корінь бінарного дерева.
    """
    # Функція для створення вузла дерева з індексу в масиві купи
    def create_node_from_heap(index):
        if index < len(heap_array):
            node = Node(heap_array[index])
            node.left = create_node_from_heap(2 * index + 1)
            node.right = create_node_from_heap(2 * index + 2)
            return node
        return None

    # Створення кореня дерева, починаючи з індексу 0
    return create_node_from_heap(0)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
draw_tree(root) #Відображення дерева з прикладу коду

# Створення бінарної купи (приклад)
    # Припустимо, що у нас є бінарна купа у вигляді масиву
heap_array = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
heapq.heapify(heap_array)
    # Побудова дерева з купи
heap_tree_root = build_heap_tree(heap_array)
    # Відображення бінарної купи у вигляді дерева
draw_tree(heap_tree_root)