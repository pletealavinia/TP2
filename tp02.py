ex1

def on_forever():
    basic.show_string("Lavinia")
    basic.pause(2000)
    basic.clear_screen()
basic.forever(on_forever)

ex2
def on_forever():
    led.toggle(2, 3)
basic.forever(on_forever)

ex3

def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

ex4
for i in range(10):
    if i % 2 == 0:
        basic.show_number(i)

ex5
for index in range(9):
    for i in range(10):
        if i % 2 == 1:
            basic.show_number(i)

ex6
index = 0

def on_button_pressed_a():
    global index
    index = 4
    while index >= 0:
        led.plot(index, index)
        index += -1
input.on_button_pressed(Button.A, on_button_pressed_a)
