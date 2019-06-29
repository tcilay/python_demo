import turtle

turtle.bgcolor("black")
colors=["blue","yellow","green","red","pink","white"]

words = []
word = turtle.textinput("表白","输入你想说的话或enter退出：")
while word != '':
    words.append(word)
    word = turtle.textinput("表白","输入你想说的话或enter退出：")

for x in range(100):
    turtle.pencolor(colors[x%len(words)])
    turtle.penup()
    turtle.forward(x*4)
    turtle.pendown()
    turtle.write(words[x%len(words)],font=("Arial",int((x+4)/4)))
    turtle.left(360/len(words)+2)
