def r(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** 0.5

def spherical_harmonics_functions(l, m, x, y, z):
    pi = 3.141592653589793
    return {
        (0, 0):     lambda x, y, z: 0.5 * (1 / pi) ** 0.5,
        (1, -1):    lambda x, y, z: (3 / (4 * pi)) ** 0.5 * y / r(x, y, z),
        (1, 0):     lambda x, y, z: (3 / (4 * pi)) ** 0.5 * z / r(x, y, z),
        (1, 1):     lambda x, y, z: (3 / (4 * pi)) ** 0.5 * x / r(x, y, z),
        (2, -2):    lambda x, y, z: 0.5 * (15 / pi) ** 0.5 * x * y / r(x, y, z) ** 2,
        (2, -1):    lambda x, y, z: 0.5 * (15 / pi) ** 0.5 * z * y / r(x, y, z) ** 2,
        (2, 0):     lambda x, y, z: 0.25 *(5 / pi) ** 0.5 * (-x ** 2 - y ** 2 + 2 * z ** 2) / r(x, y, z) ** 2,
        (2, 1):     lambda x, y, z: 0.5 * (15 / pi) ** 0.5 * x * z / r(x, y, z) ** 2,
        (2, 2):     lambda x, y, z: 0.25 * (15 / pi) ** 0.5 * (x ** 2 - y ** 2) / r(x, y, z) ** 2,
        (3, -3):    lambda x, y, z: 0.25 * (25 / (2 * pi)) ** 0.5 * (3 * x ** 2 - y ** 2) * y / r(x, y, z) ** 3,
        (3, -2):    lambda x, y, z: 0.5 * (105 / pi) ** 0.5 * x * y * z / r(x, y, z) ** 3,
        (3, -1):    lambda x, y, z: 0.25 * (21 / (2 * pi)) ** 0.5 * y * (4 * z ** 2 - x ** 2 - y ** 2) / r(x, y, z) ** 3,
        (3, 0):     lambda x, y, z: 0.25 * (7 / pi) ** 0.5 * z * (2 * z ** 2 - 3 * x ** 2 - 3 * y **2) / r(x, y, z) ** 3,
        (3, 1):     lambda x, y, z: 0.25 * (21 / (2 * pi)) ** 0.5 * x * (4 * z ** 2 - x ** 2 - y ** 2) / r(x, y, z) ** 3,
        (3, 2):     lambda x, y, z: 0.25 * (105 / pi) ** 0.5 * (x ** 2 - y ** 2) * z / r(x, y, z) ** 3,
        (3, 3):     lambda x, y, z: 0.25 * (25 / (2 * pi)) ** 0.5 * (x ** 2 - 3 * y ** 2) * x / r(x, y, z) ** 3,
        (4, -4):     lambda x, y, z: 0.75 * (35 / pi) ** 0.5 * x * y * (x ** 2 - y ** 2) / r(x, y, z) ** 4,
        (4, -3):     lambda x, y, z: 0.75 * (35 / (2 * pi)) ** 0.5 * z * y * (3 * x ** 2 - y ** 2) / r(x, y, z) ** 4,
        (4, -2):     lambda x, y, z: 0.75 * (5 / pi) ** 0.5 * x * y * (7 * z ** 2 - r(x, y, z) ** 2) / r(x, y, z) ** 4,
        (4, -1):     lambda x, y, z: 0.75 * (5 / (2 * pi)) ** 0.5 * z * y * (7 * z ** 2 - 3 * r(x, y, z) ** 2) / r(x, y, z) ** 4,
        (4, 0):     lambda x, y, z: 3 / 16 * (1 / pi) ** 0.5 * (35 * z ** 4 - 30 * z ** 2 * r(x, y, z) ** 2 + 3 * r(x, y, z) ** 4) / r(x, y, z) ** 4,
        (4, 1):     lambda x, y, z: 0.75 * (5 / (2 * pi)) ** 0.5 * z * x * (7 * z ** 2 - 3 * r(x, y, z) ** 2) / r(x, y, z) ** 4,
        (4, 2):     lambda x, y, z: 3 / 8 * (5 / pi) ** 0.5 (x ** 2 - y ** 2) * (7 * z ** 2 - r(x, y, z) ** 2) / r(x, y, z) ** 4,
        (4, 3):     lambda x, y, z: 0.75 * (35 / (2 * pi)) ** 0.5 * z * x * (x ** 2 - 3 * y ** 2) / r(x, y, z) ** 4,
        (4, 4):     lambda x, y, z: 3 / 16 * (35 / pi) ** 0.5 * (x ** 2 * (x ** 2 - 3 * y ** 2) - y ** 2 * (3 * x ** 2 - y ** 2)) / r(x, y, z) ** 4,
    }[l, m](x, y, z)

def spherical_harmonics_single_value(x, y, z, l, m):
    try:
        return spherical_harmonics_functions(l, m, x, y, z)
    except ZeroDivisionError:
        return None

def spherical_harmonics(x, y, z, l, m):
    return [[spherical_harmonics_single_value(*col, l, m) for j, col in enumerate(row)] for i, row in enumerate(heatmap(x, y, z))]
    
def heatmap(iterable1, iterable2, z=None):
    return [[(i, j, z) if z is not None else (i, j) for j in iterable2] for i in iterable1]

def arange(lo, hi, num=50):
    ans = []
    val = lo
    step = (hi - lo) / num
    while val < hi:
        ans.append(val)
        val += step

    return ans

def update(source):
    lo = source.data['lo'][0]
    hi = source.data['hi'][0]
    num = source.data['num'][0]
    z = source.data['z'][0]
    l = source.data['l'][0]
    m = source.data['m'][0]
    
    try:
        rnd = Math.round
    except NameError:
        def rnd(val):
            return val // 1 if val % 1 < 0.5 else val // 1 + 1

    z = rnd(z * 10) / 10
    l = rnd(l)
    m = rnd(m)

    ## This code is commented out for now to decrease the size of the html file
    ## It was originally included to speed up the calculation of the image but it does not
    ## seem to improve that much.
    # key = []
    # for v in z, l, m:
    #     try:
    #         key.append(z.__str__())
    #     except:
    #         key.append(String(v))

    # key = ", ".join(key)

    # if key in source.data:
        # source.data['image'] = source.data[key]
    # else:
    value = spherical_harmonics(
        arange(lo, hi, num),
        arange(lo, hi, num),
        z, l, m
    )
    source.data['image'] = [value]
        # source.data[key] = [value]
