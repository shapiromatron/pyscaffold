import pytest

from pyscaffold.work import super_add


def test_super_add():
    # test expected
    assert super_add(2, 2) == 4

    # test unexpected
    with pytest.raises(TypeError):
        super_add(2, "skunk")
