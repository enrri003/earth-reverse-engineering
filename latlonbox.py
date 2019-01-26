from collections import namedtuple

LatLonBox = namedtuple('LatLonBox', ['north', 'south', 'west', 'east'])


def is_latlonbox_overlapping(box1, box2):
    n1, s1, w1, e1 = box1
    n2, s2, w2, e2 = box2

    n = min(n1, n2)
    s = max(s1, s2)
    w = max(w1, w2)
    e = min(e1, e2)

    return (n >= s) and (w <= e)
