from multipledispatch import adispatch

@adispatch()
def isint(x: int):
    return True

@adispatch()
def isint(x: object):
    return False

def test_simple():
    for i in xrange(100000):
        isint(5)
        isint('a')
