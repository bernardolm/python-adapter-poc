from adapter import Foo, Bar, DataAdapter


class TestDataAdapter:

    def test_init(self):
        adapter = DataAdapter(Foo, Bar)
        assert adapter.source == type(Foo)
        assert adapter.target == type(Bar)

    def test_foo2bar(self):
        foo = Foo()
        foo.name = 'Test foo'
        actual = DataAdapter(Foo, Bar).do(foo)
        assert actual.full_name == 'Test foo Bar name'

    def test_foo2bar_1(self):
        foo = Foo()
        foo.name = 'Test foo'
        bar = Bar()
        bar.last_name = 'Test bar'
        actual = DataAdapter(Foo, Bar).do(foo, bar)
        assert actual.full_name == 'Test foo Test bar'
