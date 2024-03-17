import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#FFFFFF"):  # Змінено колір за замовчуванням на білий
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def generate_color_bfs(step, total_steps):
    """Генерує колір від темного до світлого відтінку."""
    intensity = 0 + total_steps * 26
    return f'#{intensity:02X}{intensity:02X}FF'  # Відтінки синього
def generate_color_dfs(step, total_steps):
    """Генерує колір від темного до світлого відтінку."""
    intensity = 0 + int((step / total_steps) * 255)
    return f'#{intensity:02X}{intensity:02X}FF'  # Відтінки синього

def dfs(node, action, step=0, total_steps=0):
    """Обхід в глибину з виконанням дії для кожного вузла."""
    if node is not None:
        action(node, step, total_steps)
        step += 1
        step = dfs(node.left, action, step, total_steps)
        step = dfs(node.right, action, step, total_steps)
    return step

def bfs(root, action):
    """Обхід в ширину з виконанням дії для кожного вузла."""
    queue = deque([(root, 0)])
    total_steps = len(queue)
    while queue:
        node, step = queue.popleft()
        if node is not None:
            action(node, step, total_steps)
            total_steps += 1
            queue.append((node.left, step + 1))
            queue.append((node.right, step + 1))

def colorize_node_bfs(node, step, total_steps):
    """Змінює колір вузла в BFS."""
    node.color = generate_color_bfs(step, total_steps)

def colorize_node_dfs(node, step, total_steps):
    """Змінює колір вузла в DFS."""
    node.color = generate_color_dfs(step, total_steps)

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

#Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Використання
total_steps = dfs(root, lambda node, step, total_steps: None)  # Підрахунок кількості кроків
dfs(root, colorize_node_dfs, total_steps=total_steps)  # DFS з зміною кольору
# bfs(root, colorize_node_bfs)  # BFS з зміною кольору

draw_tree(root)  # Візуалізація дерева
#print(total_steps)
