import turtle

def draw_tree(t, branch_length, level):
    if level <= 0:
        return
    else:
        # Малюємо основну гілку
        t.forward(branch_length)
        # Малюємо праву гілку
        t.right(20)
        draw_tree(t, 1 * branch_length, level - 1)
        # Повертаємося до основної гілки і малюємо ліву гілку
        t.left(40)
        draw_tree(t, 1 * branch_length, level - 1)
        # Повертаємося до початкового стану
        t.right(20)
        t.backward(branch_length)

def main():
    turtle.speed('fastest')
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -100)  # Початкова позиція нижче, щоб дерево помістилося
    turtle.down()
    recursion_level = 7
    draw_tree(turtle, 50, recursion_level)
    turtle.done()

if __name__ == "__main__":
    main()