class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except Exception:
        raise InvalidInput

    
    if  (x1, y1) == (x2, y2) or \
        (x2, y2) == (x3, y3) or \
        (x3, y3) == (x1, y1) or \
        (x3 - x1) / (x2 - x1) == (y3 - y1) / (y2 - y1):
        raise BadTriangle

    return abs( 0.5 * ((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3)) )

while(s := input()):
    try:
        ans = triangleSquare(s)
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')
    else:
        print(f'{ans:.2f}')
        break
