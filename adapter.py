

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

    def do(self, source, target=None):
        if self.source is type(Foo) and self.target is type(Bar):
            return self._foo2bar(source, target)

        elif self.source is type(Bar) and self.target is type(Foo):
            return self._bar2foo(source, target)

        else:
            print('no callings')

    def _foo2bar(self, source, target=None):
        if target is None:
            target = Bar()
        target.full_name = source.name + ' ' + target.last_name
        return target

    def _bar2foo(self, source, target=None):
        if target is None:
            target = Foo()
        target.full_name = target.name + ' ' + source.last_name
        return target
