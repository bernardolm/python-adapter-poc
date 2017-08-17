from adapter import Foo, Bar, DataAdapter


class TestDataAdapter:

    def test_init(self):
        adapter = DataAdapter(Foo, Bar)
        assert adapter.source == type(Foo)
        assert adapter.target == type(Bar)

    def test_foo2bar(self):
        foo = Foo()
        foo.name = 'Test foo'
        bar = DataAdapter(Foo, Bar).do(foo)
        assert bar.full_name == 'Test foo Bar name'
