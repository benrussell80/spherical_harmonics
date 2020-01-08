"""
Functions for the real, Cartesian Spherical Harmonics (Y_lm) for the first 4 values of l as sourced from:
https://en.wikipedia.org/wiki/Table_of_spherical_harmonics

Get each Y_lm function using (l, m) as keys. Dictionary outputs a lambda function that will accept x, y, z as numpy arrays.
"""

import numpy as np
from math import pi

def r(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** 0.5

spherical_harmonics = {
    (0, 0):     lambda x, y, z: np.zeros(x.shape) + 0.5 * np.sqrt(1 / np.pi),
    (1, -1):    lambda x, y, z: np.sqrt(3 / (4 * np.pi)) * y / r(x, y, z),
    (1, 0):     lambda x, y, z: np.sqrt(3 / (4 * np.pi)) * z / r(x, y, z),
    (1, 1):     lambda x, y, z: np.sqrt(3 / (4 * np.pi)) * x / r(x, y, z),
    (2, -2):    lambda x, y, z: 0.5 * np.sqrt(15 / np.pi) * x * y / r(x, y, z) ** 2,
    (2, -1):    lambda x, y, z: 0.5 * np.sqrt(15 / np.pi) * z * y / r(x, y, z) ** 2,
    (2, 0):     lambda x, y, z: 0.25 * np.sqrt(5 / np.pi) * (-x ** 2 - y ** 2 + 2 * z ** 2) / r(x, y, z) ** 2,
    (2, 1):     lambda x, y, z: 0.5 * np.sqrt(15 / np.pi) * x * z / r(x, y, z) ** 2,
    (2, 2):     lambda x, y, z: 0.25 * np.sqrt(15 / np.pi) * (x ** 2 - y ** 2) / r(x, y, z) ** 2,
    (3, -3):    lambda x, y, z: 0.25 * np.sqrt(25 / (2 * np.pi)) * (3 * x ** 2 - y ** 2) * y / r(x, y, z) ** 3,
    (3, -2):    lambda x, y, z: 0.5 * np.sqrt(105 / np.pi) * x * y * z / r(x, y, z) ** 3,
    (3, -1):    lambda x, y, z: 0.25 * np.sqrt(21 / (2 * np.pi)) * y * (4 * z ** 2 - x ** 2 - y ** 2) / r(x, y, z) ** 3,
    (3, 0):     lambda x, y, z: 0.25 * np.sqrt(7 / np.pi) * z * (2 * z ** 2 - 3 * x ** 2 - 3 * y **2) / r(x, y, z) ** 3,
    (3, 1):     lambda x, y, z: 0.25 * np.sqrt(21 / (2 * np.pi)) * x * (4 * z ** 2 - x ** 2 - y ** 2) / r(x, y, z) ** 3,
    (3, 2):     lambda x, y, z: 0.25 * np.sqrt(105 / np.pi) * (x ** 2 - y ** 2) * z / r(x, y, z) ** 3,
    (3, 3):     lambda x, y, z: 0.25 * np.sqrt(25 / (2 * np.pi)) * (x ** 2 - 3 * y ** 2) * x / r(x, y, z) ** 3,
    (4, -4):     lambda x, y, z: 0.75 * np.sqrt(35 / np.pi) * x * y * (x ** 2 - y ** 2) / r(x, y, z) ** 4,
    (4, -3):     lambda x, y, z: 0.75 * np.sqrt(35 / (2 * np.pi)) * z * y * (3 * x ** 2 - y ** 2) / r(x, y, z) ** 4,
    (4, -2):     lambda x, y, z: 0.75 * np.sqrt(5 / np.pi) * x * y * (7 * z ** 2 - r(x, y, z) ** 2) / r(x, y, z) ** 4,
    (4, -1):     lambda x, y, z: 0.75 * np.sqrt(5 / (2 * np.pi)) * z * y * (7 * z ** 2 - 3 * r(x, y, z) ** 2) / r(x, y, z) ** 4,
    (4, 0):     lambda x, y, z: 3 / 16 * np.sqrt(1 / np.pi) * (35 * z ** 4 - 30 * z ** 2 * r(x, y, z) ** 2 + 3 * r(x, y, z) ** 4) / r(x, y, z) ** 4,
    (4, 1):     lambda x, y, z: 0.75 * np.sqrt(5 / (2 * np.pi)) * z * x * (7 * z ** 2 - 3 * r(x, y, z) ** 2) / r(x, y, z) ** 4,
    (4, 2):     lambda x, y, z: 3 / 8 * np.sqrt(5 / np.pi) (x ** 2 - y ** 2) * (7 * z ** 2 - r(x, y, z) ** 2) / r(x, y, z) ** 4,
    (4, 3):     lambda x, y, z: 0.75 * np.sqrt(35 / (2 * np.pi)) * z * x * (x ** 2 - 3 * y ** 2) / r(x, y, z) ** 4,
    (4, 4):     lambda x, y, z: 3 / 16 * np.sqrt(35 / np.pi) * (x ** 2 * (x ** 2 - 3 * y ** 2) - y ** 2 * (3 * x ** 2 - y ** 2)) / r(x, y, z) ** 4,
}
