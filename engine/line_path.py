def line_path(x0, y0, x1, y1):
    output = []
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx-dy
    while True:
        xy = []
        xy.append(x0)
        xy.append(y0)
        output.append(xy)
        if x0 == x1 and y0 == y1:
            return output

        e2 = 2 * err
        if e2 > -dy:
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            err = err + dx
            y0 = y0 + sy



