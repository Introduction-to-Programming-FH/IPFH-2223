from math import tan, sin, cos

def angle_calcs(angle):
    tan_v = tan(angle)
    sin_v = sin(angle)
    cos_v = cos(angle)
    return [sin_v, cos_v, tan_v]

print(angle_calcs(34))