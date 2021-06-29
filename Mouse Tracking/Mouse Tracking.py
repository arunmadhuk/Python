# Mouse Tracking
# ! python3
from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    print(pt.x, pt.y)
    return {"x": pt.x, "y": pt.y}


while True:
     print(queryMousePosition())

