

class Foo:
    def __init__(self):
        self.name = 'Foo name'


class Bar:
    def __init__(self):
        self.last_name = 'Bar name'


class DataAdapter:

    def __init__(self, source, target):
        self.source = type(source)
        self.target = type(target)

    def do(self, source):
        if self.source is type(Foo) and self.target is type(Bar):
            return self.foo2bar(source)

        elif self.source is type(Bar) and self.target is type(Foo):
            return self.bar2foo(source)

        else:
            print('no callings')

    def foo2bar(self, source):
        bar = Bar()
        bar.full_name = source.name + ' ' + bar.last_name
        return bar

    def bar2foo(self, source):
        foo = Foo()
        foo.full_name = foo.name + ' ' + source.last_name
        return foo
