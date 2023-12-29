red = 255
green = 0
blue = 0
st = 1

def cycleColors():
    if st == 1:
        green=green+0.03124999936
    elif st == 2:
        red=red-0.03124999936
    elif st == 3:
        blue=blue+0.03124999936
    elif st == 4:
        green=green-0.03124999936
    elif st == 5:
        red=red+0.03124999936
    elif st == 6:
        blue=blue-0.03124999936

    if int(red) == 256:
        r = 255
        st = 6
    if int(green) == 256:
        g = 255
        st = 2
    if int(blue) == 256:
        b = 255
        st = 4
    if int(red) < 0:
        r = 0
        st = 3
    if int(green) < 0:
        g = 0
        st = 5
    if int(blue) < 0:
        b = 0
        st = 1
    return (int(red), int(green), int(blue))