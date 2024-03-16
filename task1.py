class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_before(self, next_node: Node, data):
        if next_node is None:
            print("Наступного вузла не існує.")
            return
        new_node = Node(data)
        next_node.next = new_node.next
        new_node.next = next_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        if self.head is None or self.head.next is None:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.insert_in_sorted_order(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def insert_in_sorted_order(self, head, node):
        if not head or node.data < head.data:
            node.next = head
            return node
        else:
            current = head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
            return head

    def merge_sorted_lists(self, list1, list2):
        dummy = Node()
        tail = dummy
        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next


# Створення списку
ll = LinkedList()

# Вставка елементів на початок і в кінець списку
ll.insert_at_end(10)
ll.insert_at_beginning(5)
ll.insert_at_end(15)

print("Список:")
ll.print_list()

# Пошук елемента
found_node = ll.search_element(10)
if found_node:
    print("Пошук 10 у списку")
    print("Елемент знайдено")
else:
    print("Елемент не знайдено.")

# Вставка елемента перед іншим вузлом
node_to_insert_before = ll.search_element(10)
if node_to_insert_before:
    prev_node = ll.search_element(node_to_insert_before.data - 1)
    if prev_node:
        ll.insert_after(prev_node, 7)
    else:
        ll.insert_at_beginning(7)

# Вставка елемента після іншого вузла
node_to_insert_after = ll.search_element(7)
if node_to_insert_after:
    ll.insert_after(node_to_insert_after, 8)

print("Список після вставок:")
ll.print_list()

# Видалення вузла
ll.delete_node(15)

# Виведення списку
print("Список після видалення 15:")
ll.print_list()

# Реверсування списку
ll.reverse()
print("Реверсований список:")
ll.print_list()

# Сортування списку
ll.sort()
print("Відсортований список:")
ll.print_list()


ll2 = LinkedList()
ll2.insert_at_end(1)
ll2.insert_at_end(2)
ll2.insert_at_end(3)
ll2.insert_at_end(4)
ll2.insert_at_end(6)
ll2.insert_at_end(8)
ll2.insert_at_end(9)

# Злиття відсортованих списків
merged_list_head = ll.merge_sorted_lists(ll.head, ll2.head)
merged_list = LinkedList()
merged_list.head = merged_list_head
print("Злитий відсортований список:")
merged_list.print_list()

# Приклад використання функції reverse
print("\nПриклад використання reverse")
print("Oригінальний список:")
merged_list.print_list()
merged_list.reverse()
print("Список після реверсування:")
merged_list.print_list()

# Приклад використання функції sort
llist = LinkedList()
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(2)
print("\nПриклад використання sort")
print("Оригінальний список:")
llist.print_list()
llist.sort()
print("Відсортований список:")
llist.print_list()

# Приклад використання функції merge_sorted_lists
llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)
llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)
print("\nПриклад використання merge_sorted_lists")
print("Перший відсортований список:")
llist1.print_list()
print("Другий відсортований список:")
llist2.print_list()
merged_head = llist1.merge_sorted_lists(llist1.head, llist2.head)
# Для виведення об'єднаного списку, потрібно тимчасово змінити голову першого списку
temp_head = llist1.head  # Зберігаємо оригінальну голову першого списку
llist1.head = merged_head  # Встановлюємо голову об'єднаного списку
print("\nОб'єднаний відсортований список:")
llist1.print_list()
llist1.head = temp_head  # Відновлюємо оригінальну голову першого списку