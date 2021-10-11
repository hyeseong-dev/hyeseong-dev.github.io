# 2_runtime_lists_with_timeit_module.py
# timeit() 메서드로 성능을 측정할 때는 임시로 가비지 컬렉션 기능이 중진된다. 가비지 컬렉션 수행 시간도 성능 측정에 같이 포함하고 싶다면, 다음과 같이 gc.enable()를 추가해야 한다. 


def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = list()
    for i in range(1000):
        l.append(i)

def test3():
    l = list(i for i in range(1000))

def test4():
    l = list(range(1000))


if __name__ == '__main__':
    import timeit
    t1 = timeit.Timer("test1()", "from __main__ import test1")
    print('concat', t1.timeit(number=1000), 'milliseconds')
    t2 = timeit.Timer("test2()", "from __main__ import test2")
    print('append', t2.timeit(number=1000), 'milliseconds')
    t3 = timeit.Timer("test3()", "from __main__ import test3")
    print('comprehension', t3.timeit(number=1000), 'milliseconds')
    t4 = timeit.Timer("test4()", "from __main__ import test4")
    print('list range', t4.timeit(number=1000), 'milliseconds')


