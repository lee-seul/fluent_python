# coding: utf-8 


def simple_coro2(a):
    print('start', a)
    b = yield a
    print('received b', b)
    c = yield a+b
    print('received c', c)


if __name__ == '__main__':
    my_coro2 = simple_coro2(14)
    from inspect import getgeneratorstate
    getgeneratorstate(my_coro2)

    next(my_coro2)
    getgeneratorstate(my_coro2)

    my_coro2.send(28)
    my_coro2.send(99)
    
    getgeneratorstate(my_coro2)
