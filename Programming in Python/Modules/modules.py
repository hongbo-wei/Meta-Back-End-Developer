import calendar

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)

def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()