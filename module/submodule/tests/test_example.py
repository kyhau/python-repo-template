from submodule import main


def test_sample_function():
    assert 2 == main.sample_function(1, 1)


def test_main():
    assert 0 == main.main()

