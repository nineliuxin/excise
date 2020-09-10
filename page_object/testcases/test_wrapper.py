from functools import wraps

def f(a):
    print("第一次输出", a)
    def extend(fuc):
        def hello(*args, **kwargs):
            print("第二次输出", a)
            print("hello")
            fuc(*args, **kwargs)
            print("good bye")
        return hello
    return extend

def extend1(fuc):
    print("第一次输出")
    def hello(*args, **kwargs):
        print("第二次输出")
        print("hello")
        fuc(*args, **kwargs)
        print("good bye")
    return hello

@f("123")
def tmp():
    print("tmp")

@extend1
def tmp1():
    print("tmp1")


def test_wrapper():
    tmp1()

# if __name__ == '__main__':
#     tmp()