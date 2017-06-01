import ctypes


class InvalidPosition(Exception):
    pass


def validate_w(pos):
    if pos < 'a' or pos > 'h':
        raise InvalidPosition()
    return ord(pos) - ord('a')


def validate_h(pos):
    pos = int(pos)
    if pos < 1 or pos > 8:
        raise InvalidPosition()
    return pos

def askdll(text: str):
    getPos = ctypes.CDLL('pyDll.dll').getPos
    getPos.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    getPos.restype = ctypes.c_bool

    text = text.lower()
    try:
        s0 = validate_w(text[0])
        s1 = validate_h(text[1])
        e0 = validate_w(text[2])
        e1 = validate_h(text[3])
    except (InvalidPosition, ValueError):
        return False,'Invalid Input'
    res = getPos(s0, s1, e0, e1)
    return True, res
    pass
