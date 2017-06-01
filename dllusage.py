import ctypes


class ParseError(Exception):
    pass


class InvalidSymbol(ParseError):
    pass


class InvalidLength(ParseError):
    pass


def validate_w(sym):
    if sym < 'a' or sym > 'h':
        raise InvalidSymbol(sym)
    return ord(sym) - ord('a')


def validate_h(sym):
    sym = int(sym)
    if sym < 1 or sym > 8:
        raise InvalidSymbol(sym)
    return sym


def prepare_fn():
    dll_fn = ctypes.CDLL('pyDll.dll').getPos
    dll_fn.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
    dll_fn.restype = ctypes.c_bool
    return dll_fn


def parse_input(text):
    text = text.strip()
    if len(text) != 4:
        raise InvalidLength()
    text = text.lower()
    s0 = validate_w(text[0])
    s1 = validate_h(text[1])
    e0 = validate_w(text[2])
    e1 = validate_h(text[3])
    return [s0, s1, e0, e1]


def format_msg(ex):
    msg = str(type(ex).__name__)
    sex = str(ex)
    if sex:
        msg += ': ' + sex
    return msg


def askdll(text: str):
    dll_fn = prepare_fn()
    try:
        poslist = parse_input(text)
    except (ParseError, ValueError) as ex:
        return False, format_msg(ex)
    res = dll_fn(*poslist)
    return True, res
