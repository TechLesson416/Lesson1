# Рекурсия - функция вызывает сама себя
# def factorial(count): #5! = 1 * 2 * 3 * 4 * 5 = 120
#     result = 1
#     for i in range(2, count + 1):
#         result *= i
#     return result
#
# for x in range(10):
#     print(x, factorial(x))

# def factorial(x):
#     if x == 1 or x == 0:
#         return 1
#     return x * factorial(x - 1)
#
# for x in range(10):
#     print(x, factorial(x))

# Черепашья графика

# N  = 5
#
import turtle as t
t.speed(0)
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
#
# t.bgcolor('black')
# angle = 360 // len(colors) - 1
#
# for x in range(200):
#     t.pencolor(colors[x % len(colors)])
#     t.width(x // 100 + 1)
#     t.forward(x)
#     t.left(angle)
#
# t.penup()
# t.goto( 100, 200 )
# t.pendown()
#
# def square(side):
#     for _ in range(4):
#         t.forward(side)
#         t.right(90)
#
# def flower():
#     for _ in range(36):
#         t.circle(50)
#         t.right(10)

def tree(length):
    if length < 10:
        return
    t.forward(lenth)
    t.left(30)
    tree(length * 0.7)
    t.right(60)
    tree(length * 0.7)
    t.left(30)
    t.backward(length)
   # flower()

t.left(90)
tree(100)

t.mainloop()